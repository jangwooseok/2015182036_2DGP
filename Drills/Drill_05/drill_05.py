from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# 4
frame = 0
count = 0
x = []
y = []

def save_coord():
    global x, y
    x = [203, 132, 535, 477, 715, 316, 510, 692, 682, 712]
    y = [535, 243, 470, 203, 136, 225, 92, 518, 336, 349]





def move_charcter():
    global count
    global frame

    clear_canvas()
    if(count > 0):
        if(x[count-1] < x[count]):
            frame = 100
        else:
            frame = 0

    character.clip_draw(frame * 100, 100, 100, 100, x[count], y[count])
    update_canvas()
    delay(0.05)



while True:
    save_coord()
    move_charcter()
    count += 1
    if(count == 10):
        count = 0


    
close_canvas()
