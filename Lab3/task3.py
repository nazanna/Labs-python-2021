import turtle
from random import *
import math


with open('numbers.txt','r') as number:
    numbers = []
    for line in number:
        numbers.append(line)
        
    turtle.color('Indigo')
    x = 30
    s = '141700'
    
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    
    for i in s:
       
        for a in numbers[int(i)].split():
            
            if a[0] == 'f':
                turtle.forward(x * float(a[1:]))
            
            if a[0] == 'r':
                turtle.right(float(a[1:]))
            
            if a == 'pu':
                turtle.penup()
            
            if a == 'pd':
                turtle.pendown()
                
        turtle.penup()
        turtle.forward(x * 2)
        turtle.pendown()