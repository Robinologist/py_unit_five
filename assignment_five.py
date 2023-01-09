#THE GAME OF NIM

"""
Robin Engdahl
January 9th
A python recreation of the game of Nim, where two players take turns removing sticks from 3 piles.
The last person to draw a stick loses.
"""

import random                       #used for the computer's random moves
import time                         #used for delays

#setup game
boardRow1=["|","|","|"]             #the board is stored in 3 lists representing the rows, so I can easily add/take items
boardRow2=["|","|","|","|","|"]
boardRow3=["|","|","|","|","|","|","|"]


#define functions


#============================================#


def refreshBoard():
    print("",boardRow1,"\n",boardRow2,"\n",boardRow3)


#============================================#


def playerLose():                                           #self-explanatory
    print("You drew the final piece! You lose.")


#============================================#


def computerLose():                                         #also self-explanatory
    print("The computer drew the final piece. You win!")


#============================================#


def checkComputerLose():                                    #checks if there are any sticks left, if not then the computer must have drawn the last one
    if len(boardRow1) == 0 and len(boardRow2) == 0 and len(boardRow3) == 0:
        computerLose()
    else:
        gameloop()


#============================================#


def checkPlayerLose():                                      #checks if there are any sticks left, if not then the player must have drawn the last one
    if len(boardRow1) == 0 and len(boardRow2) == 0 and len(boardRow3) == 0:
        playerLose()
    else:
        computerTurn()


# ============================================#


def pickNewRow():                                           #picks a random row for the computer to take from
    Row = random.randint(1, 3)

                                                            #checks if the chosen row is empty and if it is, pick a different row
    if Row == 1 and len(boardRow1) == 0:
        return pickNewRow()
    elif Row == 2 and len(boardRow2) == 0:
        return pickNewRow()
    elif Row == 3 and len(boardRow3) == 0:
        return pickNewRow()
    else:
        return Row


#============================================#


def pickNewNumber(Row):                                     #picks a random number of sticks to take
    Number = random.randint(1, 7)

    if  Row == 1:                                           #checks if that number of sticks exists if the chosen row is row 1
        if Number > len(boardRow1):
            return pickNewNumber(Row)
        else:
            return Number

    elif  Row == 2:
        if Number > len(boardRow2):                         #checks if that number of sticks exists if the chosen row is row 2
            return pickNewNumber(Row)
        else:
            return Number

    elif  Row == 3:
        if Number > len(boardRow3):                         #checks if that number of sticks exists if the chosen row is row 3
            return pickNewNumber(Row)
        else:
            return Number


#============================================#


def computerTurn():
    editStickRow = pickNewRow()                         #Picks a random row
    editStickNumber = pickNewNumber(editStickRow)       #Picks a random number <= the length of the row

    # Take the sticks from the chosen row
    storeStickNumber = editStickNumber
    while editStickNumber > 0:
        if editStickRow == 1:
            del boardRow1[0]
        elif editStickRow == 2:
            del boardRow2[0]
        else:
            del boardRow3[0]
        editStickNumber = editStickNumber - 1

    time.sleep(1)
    print("The computer took", storeStickNumber, "sticks from row #",editStickRow)  # tells the player the computer's choice
    time.sleep(0.5)
    checkComputerLose()


#============================================#


def checkValidNumber(editStickRow,editStickNumber):

    if editStickNumber > 0:
        if editStickRow == 1:                             #checks if the player can take the requested # of sticks from the requested row
            if len(boardRow1) >= editStickNumber:
                while editStickNumber > 0:
                    del boardRow1[0]
                    editStickNumber = editStickNumber - 1

                refreshBoard()                            #if number and row are valid, show the player the updated board

            else:
                print("There aren't enough sticks in that row:")
                gameloop()


        if editStickRow == 2:
            if len(boardRow2) >= editStickNumber:
                while editStickNumber > 0:
                    del boardRow2[0]
                    editStickNumber = editStickNumber - 1
                refreshBoard()

            else:
                print("There aren't enough sticks in that row:")
                gameloop()


        if editStickRow == 3:
            if len(boardRow3) >= editStickNumber:
                while editStickNumber > 0:
                    del boardRow3[0]
                    editStickNumber = editStickNumber - 1
                refreshBoard()

            else:
                print("There aren't enough sticks in that row:")
                gameloop()

    else:
        print("That's not a valid number of sticks")
        gameloop()


#============================================#


def gameloop():  #The main loop of gameplay, in which the player takes their turn before calling the computer's turn function
    #player turn
    refreshBoard()
    editStickRow=int(input("Which row would you like to take sticks from?\nRow: "))
    if editStickRow >= 1 and editStickRow <= 3:
        editStickNumber = int(input("How many sticks would you like to take?\nNumber: "))
        checkValidNumber(editStickRow,editStickNumber)
    else:
        print("That's not a valid row")
        gameloop()

    if len(boardRow1) == 0 and len(boardRow2) == 0 and len(boardRow3) == 0:  #check if the board still has sticks, of not then the player took the last one and must lose
        playerLose()

    else:
        computerTurn()


#============================================#


#main
print("Welcome to NIM")
gameloop()