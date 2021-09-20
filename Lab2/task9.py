import turtle
import math
from random import *

def prmn(n, r):
    turtle.color('Brown')
    alp = 360 / n
    a = 2 * r * math.sin(alp / 2 * math.pi / 180)
    
    turtle.penup()
    turtle.goto((- 1) * a / 2, (- 1) * r * math.cos(alp / 2 * math.pi / 180))
    turtle.pendown()
    
    for _ in range(n):
        turtle.forward(a)
        turtle.left(alp)
        
s = 20
for a in range(3, 11):
    prmn(a, s)
    s += 20
