import re
import requests


class Wc3InfoAliasInterface:
  def __get_alias(player, data):
    alias = None
    for entry in data:
      if entry['aka'] is None:
        continue
      if entry['daily_history']['name'] == player.name:
        alias_pat = re.compile(r'.*>(.*)</a>')
        alias = alias_pat.match(entry['aka']).group(1)
    player.alias = alias

  def get_alias(player, gateway):
    url = 'https://warcraft3.info/stats/bnet_data?server=' + gateway
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
      Wc3InfoAliasInterface.__get_alias(player, response.json()['data'])
