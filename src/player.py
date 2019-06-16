class Stats:
  def __init__(self):
    self.wins = None
    self.losses = None
    self.win_percent = None

class Player:
  def __init__(self):
    self.id = None
    self.is_me = False
    self.name = None
    self.alias = None
    self.race = None
    self.solo_stats = Stats()
    self.team_stats = Stats()
    self.ffa_stats = Stats()

  def print(self):
    if self.solo_stats.wins == -1 or self.team_stats.wins == -1 or self.ffa_stats.wins == -1:
      print('Can not reach battle.net webprofiles for: ')
      print('[{}] {} ({})'.format(self.id, self.name, self.race))
    else:
      self.__print()

  def __print(self):
    print('[{}] {} ({}) - Solo: W:{} L:{} ({}%) - Team: W:{} L:{} ({}%) - FFA: W:{} L:{} ({}%)'.format(self.id, self.name, self.race, self.solo_stats.wins, self.solo_stats.losses, self.solo_stats.win_percent, self.team_stats.wins, self.team_stats.losses, self.team_stats.win_percent, self.ffa_stats.wins, self.ffa_stats.losses, self.ffa_stats.win_percent))
