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
    for i in range(len(A)):
        draw(A[i])
        space()

def space():
    t.penup()
    B = t.pos()
    t.goto(B[0] + 50, B[1])
    t.pendown()


inp = open('config.txt', 'r')
N0 = inp.readline().rstrip().split(', ')
N0[0] = N0[0][3::]
N1 = inp.readline().rstrip().split(', ')
N1[0] = N1[0][3::]
N2 = inp.readline().rstrip().split(', ')
N2[0] = N2[0][3::]
N3 = inp.readline().rstrip().split(', ')
N3[0] = N3[0][3::]
N4 = inp.readline().rstrip().split(', ')
N4[0] = N4[0][3::]
N5 = inp.readline().rstrip().split(', ')
N5[0] = N5[0][3::]
N6 = inp.readline().rstrip().split(', ')
N6[0] = N6[0][3::]
N7 = inp.readline().rstrip().split(', ')
N7[0] = N7[0][3::]
N8 = inp.readline().rstrip().split(', ')
N8[0] = N8[0][3::]
N9 = inp.readline().rstrip().split(', ')
N9[0] = N9[0][3::]
for i in range(len(N0)):
    N0[i] = N0[i].split()
    for n in range(3):
        N0[i][n] = int(N0[i][n])
for i in range(len(N1)):
    N1[i] = N1[i].split()
    for n in range(3):
        N1[i][n] = int(N1[i][n])
for i in range(len(N2)):
    N2[i] = N2[i].split()
    for n in range(3):
        N2[i][n] = int(N2[i][n])
for i in range(len(N3)):
    N3[i] = N3[i].split()
    for n in range(3):
        N3[i][n] = int(N3[i][n])
for i in range(len(N4)):
    N4[i] = N4[i].split()
    for n in range(3):
        N4[i][n] = int(N4[i][n])
for i in range(len(N5)):
    N5[i] = N5[i].split()
    for n in range(3):
        N5[i][n] = int(N5[i][n])
for i in range(len(N6)):
    N6[i] = N6[i].split()
    for n in range(3):
        N6[i][n] = int(N6[i][n])
for i in range(len(N7)):
    N7[i] = N7[i].split()
    for n in range(3):
        N7[i][n] = int(N7[i][n])
for i in range(len(N8)):
    N8[i] = N8[i].split()
    for n in range(3):
        N8[i][n] = int(N8[i][n])
for i in range(len(N9)):
    N9[i] = N9[i].split()
    for n in range(3):
        N9[i][n] = int(N9[i][n])
CON = list(map(int, input().split()))
numb = [N0, N1, N2, N3, N4, N5, N6, N7, N8, N9]
t.shape('turtle')
t.penup()
t.backward(300)
t.pendown()
paint(CON)