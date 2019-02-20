from urllib.request import urlopen
from bs4 import BeautifulSoup
from game_info import GameInfo

GatewayList = ['Azeroth', 'Lordaeron', 'Northrend']

class BNetStatsScraper:
  def get_stats(name, gateway):
    if gateway not in GatewayList:
      raise ValueError('Invalid Gateway')

    page = urlopen('http://classic.battle.net/war3/ladder/' + GameInfo.get_game_version_str() + '-player-profile.aspx?Gateway=' + gateway + '&PlayerName=' + name)
    soup = BeautifulSoup(page, 'html.parser')
    solo_games_text = soup.find(text='Solo Games')
    if solo_games_text is None:
      return 0, 0

    solo_games = solo_games_text.find_parent('table')
    solo_wins = int(solo_games.find(text='Wins:').find_next('td').text.strip())
    solo_losses = int(solo_games.find(text='Losses:').find_next('td').text.strip())
    return solo_wins, solo_losses