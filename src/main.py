import json
import time

from bnet_player_monitor import BNetPlayerMonitor
from broadcast_server import BroadcastServer
from game_state import GameState
from player import Player


def obj_dict(obj):
  return obj.__dict__

def send_msg(server, type, data=None):
  server.send(json.dumps({'type': type, 'data': data}, default=obj_dict))

def set_my_id(player_list):
  ids = list(range(1, len(player_list) + 1))
  for player in player_list:
    if not player.is_me:
      ids.remove(player.id)

  for player in player_list:
    if player.is_me:
      player.id = ids[0]

def get_teams_from_player_list(player_list):
  team1 = []
  team2 = []

  my_team_is_even = True
  for player in player_list:
    if player.is_me:
      team1.append(player)
      my_team_is_even = player.id % 2

  for player in player_list:
    if not player.is_me:
      team1.append(player) if player.id % 2 == my_team_is_even else team2.append(player)

  return team1, team2

# A hack to copy AT stats RT stats. I need to re-think what the client gets sent
def set_at_stats(team):
  for at in team[0].at_stats:
    matches = 0
    for player in team:
      print('{} in {} ?'.format(player.name, at.partners))
      if player.name in at.partners:
        matches += 1;
        print('matches {}'.format(matches))
    if matches is len(team) - 1:
      for player in team:
        player.team_stats = at.stats

def handle_game_started(server, player_list):
  if len(player_list) is 0:
    # Tool started after a game has started
    return

  for player in player_list:
    player.print()
  set_my_id(player_list);

  team1, team2 = get_teams_from_player_list(player_list)

  set_at_stats(team1)
  set_at_stats(team2)

  send_msg(server, 'player_data', [team1, team2])
  send_msg(server, 'game_started')


def main():
  player_monitor = BNetPlayerMonitor()
  player_monitor.start()

  port = 6110
  server = BroadcastServer(port)
  server.start()
  server_connected = server.is_connected()

  game_state = GameState()
  game_state.open()
  is_in_game = False


  print('Initialized')

  while True:
    if not game_state.is_valid():
      # print('Game state invalid')
      # WC3 isn't running.
      if (is_in_game):
        print('Game closed')
        send_msg(server, 'game_ended')
        player_monitor.reset_players()
        is_in_game = False
      # If the game_state is open when WC3 is launched it will never be valid
      game_state.close()
      time.sleep(10)
      game_state.open()
      continue

    if server.is_connected() is not server_connected:
      server_connected = server.is_connected()
      if server_connected and is_in_game:
        # The client connected late (already in a game)
        # Give it the current info if valid
        handle_game_started(server, player_monitor.get_players())

    if is_in_game is not game_state.is_in_game():
      is_in_game = game_state.is_in_game()

      if is_in_game:
        # Delay a bit to allow the stat lookups to finish
        # This is more of a problem when the game loads too quick
        time.sleep(3)

        print('Game started')
        handle_game_started(server, player_monitor.get_players())
      else:
        print('Game ended')
        send_msg(server, 'game_ended')
        player_monitor.reset_players()

    time.sleep(1)

if __name__ == "__main__":
  main()
