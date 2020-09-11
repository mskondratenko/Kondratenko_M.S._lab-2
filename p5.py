import turtle as t

t.shape('turtle')
n = 100
while n > 0:
    t.penup()
    t.forward(5)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.pendown()
    t.forward(n)
    t.right(90)
    t.forward(n)
    t.right(90)
    t.forward(n)
    t.right(90)
    t.forward(n)
    t.right(90)
    n -= 10
    t.penup()
t.hideturtle()