from display import *
import math

def draw_line(x0,y0,x1,y1,screen,color):
   # float slope = (max(y0,y1) - min(y0,y1)) / (x1 - x0))
    
    #Octant 1 / 5
    draw_line_one(x0,y0,x1,y1,screen,color)
    #Octant 2 / 6
    #Octant 7 / 3
    #Octant 8 / 4
    delta_y = y1 - y0
    delta_x = x1 - x0
    if (delta_y > 0):
        if (delta_x < delta_y):
            draw_line_two (x0, y0, x1, y1, screen, color)
        else:
            draw_line_one (x0, y0, x1, y1, screen, color)
    else:
        if (abs(delta_y) > abs(delta_x)):
            draw_line_seven (x0, y0, x1, y1, screen, color)
        else:
            draw_line_eight (x0, y0, x1, y1, screen, color)

#Octants 1 and 5.  
def draw_line_one(x0,y0,x1,y1,screen,color):
    if (x0 > x1):
        buffer = x1
        x1 = x0
        x0 = buffer
        buffer = y1
        y1 = y0
        y0 = buffer
        #^ If it's an octant 5 line ^
    x,y = x0,y0
    a = y1-y0
    b = -(x1-x0)
    d = 2 * a + b
    while (x <= x1):
        plot(screen,color,x,y)
        if d >= 0:
            y += 1
            d += 2 * b
        x += 1
        d += 2 * a
def draw_line_two(x0,y0,x1,y1,screen,color):
    if (x0 > x1):
        buffer = x1
        x1 = x0
        x0 = buffer
        buffer = y1
        y1 = y0
        y0 = buffer
        #^ If it's an octant 6 line ^
    x,y = x0,y0
    a = y1-y0
    b = -(x1-x0)
    d = 2 * b + a
    while y <= y1:
        plot(screen,color,x,y)
        if d < 0:
            x += 1
            d += 2 * a
        y += 1
        d += 2 * b
def draw_line_seven(x0,y0,x1,y1,screen,color):
    y0 *= -1
    y1 *= -1
    draw_line_two(x0,y0,x1,y1,screen,color)
def draw_line_eight(x0,y0,x1,y1,screen,color):
    y0 *= -1
    y1 *= -1
    draw_line_one(x0,y0,x1,y1,screen,color)  
screen = new_screen()
color = [0,98,51]
draw_line(0,600,350,500,screen,color)
draw_line(400,600,0,600,screen,color)
draw_line(0,600,400,600,screen,color)
#draw_line(200,0,50,500,screen,color)
#draw_line(200,0,550,500,screen,color)
#draw_line(400,600,50,500,screen,color)
display(screen)
save_extension(screen,'img.png')

