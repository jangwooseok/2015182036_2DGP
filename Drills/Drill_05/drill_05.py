from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# 커밋 횟수 5

frame = 0
count = 0

x_mul = 203
y_mul = 535

x = []
y = []

def save_coord():
    global x, y
    x = [203, 132, 535, 477, 715, 316, 510, 692, 682, 712]
    y = [535, 243, 470, 203, 136, 225, 92, 518, 336, 349]





def move_character():
    global count
    global frame
    global x_mul
    global y_mul

    clear_canvas()


    if(count == 9):
        frame = 0
    else:
        if (x[count] < x[count + 1]):
            frame = 1
        else:
            frame = 0

    character.clip_draw(100, frame * 100, 100, 100, x_mul, y_mul)

    if(count == 9):     #9 에서 0으로 갈 때
        if (x_mul <= x[0] and y_mul >= y[0]):
            count = 0
            x_mul = x[count]
            y_mul = y[count]
    elif(x[count] < x[count + 1] and y[count] < y[count + 1]):  #++
        if(x_mul >= x[count + 1] and y_mul >= y[count + 1]):
            count += 1
            x_mul = x[count]
            y_mul = y[count]
    elif(x[count] < x[count + 1] and y[count] > y[count + 1]):  #+-
        if (x_mul >= x[count + 1] and y_mul <= y[count + 1]):
            count += 1
            x_mul = x[count]
            y_mul = y[count]
    elif (x[count] > x[count + 1] and y[count] > y[count + 1]): #--
        if (x_mul <= x[count + 1] and y_mul <= y[count + 1]):
            count += 1
            x_mul = x[count]
            y_mul = y[count]
    elif(x[count] > x[count + 1] and y[count] < y[count + 1]):  #-+
        if (x_mul <= x[count] and y_mul >= y[count]):
            count += 1
            x_mul = x[count]
            y_mul = y[count]

    if count == 9:
            x_mul -= 1
            a = (y[count] - y[0]) / (x[count] - x[0])

    else:
        if (x[count] >= x[count + 1]):
            x_mul -= 1
        elif (x[count] < x[count + 1]):
            x_mul += 1

        a = (y[count] - y[count + 1]) / (x[count] - x[count + 1])

    y_mul = a * x_mul + y[count] - a*x[count] #기울기x + y



    update_canvas()
    delay(0.01)



save_coord()
while True:
    move_character()




    
close_canvas()
