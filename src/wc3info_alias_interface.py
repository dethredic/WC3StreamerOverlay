import re
import requests


class Wc3InfoAliasInterface:
  def __get_alias(player, data):
    alias = None
    for entry in data:
      if entry['aka'] is None or entry['aka'] is '':
        continue
      if entry['aka']['aka'] == player.name:
        alias = entry['aka']['player']['name']
    player.alias = alias

  def get_alias(player, gateway):
    url = 'https://warcraft3.info/stats/bnet_data?server=' + gateway
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
      Wc3InfoAliasInterface.__get_alias(player, response.json()['ranking'])
