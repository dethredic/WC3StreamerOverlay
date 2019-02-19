from scapy.all import sniff, raw, IP
from threading import Thread

from player import Player
from bnet_stats_scraper import BNetStatsScraper

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
    self.me = Player()
    self.opponent = Player()
    self.gateway = None

  def __get_player_stats(self, player):
    player.wins, player.losses = BNetStatsScraper.get_stats(player.name, self.gateway)
    games_played = player.wins + player.losses
    if games_played:
      player.win_percent = int(100 * player.wins / games_played)
    else:
      player.win_percent = 0

  def __parse_player_packet(self, player, data, offset):
    player.name = str(data[offset:].split(b'\x00')[0], 'utf-8')
    race_offset = offset + len(player.name) + 6
    player.race = RaceNameMap[data[race_offset:race_offset + 1]]

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
      self.__parse_player_packet(self.me, raw_payload, 19)
      self.__get_player_stats(self.me)
    elif raw_payload[:2] == b'\xf7\x06':
      self.__parse_player_packet(self.opponent, raw_payload, 9)
      self.__get_player_stats(self.opponent)

  def __build_filter(self):
    or_str = ' or '
    filter_str = ''
    for ip in GatewayNetMap.values():
      filter_str += 'net ' + ip + or_str
    return filter_str[:len(filter_str) - len(or_str)]

  def run(self):
    sniff(filter=self.__build_filter(), prn=self.__packet_callback, store=0)

  def get_me_data(self):
    return self.me

  def get_opponent_data(self):
    return self.opponent