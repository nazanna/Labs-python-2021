import turtle
import math
from random import *

def arc(r):
    turtle.color('Black')
    n = 100
    
    for i in range(n):
        turtle.forward(r)
        turtle.right(180 / n)


def circle(r):
    turtle.color('Green')
    turtle.width(2)
    n = 200
    
    for i in range(n+1):
        turtle.forward(r)
        turtle.left(360 / n)
        

turtle.begin_fill()
circle(3)
turtle.color('Yellow')
turtle.end_fill()

turtle.penup()
turtle.color('Blue')
turtle.goto(- 30, 120)
turtle.pendown()

turtle.begin_fill()
circle(0.5)
turtle.color('Blue')
turtle.end_fill()

turtle.penup()
turtle.goto(30, 120)
turtle.pendown()

turtle.begin_fill()
circle(0.5)
turtle.color('Blue')
turtle.end_fill()

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()

turtle.width(10)
turtle.color('Black')
turtle.right(95)
turtle.forward(40)

turtle.color('Red')
turtle.penup()
turtle.goto(45, 70)
turtle.pendown()

n = 100
for i in range(n):
    turtle.forward(1.4)
    turtle.right(180 / n)