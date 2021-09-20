import turtle
import math
from random import *

def zvezd(n, r):
    alp = 180 / n
    for i in range(n):
        turtle.forward(r)
        turtle.right(180 + alp)
    

turtle.penup()
turtle.goto(- 300, 0)
turtle.pendown()

zvezd(5, 200)

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

zvezd(11, 200)