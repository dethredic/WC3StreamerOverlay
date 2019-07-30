import sys
sys.path.insert(0, '../src')

from player import Player

p1 = Player()
p1.id = 1
p1.is_me = True
p1.name = 'FollowGrubby'
p1.alias = 'Grubby'
p1.race = 'Orc'
p1.solo_stats.level = 49
p1.solo_stats.wins = 484
p1.solo_stats.losses = 79
p1.solo_stats.win_percent = 86
p1.team_stats.level = 30
p1.team_stats.wins = 123
p1.team_stats.losses = 8
p1.team_stats.win_percent = 86

p2 = Player()
p2.id = 2
p2.name = 'ILoveNecropolis'
p2.alias = 'Happy'
p2.race = 'Undead'
p2.solo_stats.level = 52
p2.solo_stats.wins = 1168
p2.solo_stats.losses = 19
p2.solo_stats.win_percent = 98
p2.team_stats.level = 40
p2.team_stats.wins = 1234
p2.team_stats.losses = 123
p2.team_stats.win_percent = 98

p3 = Player()
p3.id = 3
p3.is_me = True
p3.name = 'RomanticHuman'
p3.alias = 'ToD'
p3.race = 'Human'
p3.solo_stats.level = 47
p3.solo_stats.wins = 2590
p3.solo_stats.losses = 378
p3.solo_stats.win_percent = 87
p3.team_stats.level = 40
p3.team_stats.wins = 1234
p3.team_stats.losses = 1234
p3.team_stats.win_percent = 98

p4 = Player()
p4.id = 4
p4.name = '123456789012345'
p4.alias = 'Sonik'
p4.race = 'Night Elf'
p4.solo_stats.level = 43
p4.solo_stats.wins = 1493
p4.solo_stats.losses = 155
p4.solo_stats.win_percent = 91
p4.team_stats.level = 42
p4.team_stats.wins = 1493
p4.team_stats.losses = 155
p4.team_stats.win_percent = 91

p5 = Player()
p5.id = 5
p5.name = 'Dethredic'
p5.race = 'Random'
p5.solo_stats.level = 9
p5.solo_stats.wins = 20
p5.solo_stats.losses = 5
p5.solo_stats.win_percent = 80
p5.team_stats.level = 9
p5.team_stats.wins = 2000
p5.team_stats.losses = 2000
p5.team_stats.win_percent = 80

p6 = Player()
p6.id = 6
p6.name = 'abcdefghijklmnopqrstuvwxyz'
p6.alias = 'Dethredic'
p6.race = 'Orc'
p6.solo_stats.level = 25
p6.solo_stats.wins = 1000
p6.solo_stats.losses = 1000
p6.solo_stats.win_percent = 50
p6.team_stats.level = 4
p6.team_stats.wins = 50
p6.team_stats.losses = 1000
p6.team_stats.win_percent = 50

p7 = Player()
p7.id = 7
p7.name = 'mmmmmmmmmmmmmmm'
p7.race = 'Human'
p7.solo_stats.level = 25
p7.solo_stats.wins = 321
p7.solo_stats.losses = 321
p7.solo_stats.win_percent = 50
p7.team_stats.level = 25
p7.team_stats.wins = 456
p7.team_stats.losses = 456
p7.team_stats.win_percent = 50

p8 = Player()
p8.id = 8
p8.name = 'Qwe'
p8.race = 'Night Elf'
p8.solo_stats.level = 0
p8.solo_stats.wins = 0
p8.solo_stats.losses = 0
p8.solo_stats.win_percent = 0
p8.team_stats.level = 9
p8.team_stats.wins = 15
p8.team_stats.losses = 0
p8.team_stats.win_percent = 100

p9 = Player()
p9.id = 9
p9.name = 'feelsHuman'
p9.race = 'Human'
p9.solo_stats.wins = -1
p9.team_stats.wins = -1

p10 = Player()
p10.id = 10
p10.name = 'feelsUndeadMan'
p10.race = 'Undead'
p10.solo_stats.wins = -1
p10.team_stats.wins = -1