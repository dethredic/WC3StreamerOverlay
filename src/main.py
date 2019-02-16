import json
import time

from bnet_player_monitor import BNetPlayerMonitor
from broadcast_server import BroadcastServer
from game_state import GameState
from player import Player


def send_msg(server, type, data=None):
  server.send(json.dumps({'type': type, 'data': data}))

def handle_game_started(server, player_monitor):
  send_msg(server, 'game_started')

  me = player_monitor.get_me_data()
  opponent = player_monitor.get_opponent_data()
  me.print()
  opponent.print()
  send_msg(server, 'me_data', me.__dict__)
  send_msg(server, 'opponent_data', opponent.__dict__)

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

    if server.is_connected() != server_connected:
      server_connected = server.is_connected()
      if server_connected and is_in_game:
        # The client connected late (already in a game)
        # Give it the current info if valid
        handle_game_started(server, player_monitor)

    if is_in_game != game_state.is_in_game():
      is_in_game = game_state.is_in_game()

      if is_in_game:
        print('Game started')
        handle_game_started(server, player_monitor)
      else:
        print('Game ended')
        send_msg(server, 'game_ended')

    time.sleep(1)

if __name__ == "__main__":
  main()