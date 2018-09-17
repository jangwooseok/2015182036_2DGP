from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 2

count = 0
x, y = 0, 0
def save_coord():
    if(count == 0):
        x, y = 203, 535
    if(count == 0):
        x, y = 132, 243
    if(count == 0):
        x, y = 535, 470
    if(count == 0):
        x, y = 477, 203
    if(count == 0):
        x, y = 715, 136
    if(count == 0):
        x, y = 316, 225
    if(count == 0):
        x, y = 510, 92
    if(count == 0):
        x, y = 692, 518
    if(count == 0):
        x, y = 682, 336
    if(count == 0):
        x, y = 712, 349

    pass

def move_charcter(x, y):

    clear_canvas()
    #character.clip_draw(frame * 100, 100, 100, 100, x, 90)

    delay(0.05)
    pass


while True:
    save_coord()
    move_charcter(x, y)


    
close_canvas()
