import sys
from LevelVisualizer import LevelVisualizer

def main(game_path, level_path, tile_size):
	lv = LevelVisualizer(game_path, tile_size)

	with open(level_path, 'r') as level:
		level_str = level.read()
	img = lv.draw_level(level_str)
	img.show()

if __name__ == "__main__":
	game_path = sys.argv[1]
	level_path = sys.argv[2]
	if(len(sys.argv) > 3):
		tile_size = int(sys.argv[3])
	else:
		tile_size = 16
	main(game_path, level_path, tile_size)
