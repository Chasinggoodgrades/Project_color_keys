from turtle import *
from random import random
chase = Turtle()

#Screen / Drawing Setup
chase.width(10)
title("Color Keys!!!!")
textinput("Project Color Keys Instructions", "Use arrow keys to draw. You may change the colors using (r,g,b) as well as clear,undo, and reset using (c, Backspace, and v)")
chase.shape("turtle")
bgpic("Bing.png")
bgpic

cv = getcanvas
cv
#Arrow Key Functions
def up_arrow():
    chase.fd(100)
def down_arrow():
    chase.back(100)
def left_arrow():
    chase.left(45)
def right_arrow():
    chase.right(45)

#Undo/Clear Functions
def back_space():
    chase.undo()
def clear_game():
    chase.clear()
def reset_game():
    chase.reset()
    chase.width(10)

#Color Functions
def red():
    chase.color(1,0,0)
def blue():
    chase.color(0,0,1)
def green():
    chase.color(0,1,0)
def reset_color():
    chase.color(0,0,0)
def white():
    chase.color(1,1,1)
#Penup/Pendown Function
def space_bar():
    if chase.isdown():
        chase.penup()
    else:
        chase.pendown()


onclick(chase.goto)
#Spacebar for controling the pen
onkeypress(space_bar, "space")
# Choose a color
#Press r for Red
#Press b for Blue
#Press g for Green
#Press n for Black
#Press j for white eraser"
onkeypress(red, "r")
onkeypress(blue, "b")
onkeypress(green, "g")
onkeypress(reset_color, "n")
onkeypress(white, "j")
# Undo/Clear/Reset
onkeypress(back_space, "BackSpace")
onkeypress(clear_game, "c")
onkeypress(reset_game, "v")
# Draw with Arrow Keys
onkeypress(up_arrow, "Up")
onkeypress(down_arrow, "Down")
onkeypress(left_arrow, "Left")
onkeypress(right_arrow, "Right")
listen()
