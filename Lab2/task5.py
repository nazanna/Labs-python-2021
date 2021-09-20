import turtle
import math
from random import *


turtle.color('Gray')
n = 10
a = 20

for i in range(n):
    
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
        
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    a += 20
    
    turtle.pendown()
