import turtle as t
from random import *

def move(l, rad):
  t.forward(l)
  t.right(rad)

t.shape('turtle')
for i in range(100):
    l = randint(1, 100)
    rad = randint(0, 360)
    move(l, rad)
