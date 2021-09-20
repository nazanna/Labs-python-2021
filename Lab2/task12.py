import turtle
import math
from random import *

def arc(r):
    turtle.color('Black')
    n = 100
    
    for i in range(n):
        turtle.forward(r)
        turtle.right(180 / n)

n = 10
turtle.left(90)

turtle.penup()
turtle.goto(- 300, 0)
turtle.pendown()

for i in range(n):
    arc(1)
    arc(0.2)