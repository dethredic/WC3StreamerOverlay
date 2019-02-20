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

def handle_game_started(server, player_list):
  send_msg(server, 'game_started')
  for player in player_list:
    player.print()
  send_msg(server, 'player_data', player_list)


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
        handle_game_started(server, player_monitor)

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