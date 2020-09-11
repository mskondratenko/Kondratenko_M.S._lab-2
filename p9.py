import turtle as t
import math as m

t.shape('turtle')
def regpol(n:int, r:tuple):
    t.penup()
    t.forward(r)
    t.pendown()
    deg = 180 * (n-2) / n
    side = 2 * r * m.sin(m.pi / n)
    t.left(180 - deg / 2)
    for i in range(n):
        t.forward(side)
        t.left(180 - deg)
    t.left(deg / 2)
    t.penup()
    t.forward(r)
    t.right(180)
    t.pendown()
n = int(input ('Сколько врешин в первом?'))
r = int(input('Какой радиус описанной окружносит вокруг первого?'))
step = int(input('Какой шаг радиуса?'))
k = int(input('Сколько вершин в последнем?'))
for i in range(k-n+1):
    regpol(n, r)
    n +=1
    r +=step