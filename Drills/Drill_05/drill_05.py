from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# 2

count = 0
x, y = 0, 0
b_x, b_y = 0, 0
def save_coord(x, y):
    if(count == 0):
        x, y = 203, 535
    elif(count == 1):
        b_x, b_y = x, y
        x, y = 132, 243
    elif(count == 2):
        b_x, b_y = x, y
        x, y = 535, 470
    elif(count == 3):
        b_x, b_y = x, y
        x, y = 477, 203
    elif(count == 4):
        b_x, b_y = x, y
        x, y = 715, 136
    elif(count == 5):
        b_x, b_y = x, y
        x, y = 316, 225
    elif(count == 6):
        b_x, b_y = x, y
        x, y = 510, 92
    elif(count == 7):
        b_x, b_y = x, y
        x, y = 692, 518
    elif(count == 8):
        b_x, b_y = x, y
        x, y = 682, 336
    elif(count == 9):
        b_x, b_y = x, y
        x, y = 712, 349

frame = 0

def move_charcter():

    clear_canvas()
    if(b_x < x):
        frame = 100
    elif(b_x > x):
        frame = 0
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)

    delay(0.05)



while True:
    save_coord()
    move_charcter(x, y)
    count += 1
    if(count == 10):
        count = 0


    
close_canvas()
