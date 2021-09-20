import turtle
import math
from random import *

def circle(r):
    turtle.color('Green')
    turtle.width(2)
    turtle.speed(0.3)
    n = 200
    
    for i in range(n+1):
        turtle.forward(r)
        turtle.left(360 / n)

n = 6
for i in range(n):
    turtle.speed(3)
    circle(2)
    turtle.left(360 / n)