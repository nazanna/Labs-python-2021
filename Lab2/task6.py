import turtle
import math
from random import *


turtle.color('Gray')
turtle.shape('turtle')
a = 100
n = 12

for i in range(n):
    turtle.right(360 / n)
    turtle.forward(a)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(a)
    turtle.right(180)
