import os

from pico2d import*
import game_framework
import logo_mode

os.chdir(os.path.dirname(os.path.abspath(__file__)))

open_canvas()
game_framework.run(logo_mode)
close_canvas()
