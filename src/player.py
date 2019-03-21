class Stats:
  def __init__(self):
    self.wins = None
    self.losses = None
    self.win_percent = None


class ATStats:
  def __init__(self):
    self.partners = []
    self.stats = Stats()

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
    self.at_stats = []

  def print(self):
    print('[{}] {} ({}) - Solo: W:{} L:{} ({}%) - Team: W:{} L:{} ({}%) - FFA: W:{} L:{} ({}%)'.format(self.id, self.name, self.race, self.solo_stats.wins, self.solo_stats.losses, self.solo_stats.win_percent, self.team_stats.wins, self.team_stats.losses, self.team_stats.win_percent, self.ffa_stats.wins, self.ffa_stats.losses, self.ffa_stats.win_percent))
    if self.at_stats:
      print('AT Stats:')
      for stat in self.at_stats:
        print('\t{}: W:{} L:{} ({})%'.format(' '.join(stat.partners), stat.stats.wins, stat.stats.losses, stat.stats.win_percent))
