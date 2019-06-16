from player_data import *
from runner import *

matchups = [[[p1], [p2]], [[p3], [p4]], [[p5], [p6]], [[p7], [p8]], [[p9], [p10]]]

runner = TestRunner(matchups)
runner.start()

