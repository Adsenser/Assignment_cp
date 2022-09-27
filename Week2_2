import turtle
import random
import math

def screenLeftClick(x,y):
    turtle.goto(x,y)
    
def screenRightClick(x,y):
    global r,g,b
    circle_size_x = abs(turtle.xcor()-x)
    circle_size_y = abs(turtle.ycor()-y)
    r = random.random()
    g = random.random()
    b = random.random()
    
    circle_r = math.sqrt((circle_size_x)**2 + (circle_size_y)**2)
    
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.circle(circle_r)
    
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
