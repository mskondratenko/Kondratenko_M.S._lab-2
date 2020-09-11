import turtle as t

t.shape('turtle')
t.right(180)
n = 11
for i in range(n):
    t.forward(300)
    t.left(180 - (180 - 180 * (n - 2) / n) / 2)