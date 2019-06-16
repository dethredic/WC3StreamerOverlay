from player import Player, Stats
import winreg
from urllib.request import urlopen
from bs4 import BeautifulSoup
from game_info import GameInfo

GatewayList = ['Azeroth', 'Lordaeron', 'Northrend']

class BNetStatsScraper:
  def __get_stat(soup, stat, text):
    section_text = soup.find(text=text)
    if section_text is None:
      stat.wins = 0
      stat.losses = 0
      stat.win_percent = 0
      return

    games = section_text.find_parent('table')
    stat.wins = int(games.find(text='Wins:').find_next('td').text.strip())
    stat.losses = int(games.find(text='Losses:').find_next('td').text.strip())
    games_played = stat.wins + stat.losses
    if games_played:
      stat.win_percent = int(100 * stat.wins / games_played)
    else:
      stat.win_percent = 0

  def get_stats(player, gateway):
    if gateway not in GatewayList:
      raise ValueError('Invalid Gateway')

    try:
      url = 'http://classic.battle.net/war3/ladder/' + GameInfo.get_game_version_str() + '-player-profile.aspx?Gateway=' + gateway + '&PlayerName=' + player.name
      page = urlopen(url, timeout=10)
      soup = BeautifulSoup(page, 'html.parser')
      BNetStatsScraper.__get_stat(soup, player.solo_stats, 'Solo Games')
      BNetStatsScraper.__get_stat(soup, player.team_stats, 'Team Games')
      BNetStatsScraper.__get_stat(soup, player.ffa_stats, 'FFA Games')
    except:
      player.solo_stats.wins = player.team_stats.wins = player.ffa_stats.wins = -1
