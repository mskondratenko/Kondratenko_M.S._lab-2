import turtle as t

t.speed(1000)
t.shape('turtle')
def halfcircle(n):
    for i in range(90):
        t.forward(n)
        t.right(2)
t.left(90)
for i in range(10):
    halfcircle(2)
    halfcircle(0.5)


