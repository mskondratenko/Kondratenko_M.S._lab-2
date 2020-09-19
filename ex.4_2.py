#реальный газ

from random import randint
import turtle as t
import math


numt = 50
time = 50

place = [[0, 0]] * numt
speed = [0] * numt
pool = [t.Turtle(shape = 'circle') for i in range(numt)]
for unit in pool:
    unit.turtlesize(0.3)
    unit.penup()
    unit.speed(1000)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.right(randint(0, 360))
    sp = randint(0, 100)
    unit.speed(sp)
    k = pool.index(unit)
    place[k] = unit.pos()
    speed[k] = sp

for i in range(time):
    for unit in pool:
        i = pool.index(unit)
        unit.forward(math.floor(speed[i] * 0.1))
        (x, y) = unit.pos()
        place[i] = [0.1, 0.1]
        for x1 in range(-20, 21, 1):
            for y1 in range(-20, 21, 1):
                if [x + x1, y + y1] in place:
                    j = place.index([x + x1, y + y1])
                    (speed[i], speed[j]) = (speed[j], speed[i])
                    pool[i].right(randint(90, 180))
                    pool[j].right(randint(90, 180))
        place[i][0] = math.floor(x) 
        place[i][1] = math.floor(y)