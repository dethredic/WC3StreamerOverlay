import mmap
from construct import *

ObserverSharedMemory = Struct(
  "version" / Int32ul,
  "refresh_rate" / Int32ul,
  "is_in_game" / Byte,
  "game_time_ms" / Int32ul,
  "players_count" / Byte,
  "game_name" / PaddedString(256, "utf8"),
  "map_name" / PaddedString(256, "utf8")
  # ... We don't care about the rest since it doesn't get populated when playing (only when observing)
)

class GameState():
  def __init__(self):
    self.shmem = None

  def __read(self):
    return ObserverSharedMemory.parse(self.shmem[:])

  def is_valid(self):
    return any(self.shmem[:])

  def is_in_game(self):
    return self.__read()['is_in_game'] == 1

  def open(self):
    print('Open')
    self.shmem = mmap.mmap(-1, ObserverSharedMemory.sizeof(), "War3StatsObserverSharedMemory", access=mmap.ACCESS_READ)

  def close(self):
    print('Close')
    self.shmem.close()