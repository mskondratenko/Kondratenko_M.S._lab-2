#идеальный газ

from random import randint
import turtle as t
import math


numt = 30
time = 50

pool = [t.Turtle(shape = 'circle') for i in range(numt)]
for unit in pool:
    unit.turtlesize(0.3)
    unit.penup()
    unit.speed(1000)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.speed(randint(0, 500))

for i in range(time):
    for unit in pool:
        unit.forward(5)
        unit.right(randint(0, 360))