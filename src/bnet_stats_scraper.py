from player import Player, Stats, ATStats
import winreg
from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment
from game_info import GameInfo

GatewayList = ['Azeroth', 'Lordaeron', 'Northrend']

def calculate_win_percent(wins, losses):
  games_played = wins + losses
  if games_played:
    return int(100 * wins / games_played)
  else:
    return 0

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
    stat.win_percent = calculate_win_percent(stat.wins, stat.losses)


  def __get_at_stats(soup, at_stats):
    for at_section in soup.find_all(text='Partner(s):'):
      at_stat_section = at_section.find_parent('table').find_parent('table').find_parent('table')
      at_stat = ATStats()
      at_stat.stats.wins = at_stat_section.find(text='\xa0Wins:\xa0').find_parent('td').find_next_sibling('td').text.strip()
      at_stat.stats.losses = at_stat_section.find(text='\xa0Losses:\xa0').find_parent('td').find_next_sibling('td').text.strip()
      at_stat.stats.win_percent = calculate_win_percent(int(at_stat.stats.wins), int(at_stat.stats.losses))
      for partner in at_section.find_parent('table').find_next_sibling('b').find_all('a'):
        at_stat.partners.append(partner.text.strip())
      at_stats.append(at_stat)


  def get_stats(player, gateway):
    if gateway not in GatewayList:
      raise ValueError('Invalid Gateway')

    page = urlopen('http://classic.battle.net/war3/ladder/' + GameInfo.get_game_version_str() + '-player-profile.aspx?Gateway=' + gateway + '&PlayerName=' + player.name)
    soup = BeautifulSoup(page, 'html.parser')
    BNetStatsScraper.__get_stat(soup, player.solo_stats, 'Solo Games')
    BNetStatsScraper.__get_stat(soup, player.team_stats, 'Team Games')
    BNetStatsScraper.__get_stat(soup, player.ffa_stats, 'FFA Games')
    BNetStatsScraper.__get_at_stats(soup, player.at_stats)





if __name__ == "__main__":
  gateway = "Northrend"
  p1 = Player()
  p1.name = "Lfun]Flash"
  BNetStatsScraper.get_stats(p1, gateway)

  p2 = Player()
  p2.name = "imp."
  BNetStatsScraper.get_stats(p2, gateway)

  p3 = Player()
  p3.name = "slowturtle"
  BNetStatsScraper.get_stats(p3, gateway)

  set_at_stats([p1, p2, p3])

  p1.print()
  p2.print()
  p3.print()
