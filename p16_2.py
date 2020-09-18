import turtle as t

def draw(A):
    B = t.pos()
    for x, y, z in A:
        if z == 1:
            t.penup()
        t.goto(B[0] + x, B[1] + y)
        t.pendown()

def paint(A):
    for coord in A:
        draw(coord)
        space()

def space():
    t.penup()
    B = t.pos()
    t.goto(B[0] + 50, B[1])
    t.pendown()

t.shape('turtle')
t.penup()
t.backward(300)
t.pendown()
N1 = [(0, -50, 1), (50, 0, 0), (50, -100, 0), (50, 0, 0)]
N4 = [(0, -50, 0), (50, -50, 0), (50, -100, 0), (50, 0, 0)]
N7 = [(50, 0, 0), (0, -50, 0), (0, -100, 0), (50, 0, 1)]
N0 = [(0, -100, 0), (50, -100, 0), (50, 0, 0), (0, 0, 0), (50, 0, 0)]
INDEX = [N1, N4, N1, N7, N0, N0]
paint(INDEX)