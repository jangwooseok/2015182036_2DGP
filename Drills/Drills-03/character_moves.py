from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#CIRCLE

cx = 400
cy = 300


th = 0
r = 200
#CIRCLE


#SQUARE
xpos = 400
ypos = 100

x = 2
y = 0


is_square = 0

while(True):

    if(is_square == 1):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(xpos,ypos)
    
        if(xpos + 20 > 800-20):
            x = 0
            y = 2
        if(ypos + 20 >= 600 - 40):
            x = -2
            y = 0
        if(xpos -20 <= 0):
            x = 0
            y = -2
        if(ypos -20 < 90-20):
            ypos = 100
            x = 2
            y = 0
        if(ypos == 100 and xpos +2 == 400):
            is_square = 0

        xpos = xpos + x
        ypos = ypos + y
        delay(0.01)
        
    elif(is_square == 0):
        clear_canvas_now()
    
        c_xpos = math.cos(th + 3.14 * 1.5) * r + cx
        c_ypos = math.sin(th + 3.14 * 1.5) * r + cy
    

        grass.draw_now(400,30)
        character.draw_now(c_xpos,c_ypos)
        
        th = th + 0.01
        
        if (th > 6.28):
            th = 0
            is_square = 1
            
        delay(0.01)    
            
 
    
close_canvas()
