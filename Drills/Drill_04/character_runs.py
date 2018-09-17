from pico2d import *
open_canvas()
grass = load_image('grass.png')
#character = load_image('run_animation.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0

move_way = 0

while True:
    clear_canvas()
    grass.draw(400, 30)

    if move_way == 0:
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    if move_way == 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    if move_way == 0:
        x += 10
    elif move_way == 1:
        x -= 10
    if x + move_way > 800:
        move_way = 1
    if x + move_way < 0:
        move_way = 0
    delay(0.05)
    get_events()


close_canvas()

