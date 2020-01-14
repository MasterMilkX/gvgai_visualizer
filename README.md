# gvgai_visualizer 2.0
Render Levels Created for GVGAI

**To render a level with test.py:**
```bash 
python test.py file_path level_path [tile_size]
```

_file_path_: VGDL game description file  
_level_path_: ascii level description file  
_tile_size (optional)_: size of tiles for rendering  

**To render a level from atdelphi_plus results:**
```bash
python result_visualizer.py game_name result_level_path [tile render size]
```
_game_name_: the name of the VGDL game description (located in examples/ in the parent directory this is placed)
_result_level_path_: path of the result .txt file generated by atdelphi_plus
_tile render size (optional)_: the size of the tiles to render for the final image

**To render multiple levels at once from atdelphi_plus results:**
```bash
python multi_result_visualizer.py game_name level_directory [tile render size]
```
_game_name_: same as above
_level_directory_: the directory where all of the result .txt files for the levels are placed
_tile render size_: same as above
