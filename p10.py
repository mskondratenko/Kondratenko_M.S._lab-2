
import turtle as t

t.speed(1000)
t.shape('turtle')
def doublecircle():
    for n in range(180):
        t.forward(2)
        t.right(2)
    for n in range(180):
        t.forward(2)
        t.left(2)
for n in range (3):
    doublecircle()
    t.right(60)