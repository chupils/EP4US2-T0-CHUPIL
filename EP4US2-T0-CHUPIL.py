#---------Computer Move Generation---------
from random import *
moves = ["R", "P", "S"]
comp = sample(moves,  1)   # Pick a random item from the list

#--------Game Intro and Player Input-------
print("ARE YOU READY TO PLAY SOME ROCK PAPER SCISSORS?")
player = input("ENTER YOUR MOVE (R, P, OR S)")

#-------------CALCULATION------------------
if (player == "R") or (player == "P") or (player == "S"):
    print("MY MOVE: ",comp[0])
    if (player == "R"):
        if (comp[0] == "R"):
            print("WE HAVE TIED")
        elif (comp[0] == "P"):
            print("HAHAHA...I WIN!")
        elif (comp[0] == "S"):
            print("FINE, YOU WIN")
    elif (player == "P"):
        if (comp[0] == "R"):
            print("FINE, YOU WIN")
        elif (comp[0] == "P"):
            print("WE HAVE TIED")
        elif (comp[0] == "S"):
            print("HAHAHA...I WIN!")
    elif (player == "S"):
        if (comp[0] == "R"):
            print("HAHAHA...I WIN!")
        elif (comp[0] == "P"):
            print("FINE, YOU WIN")
        elif (comp[0] == "S"):
            print("WE HAVE TIED")    
else: 
    print ("ERROR WITH INPUT: PLEASE ENTER R, P, OR S")
print("RUN PROGRAM TO PLAY AGAIN")
