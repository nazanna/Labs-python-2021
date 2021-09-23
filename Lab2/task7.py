import turtle
import math
from random import *

turtle.speed(0)
turtle.color('Orange')
n = 360 * 20
a = 10

for i in range(n):
    fi = i * 2 * math.pi / 360
    x = a / 2 / math.pi * fi * math.cos (fi)
    y = a / 2 / math.pi * fi * math.sin (fi)
    turtle.goto(x, y)
