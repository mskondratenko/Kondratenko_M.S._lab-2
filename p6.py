import turtle as t

n = int(input('Сколько лап?'))
degree = 360 / n
t.shape('turtle')
for i in range(n):
    t.forward(20)
    t.stamp()
    t.backward(20)
    t.right(degree)
t.hideturtle()