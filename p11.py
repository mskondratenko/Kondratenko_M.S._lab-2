import turtle as t

t.speed(1000)
t.shape('turtle')
def doublecircle(n):
    for i in range(180):
        t.forward(n)
        t.right(2)
    for i in range(180):
        t.forward(n)
        t.left(2)
n = 1
t.right(90)
for i in range(10):
    doublecircle(n)
    n +=0.3
