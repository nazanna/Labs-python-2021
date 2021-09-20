import turtle
from random import *
import math


numbers = ['f1 r90 f2 r90 f1 r90 f2 r90',
       'pu r90 f1 pd r225 f1.414213562373 r135 f2 pu r180 f2 r270 f1 r180 pd',
       'f1 r90 f1 r45 f1.414213562373 r225 f1 pu r180 f1 r90 f2 r90 pd',
       'f1 r135 f1.414213562373 r225 f1 r135 f1.414213562373 r135 pu f2 r90 pd',
       'r90 f1 r270 f1 r90 f1 r180 f2 r270 pu f1 r180 pd',
       'f1 r90 pu f1 pd f1 r90 f1 r90 pu f1 pd r90 f1 r180 f1 r90 f1 r90',
       'pu f1 pd r135 f1.414213562373 r225 f1 r90 f1 r90 f1 r90 f1 pu f1 pd r90',
       'f1 r135 f1.414213562373 r315 f1 r180 pu f2 pd r90',
       'f1 r90 f2 r90 f1 r90 f1 r90 f1 r180 f1 r90 f1 r90',
       'f1 r90 f1 r90 f1 r90 f1 r180 pu f2 pd r225 f1.414213562373 r225 pu f1 r90 f1 r90 pd']        

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
