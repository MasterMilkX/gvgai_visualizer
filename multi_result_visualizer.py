import os
import sys
import math
from LevelVisualizer import LevelVisualizer
from PIL import Image

#import the arguments
if len(sys.argv) < 3:
	print("ERROR: Not enough arguments")
	print("$ python level_vis.py [location of VGDL game description] [location of level from AtDelphi+]")
	exit(0)

VGDL="../examples/gridphysics/" + sys.argv[1] + ".txt"	#get the game
LEVEL_DIR = sys.argv[2]										#get the levels
TILE_SIZE = 16
if len(sys.argv) > 3:
	TILE_SIZE = int(sys.argv[3])

#import the level visualizer
lv = LevelVisualizer(VGDL, TILE_SIZE)

#create the subdirectory for all of the images
img_dir = os.path.join(LEVEL_DIR,"level_imgs")
if not os.path.exists(img_dir):
	os.mkdir(img_dir)		

#get all the levels
LEVELS = [f for f in os.listdir(LEVEL_DIR) if os.path.isfile(os.path.join(LEVEL_DIR, f)) and sys.argv[1] in f]

fs = []
#create the level image representations
for LEVEL in LEVELS:
	binval = LEVEL.split("_")[1].replace(".txt", "")

	#parse the level file to just the level
	file = open(os.path.join(LEVEL_DIR,LEVEL), "r")
	f = file.readlines()
	is_level = False
	actual_level = []
	for l in f:
		if  not is_level:
			if (len(actual_level) == 0) and (("Level:" in l) or ("Elite:" in l) or ("Infeasible Levels " in l)):
			#if ("Level:" in l) or ("Elite:" in l):
			#if ("Infeasible Levels " in l):
				is_level = True
				continue
			''' print the stats
			else:
				print(l)
			'''
		else:
			if (l != "") and (l != "\n") and (l != " ") and ("," not in l):
				actual_level.append(l)
			else:
				is_level = False

	#no elite so ski
	if(len(actual_level) == 0):
		continue

	level_str = "".join(actual_level).strip().replace(" ", ".")
	#print(level_str)

	#run the module for the level visualization
	img = lv.draw_level(level_str)

	#save the level
	img.save(os.path.join(img_dir,binval+".png"),format='png')
	fs.append(img)


#place image levels in a grid
'''
fs = []
IMG_LEVELS = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f)) and (".png" in f)]
for IMG_LEVEL in IMG_LEVELS:
	im = Image.open(os.path.join(img_dir, IMG_LEVEL), 'r')
	fs.append(im)

'''

#get the image size
x,y = fs[0].size
print(str(len(fs)) + " images @ " + str(x)+" x "+str(y))

#set up the grids
ncol = int(math.sqrt(len(fs)))
nrow = int(len(fs) / ncol)
if len(fs) % ncol != 0:
	nrow += 1

print(str(ncol) + "x" + str(nrow))

#make the combined image
grid = Image.new('RGB', (x*ncol,y*nrow))
for i in range(len(fs)):
	px, py = x*int(i%ncol),y*int(i/ncol)
	grid.paste(fs[i],(px,py))

grid.save(os.path.join(LEVEL_DIR,"all_levels.png"),format='png')
grid.show()
