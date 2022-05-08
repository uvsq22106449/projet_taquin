from random import randrange
from tkinter import *

DELTA=20
DIST=10
moving=0

def multi(orig, empty):
    i, j=orig
    ii, jj=empty
    delta=(di, dj)=(ii-i, jj-j)
    if di!=0!=dj or di==dj==0:
        return None
    norm=max(abs(di), abs(dj))

    dirx, diry =(di//norm, dj//norm)
    L=[((ii-dirx, jj-diry), (ii, jj))]

    for k in range(norm-1):
        (a, b), destn=L[-1]
        pos=((a-dirx, b-diry), (a, b))
        L.append(pos)
    return L, (dirx, diry)

def anim(item, target, drtn):
    global moving
    L =cnv.coords(item)
    a=L[0]
    b=L[1]
    x, y=target
    u, v=drtn
    d=u*(x-a)+v*(y-b)
    if d>DIST:
        cnv.move(item, u*DIST, v*DIST)
        cnv.after(DELTA, anim, item, target, drtn)
    else:
        cnv.move(item, (x-a), (y-b))
        moving-=1

#Benjamin
def genererPlateauRandom() ->list:

    listePlateau=[ k for k in range(1,16)]

    shuffle(listePlateau)

    return listePlateau+[0]

def plateauValable(listePlateau:list) ->bool:

    cpt=0

    for i in range(1,16):

        if listePlateau[i-1]!=i:

            n=listePlateau.index(i)

            listePlateau[i-1],listePlateau[n]=listePlateau[n],listePlateau[i-1]

            cpt=cpt+1

    return cpt%2==0

def genererPlateauValable() -> list:

    listePlateau=genererPlateauRandom()

    while not plateauValable(listePlateau.copy()):

        listePlateau=genererPlateauRandom()

    matricePlateau=[listePlateau[:4],listePlateau[4:8],listePlateau[8:12],listePlateau[12:16]]

    return matricePlateau


def move_tile(orig, dstn, drtn):
    global moving
    i, j=orig
    nro=board[i][j]
    rect, txt=items[nro]
    ii, jj =dstn
    target=100*jj, 100*ii
    target_txt=100*jj+50, 100*ii+50

    anim(rect, target, drtn)
    anim(txt, target_txt, drtn)
    moving+=2

    board[i][j],board[ii][jj]=board[ii][jj], board[i][j]

def clic(event):
    global i_empty,j_empty
    i=event.y//100
    j=event.x//100

    r=multi((i,j),(i_empty,j_empty))
    if (r is None) or moving:
        return
    L, drtn=r
    for orig,dstn in L:
        move_tile(orig,dstn, drtn[::-1])
    i_empty=i
    j_empty=j




def voisins(n, i, j):
    return [(a,b) for (a, b) in
            [(i, j+1),(i, j-1), (i-1, j), (i+1,j)]
            if a in range(n) and b in range(n)]

def echange(board, empty):
    i, j=empty
    V=voisins(4, i, j)
    ii, jj=V[randrange(len(V))]
    board[ii][jj], board[i][j]=board[i][j],board[ii][jj]
    return ii, jj

def normal(board, empty):
    i_empty, j_empty = empty
    for i in range(i_empty, 4):
        (board[i][j_empty], board[i_empty][j_empty])= (
            board[i_empty][j_empty], board[i][j_empty])
        i_empty=i
    for j in range(j_empty, 4):
        board[i_empty][j], board[i_empty][j_empty]= (
            board[i_empty][j_empty],board[i_empty][j])
        j_empty=j

def melanger(N):
    board=[[4*lin+1+col for col in range(4)]
        for lin in range(4)]

    empty=(3,3)

    for i in range(N):
        empty=echange(board, empty)
    return board

def init(N=1000):
    global i_empty, j_empty, items, board, bravo
    cnv.delete("all")
    items=[None]

    board=melanger(N)
    for i in range(4):
        for j in range(4):
            if board[i][j]==16:
                i_empty, j_empty=i, j
    empty=i_empty, j_empty
    normal(board, empty)
    i_empty, j_empty=3,3
    items=[None for i in range(17)]

    for i in range(4):
        for j in range(4):
            x, y=100*j, 100*i
            A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
            rect=cnv.create_rectangle(A, B, fill="white")
            nro=board[i][j]
            txt=cnv.create_text(C, text=nro, fill="black",
                                font=FONT)
            items[nro]=(rect, txt)
    rect, txt=items[16]
    cnv.delete(txt)
    cnv.delete(rect)
    lbl.configure(text="")
    bravo=False


win=[[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

FONT=('Ubuntu', 27, 'bold')
master=Tk()
cnv=Canvas(master, width=400, height=400, bg='gray70')
cnv.pack(side='left')

btn=Button(text="Mélanger", command=init)
btn.pack()
btn=Button(text="RETOUR", command=init)#finir#
btn.pack()

lbl=Label(text="      ", font=('Ubuntu', 25, 'bold'),
          justify=CENTER, width=7)
lbl.pack(side="left")

cnv.bind("<Button-1>",clic)
init()


master.mainloop()
