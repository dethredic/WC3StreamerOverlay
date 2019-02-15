from urllib.request import urlopen
from bs4 import BeautifulSoup

GatewayList = ['Azeroth', 'Lordaeron', 'Northrend', 'Kalimdor']

class BNetStatsScraper:
  def get_stats(name, gateway):
    if gateway not in GatewayList:
      raise ValueError('Invalid Gateway')

    page = urlopen('http://classic.battle.net/war3/ladder/W3XP-player-profile.aspx?Gateway=' + gateway + '&PlayerName=' + name)
    soup = BeautifulSoup(page, 'html.parser')
    solo_games_text = soup.find(text='Solo Games')
    if solo_games_text is None:
      return 0, 0

    solo_games = solo_games_text.find_parent('table')
    solo_wins = int(solo_games.find(text='Wins:').find_next('td').text.strip())
    solo_losses = int(solo_games.find(text='Losses:').find_next('td').text.strip())
    return solo_wins, solo_losses