import json
from scapy.all import sniff, raw, IP
from threading import Thread

from player import Player, Stats
from bnet_stats_scraper import BNetStatsScraper
from wc3info_alias_interface import Wc3InfoAliasInterface

RaceNameMap = {
  b'\x01': 'Human',
  b'\x02': 'Orc',
  b'\x04': 'Night Elf',
  b'\x08': 'Undead',
  b'\x20': 'Random'
}

# TODO: Get IPs from other Gateways
GatewayNetMap = {
  'Azeroth': '199.108.55.0/24',
  'Lordaeron': '12.129.236.0/24',
  'Northrend': '5.42.181.0/24',
}

class BNetPlayerMonitor(Thread):
  def __init__(self):
    super(BNetPlayerMonitor, self).__init__()
    self.daemon = True
    self.player_list = []
    self.gateway = None

  def __parse_player_packet(self, player, data, name_offset):
    player.name = str(data[name_offset:].split(b'\x00')[0], 'utf-8')
    race_offset = name_offset + len(player.name) + 6
    player.race = RaceNameMap[data[race_offset:race_offset + 1]]
    Wc3InfoAliasInterface.get_alias(player, self.gateway)
    # Setting the id doesn't work for yourself.
    # We fill it in later when we have the other IDs
    player.id = data[name_offset - 1]

  def __set_gateway(self, packet):
    if IP in packet:
      partial_ip = ".".join(str(packet[IP].dst).split('.')[0:-1])
      for name, ip in GatewayNetMap.items():
        if partial_ip in ip:
          print('Setting gateway: ' + name)
          self.gateway = name

  def __packet_callback(self, packet):
    raw_payload = raw(packet.payload.payload.payload)

    if raw_payload[:2] == b'\xf7\x1e':
      self.__set_gateway(packet)

      player = Player()
      player.is_me = True
      self.__parse_player_packet(player, raw_payload, 19)
      BNetStatsScraper.get_stats(player, self.gateway)
      self.player_list.append(player)
    elif raw_payload[:2] == b'\xf7\x06':
      player_offset = 0
      while player_offset is not -1:
        player = Player()
        self.__parse_player_packet(player, raw_payload[player_offset:], 9)
        BNetStatsScraper.get_stats(player, self.gateway)
        self.player_list.append(player)
        player_offset = raw_payload.find(b'\xf7\x06', player_offset + 1)

  def __build_filter(self):
    or_str = ' or '
    filter_str = ''
    for ip in GatewayNetMap.values():
      filter_str += 'net ' + ip + or_str
    return filter_str[:len(filter_str) - len(or_str)]

  def run(self):
    sniff(filter=self.__build_filter(), prn=self.__packet_callback, store=0)

  def reset_players(self):
    self.player_list = []

  def get_players(self):
    return self.player_list
