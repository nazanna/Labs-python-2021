import turtle
import math
from random import *

n = 100
turtle.color('Indigo')
turtle.shape('turtle')

for i in range(n):
    turtle.forward(randint(30, 90))
    turtle.right(randint(0, 180))