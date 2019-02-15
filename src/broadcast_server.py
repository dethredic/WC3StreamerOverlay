import websockets
import asyncio
from threading import Thread

class BroadcastServer(Thread):
  def __init__(self, port):
    Thread.__init__(self)
    self.daemon = True
    self.websocket = None
    self.port = port

  async def __connection_handler(self, websocket, path):
    print('Client connected')
    self.websocket = websocket
    try:
      await self.websocket.recv()
    except websockets.exceptions.ConnectionClosed:
      pass
    finally:
      print('Client disconnected')
      self.websocket = None

  def is_connected(self):
    return self.websocket is not None

  def send(self, data):
    if self.websocket is None:
      return
    coroutine = self.websocket.send(data)
    asyncio.run_coroutine_threadsafe(coroutine, self.event_loop)

  def run(self):
    self.event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(self.event_loop)

    ws_server = websockets.serve(self.__connection_handler, 'localhost', 6110)
    self.event_loop.run_until_complete(ws_server)
    self.event_loop.run_forever()