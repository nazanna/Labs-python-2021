import turtle
import math
from random import *

def task2():
    turtle.color('Purple')
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


def task3(a = 60):
    turtle.color('Blue')
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)

def task4():
    turtle.color('Green')
    turtle.width(2)
    n = 300
    for i in range(n):
        turtle.forward(3)
        turtle.left(360 / n)


def task5():
    turtle.color('Gray')
    #turtle.shape('arrow')
    n = 10
    a = 20
    for i in range(n):
        task3(a)
        turtle.penup()
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(10)
        turtle.right(180)
        a += 20
        turtle.pendown()

def task6(n):
    turtle.color('Gray')
    turtle.shape('turtle')
    a = 100
    for i in range(n):
        turtle.right(360 / n)
        turtle.forward(a)
        turtle.stamp()
        turtle.right(180)
        turtle.forward(a)
        turtle.right(180)
        
def task7():
    turtle.color('Orange')
    n = 360 * 2
    a = 0.0
    for i in range(n):
        turtle.right(720 * 3 / n)
        turtle.forward(a)
        a += 0.004

def task8():
    turtle.color('Red')
    a = 6
    n = 60
    for i in range(n):
        turtle.forward(a)
        turtle.left(90)
        a += 3
        
def prmn(n, r):
    turtle.color('Brown')
    alp = 360 / n
    a = 2 * r * math.sin(alp / 2 * math.pi / 180)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.goto((- 1) * a / 2, (- 1) * r * math.cos(alp / 2 * math.pi / 180))
    turtle.pendown()
    for _ in range(n):
        turtle.forward(a)
        turtle.left(alp)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    #turtle.forward(30)

def task9():
    s = 20
    for a in range(3, 11):
        prmn(a, s)
        s += 20
        
def circle(r):
    turtle.color('Green')
    turtle.width(2)
    turtle.speed(0.3)
    n = 200
    for i in range(n+1):
        turtle.forward(r)
        turtle.left(360 / n)

def task10():
    n = 6
    for i in range(n):
        turtle.speed(3)
        circle(2)
        turtle.left(360 / n)

def task11():
    n = 12
    r = 1
    turtle.left(90)
    for i in range(n):
        circle(r)
        turtle.right(180)
        circle(r)
        r+=0.3

def arc(r):
    turtle.color('Black')
    turtle.speed(0.3)
    n = 100
    for i in range(n):
        turtle.forward(r)
        turtle.right(180 / n)

def task12():
    n = 10
    turtle.left(90)
    turtle.penup()
    turtle.goto(- 300, 0)
    turtle.pendown()
    for i in range(n):
        arc(1)
        arc(0.2)
        
def task13():
    turtle.begin_fill()
    circle(3)
    turtle.color('Yellow')
    turtle.end_fill()
    
    turtle.penup()
    turtle.color('Blue')
    turtle.goto(- 30, 120)
    turtle.pendown()
    
    turtle.begin_fill()
    circle(0.5)
    turtle.color('Blue')
    turtle.end_fill()
    turtle.penup()
    turtle.goto(30, 120)
    turtle.pendown()
    
    turtle.begin_fill()
    circle(0.5)
    turtle.color('Blue')
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    
    turtle.width(10)
    turtle.color('Black')
    turtle.right(95)
    turtle.forward(40)
    
    turtle.color('Red')
    turtle.penup()
    turtle.goto(45, 70)
    turtle.pendown()
    
    turtle.speed(0.3)
    n = 100
    for i in range(n):
        turtle.forward(1.4)
        turtle.right(180 / n)

def zvezd(n, r):
    alp = 180 / n
    for i in range(n):
        turtle.forward(r)
        turtle.right(180 + alp)
    
def task14():
    turtle.penup()
    turtle.goto(- 300, 0)
    turtle.pendown()
    zvezd(5, 200)
    turtle.penup()
    turtle.goto(150, 0)
    turtle.pendown()
    zvezd(11, 200)

def task1():
    n = 100
    turtle.color('Indigo')
    turtle.shape('turtle')
    for i in range(n):
        turtle.forward(randint(30, 90))
        turtle.right(randint(0, 180))
        

def task():
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

def taskfile():
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

def taskflight():
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
    
        
def haos():
    pool = [turtle.Turtle(shape='circle') for i in range(20)]
    for unit in pool:
        unit.penup()
        unit.goto(randint(-300,300),randint(-200,200))
    for _ in range(1000):
        for unit in pool:
            unit.penup()
            unit.speed(50)
            unit.right(randint(0,360))
            unit.forward(random() * 20)

taskflight()











    
