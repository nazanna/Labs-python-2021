import turtle
from random import *
import math


turtle.shape('turtle')
turtle.color('magenta')

x = -200
y = -80
vx = 10
vy = 70
ay = -10
tp = 2 * vy / ay * (-1)
n = 100   

turtle.penup()
turtle.goto(x, y)
turtle.pendown()

while vy > 1:
    
    for _ in range(n):
        turtle.goto(x,y)
        dt = tp / n
        x += vx * dt
        y += vy * dt + ay * dt ** 2 / 2
        vy += ay * dt
        
    vy *= -0.7
    tp = 2 * vy / ay * (-1)