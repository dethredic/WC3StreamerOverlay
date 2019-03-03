from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re


def get_players_list():
  url = 'https://warcraft3.info/stats/player'
  page = urlopen(url)
  soup = BeautifulSoup(page, 'html.parser')
  player_urls = []
  for a in soup.find_all('a', {"class": "stats_player_field"}):
    link = a.get('href')
    player_urls.append(link)
  print('Found {} urls'.format(len(player_urls)))
  return player_urls

def get_players_alts(soup):
  alts = []
  for a in soup.find_all('a', {"title": re.compile(r'^Visit.*profile on Battle.net')}):
    if a is None:
      continue
    link = a.get('href')
    player_name_pat = re.compile(r'.*PlayerName=(.*)')
    player_name = player_name_pat.match(link).group(1)
    alts.append(player_name)
  return alts


player_urls = get_players_list()
aliases = {}

print('Finding aliases...')
for url in player_urls:
  page = urlopen(url)
  soup = BeautifulSoup(page, 'html.parser')
  pat = re.compile(r'.*/(.*)$')
  player = pat.match(url).group(1)
  alts = get_players_alts(soup)
  for alt in alts:
    aliases[alt] = player

print('Saving...')
with open('aliases.json', 'w') as of:
  json.dump(aliases, of)
of.close()

print('Work complete')
