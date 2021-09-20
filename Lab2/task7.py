import turtle
import math
from random import *

turtle.color('Orange')
n = 360 * 2
a = 0.0

for i in range(n):
    turtle.right(720 * 3 / n)
    turtle.forward(a)
    a += 0.004
