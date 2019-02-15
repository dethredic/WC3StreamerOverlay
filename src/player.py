class Player:
  def __init__(self):
    self.name = None
    self.race = None
    self.wins = None
    self.losses = None
    self.win_percent = None

  def print(self):
    print('{} ({}) - W:{} L:{} ({}%)'.format(self.name, self.race, self.wins, self.losses, self.win_percent))