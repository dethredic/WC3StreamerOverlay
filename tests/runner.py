import asyncio
import websockets
import json

def obj_dict(obj):
  return obj.__dict__

class TestRunner:
  def __init__(self, matchups):
    self.matchups = matchups

  async def __connection_handler(self, websocket, path):
    while True:
      for m in self.matchups:
        await websocket.send(json.dumps({'type': 'game_started'}))
        await websocket.send(json.dumps({'type': 'player_data', 'data': m}, default=obj_dict))
        await asyncio.sleep(6)
        await websocket.send(json.dumps({'type': 'game_ended'}))
        await asyncio.sleep(0.5)

  def start(self):
    start_server = websockets.serve(self.__connection_handler, 'localhost', 6110)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
