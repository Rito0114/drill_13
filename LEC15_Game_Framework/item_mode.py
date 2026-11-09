import game_framework
import play_mode
from pico2d import *

image = None

def init():
    global image

    image = load_image('item_select.png')

def finish():
    global image
    del image

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_0, SDLK_1, SDLK_2):
            play_mode.boy.selected_item = event.key - SDLK_0
            game_framework.pop_mode()
            return
        elif (event.type == SDL_KEYDOWN and
              event.key in (SDLK_i, SDLK_ESCAPE)):
            game_framework.pop_mode()
            return

def update():
    play_mode.update()

def render():
    clear_canvas()
    play_mode.render_scene()
    image.draw(400, 300)
    update_canvas()
