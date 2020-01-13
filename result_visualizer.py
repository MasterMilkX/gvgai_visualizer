import os
import sys
from LevelVisualizer import LevelVisualizer

#import the arguments
if len(sys.argv) < 3:
	print("ERROR: Not enough arguments")
	print("$ python level_vis.py [location of VGDL game description] [location of level from AtDelphi+]")
	exit(0)

VGDL="../examples/gridphysics/" + sys.argv[1] + ".txt"	#get the game
LEVEL = sys.argv[2]										#get the levels
TILE_SIZE = 16
if len(sys.argv) > 3:
	TILE_SIZE = int(sys.argv[3])

#parse the level file to just the level
file = open(LEVEL, "r")
f = file.readlines()

is_level = False
actual_level = []
for l in f:
	if  not is_level:
		if "Level:" in l:
			is_level = True
			continue
		else:
			print(l)
	else:
		actual_level.append(l)
level_str = "".join(actual_level).strip().replace(" ", ".")

#run the module for the level visualization
lv = LevelVisualizer(VGDL, TILE_SIZE)
img = lv.draw_level(level_str)
img.show()
