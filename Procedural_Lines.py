#=============FURRO404=============#
#ART.PY
import turtle
import random

Canvas_Size = 750
Density = 50

t = turtle.Turtle()
t.width(2.5)
t.speed(0)

s = turtle.Screen()
s.colormode(255)
s.bgcolor(24,24,24)

s.setup(Canvas_Size, Canvas_Size)
t.penup()
#-----------------------#
COLOR_LIST = [
    (178,164,236), (163,155,203), (146,170,231), (235,211,211), (214,223,174),
    (164,219,147), (231,179,213), (227,149,163), (164,235,231), (188,134,186)
    ]
#-----------------------#
def draw_line(row, col):
    Lower_Left = (
        (col * Canvas_Size / Density) - Canvas_Size / 2,
        (row * Canvas_Size / Density) - Canvas_Size / 2
    )
    Upper_Right = (
        ((col + 1) * Canvas_Size / Density) - Canvas_Size / 2,
        ((row + 1) * Canvas_Size / Density) - Canvas_Size / 2
    )
    Lower_Right = (
        ((col + 1) * Canvas_Size / Density) - Canvas_Size / 2,
        (row * Canvas_Size / Density) - Canvas_Size / 2
    )
    Upper_Left = (
        (col * Canvas_Size / Density) - Canvas_Size / 2,
        ((row + 1) * Canvas_Size / Density) - Canvas_Size / 2
    )

    direction = random.randint(0, 1)
    Color_Choice = random.choice(COLOR_LIST)
    t.pencolor(Color_Choice)

    if direction == 0:
        t.goto(Upper_Left)
        t.pendown()
        t.goto(Lower_Right)
        t.penup()
        
    elif direction == 1:
        t.goto(Lower_Left)
        t.pendown()
        t.goto(Upper_Right)
        t.penup()
#-----------------------#
t.hideturtle()

for row in range(Density):
    for col in range(Density):
        draw_line(row, col)
#=============FURRO404=============#
