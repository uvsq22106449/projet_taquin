from random import randrange
from tkinter import *
import time 


#Source: https://prograide.com/pregunta/32072/la-faon-correcte-de-mettre-en-pause-un-programme-python
#ines
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

def retour(R):
    pass #(db.rollback())

def pause(): 
    programPause = raw_input("Press the <ENTER> key to continue") 
    pass #fonctionne pas, c'etatait pour mettre la partie en pause

def melanger(N):
    board=[[4*lin+1+col for col in range(4)]
        for lin in range(4)]

    empty=(3,3)

    for i in range(N):
        empty=echange(board, empty)
    return board

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

#ines
FONT=('Ubuntu', 27, 'bold')
master=Tk()
cnv=Canvas(master, width=400, height=400, bg='gray70')
cnv.pack(side='left')

btn=Button(text="Mélanger", command=init)
btn.pack()
btn=Button(text="RETOUR", command=init)
btn.pack()

lbl=Label(text="      ", font=('Ubuntu', 25, 'bold'),
          justify=CENTER, width=7)
lbl.pack(side="left")

cnv.bind("<Button-1>",clic)
init()

master.mainloop()
