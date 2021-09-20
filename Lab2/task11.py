import turtle
import math
from random import *

def circle(r):
    turtle.color('Green')
    turtle.width(2)
    n = 200
    
    for i in range(n+1):
        turtle.forward(r)
        turtle.left(360 / n)

n = 12
r = 1
turtle.left(90)

for i in range(n):
    circle(r)
    turtle.right(180)
    circle(r)
    r+=0.3