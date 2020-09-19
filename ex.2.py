import turtle as t

def draw(i):
    B = t.pos()
    C = numb[i]
    for x, y, z in C:
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


N0 = [(0, -100, 0), (50, -100, 0), (50, 0, 0), (0, 0, 0), (50, 0, 0)]
N1 = [(0, -50, 1), (50, 0, 0), (50, -100, 0), (50, 0, 0)]
N2 = [(50, 0, 0), (50, -50, 0), (0, -100, 0), (50, -100, 0), (50, 0, 1)]
N3 = [(50, 0, 0), (0, -50, 0), (50, -50, 0), (0, -100, 0), (50, 0, 1)]
N4 = [(0, -50, 0), (50, -50, 0), (50, -100, 0), (50, 0, 0)]
N5 = [(0, -100, 1), (50, -100, 0), (50, -50, 0), (0, -50, 0), (0, 0, 0), (50, 0, 0)]
N6 = [(0, -50, 1), (0, -100, 0), (50, -100, 0), (50, -50, 0), (0, -50, 0), (50, 0, 0)]
N7 = [(50, 0, 0), (0, -50, 0), (0, -100, 0), (50, 0, 1)]
N8 = [(0, -100, 0), (50, -100, 0), (50, 0, 0), (0, 0, 0), (50, 0, 0), (0, -50, 1), (50, -50, 0), (50, 0, 1)]
N9 = [(0, -100, 1), (50, -50, 0), (50, 0, 0), (0, 0, 0), (0, -50, 0), (50, -50, 0), (50, 0, 1)]
INDEX = input().split()
for i in range(len(INDEX)):
    INDEX[i] = int(INDEX[i])
numb = [N0, N1, N2, N3, N4, N5, N6, N7, N8, N9]
t.shape('turtle')
t.penup()
t.backward(300)
t.pendown()
paint(INDEX)