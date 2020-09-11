import turtle as t

t.shape('turtle')
t.speed(100000)
step = 10
for n in range(360 * 10):
    t.forward(step)
    step +=0.1
    t.right(10)
