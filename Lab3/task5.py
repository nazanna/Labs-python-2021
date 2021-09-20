import turtle
from random import *
import math


pool = [turtle.Turtle(shape='circle') for i in range(20)]

for unit in pool:
    unit.penup()
    unit.goto(randint(-300,300),randint(-200,200))
    
for _ in range(1000):
    
    for unit in pool:
        unit.penup()
        unit.speed(0)
        unit.right(randint(0,360))
        unit.forward(random() * 15)