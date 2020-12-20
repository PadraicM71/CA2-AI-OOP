# CA2 

# Tasks:
# Create user interface and board - complete
# Initially a 2 player game - almost complete
# Handle user input - almost complete
# playe1 move - complete
# player2 move - complete
# winner? - complete
# draw? - complete
# AI basic random AI initally to test main game - complete
# AI implementation - choose algorithm! - complete
# pylint? - continious
# AI can go first or second - complete **************
# Clean up code continiously before every commit
# Comments - function comments etc before every commit
# Function comments to be cleaned up yet
#
# Full debugging to be completed yet



import random
from os import system, name 



# Define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



# Initialise our blank board
# 10 items in list - will only use index 1 to 9 for 
# board
current_game = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']



def display_board(board): # Board user interface function
    '''
    Tic Tac Toe Game Board
    User Interface
    Parameter passed is a list:
    Uses indices 1-9 in a list
    to display game board
    '''
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')



def player1Move():
    '''
    Accept player 1 input and validate it
    for correct input.
    Executes player 1 move if space is free.
    '''
    p1 = True
    while p1 == True:
        moveP1 = input ("Please choose a position for x Player 1: ")
        try:
            moveP1 = int(moveP1)
            if moveP1 in range (1,10):
                if spaceFree(moveP1):
                    p1 = False
                    insertMove(moveP1, 'x')
                else:
                    print("This position is taken already!")
            else:
                print("Please provide a valid position between 1-9 Player 1!")

        except:
            print("Please provide a number Player1!!")
           # print(current_game) # debugging



def player2Move():
    '''
    Accept player 2 input and validate it
    for correct input.
    Executes player 2 move if space is free.
    '''
    p2 = True
    while p2 == True:
        moveP2 = input ("Please choose a position for o Player 2: ")
        try:
            moveP2 = int(moveP2)
            if moveP2 in range (1,10):
                if spaceFree(moveP2):
                    p2 = False
                    insertMove(moveP2, 'o')
                else:
                    print("This position is taken already!")
            else:
                print("Please provide a valid position between 1-9 Player 2!")

        except:
            print("Please provide a number player2!!")
           # print(current_game) # debugging



def aiMove(aiGoFirstSecond, counter): # algorithm - computer move - can go first or second
    if aiGoFirstSecond == 0: # 0 implies 1st and assigns 'x' ------ 1 implies 2nd assigns 'o'
        assignXO = 'x'
        otherPlayer = 'o'
    else:
        assignXO = 'o'
        otherPlayer = 'x'

    availableMoves = [number for number,item in enumerate(current_game) if item == ' ']
    availableMoves.pop(0)  
    #print(availableMoves) # list of available moves

    #make a copy of current game board to evaluate its status and not change values of current_game
    boardCopy = []
    for i in current_game:
        boardCopy.append(i)
    #print (current_game)
    #print (boardCopy)
    print ("counter" + str(counter))
    #check for a possible win in the next move and take it
    for t in availableMoves:
        boardCopy[t] = assignXO
        if checkWin(boardCopy, assignXO):
            insertMove(t, assignXO)
            return
        else:
            boardCopy[t] = ' ' #reassign boardCopy to its origional status
                                #for evaluation below

    #check for a possible win in the next move by opponent and block it
    for h in availableMoves:
        boardCopy[h] = otherPlayer
        if checkWin(boardCopy, otherPlayer):
            insertMove(h, assignXO)
            return
        else:
            boardCopy[h] = ' ' #reassign boardCopy to its origional status
                                #important here in case of future changes to algorithm

    #if available take a corner
    cornersOpen = []
    for q in availableMoves:
        if q in [1,3,7,9]:
            cornersOpen.append(q)
    print(cornersOpen.count('x'))
    if counter < 2 and len(cornersOpen) < 4: # if human player chooses a corner on first game move
        insertMove(5, assignXO)                 #algorithm takes center
        return
    #my ai extra
    checkcountXcorner = []
    checkcountXcorner.append(current_game[1])
    checkcountXcorner.append(current_game[3])
    checkcountXcorner.append(current_game[7])
    checkcountXcorner.append(current_game[9])
    print(checkcountXcorner)
    if counter == 2 and checkcountXcorner.count('x') == 2 and aiGoFirstSecond == 1: # play position 4 if move count < 4 where player 1 picks 2 corners in row as first moves
        insertMove(4, assignXO)                                 #to block a double corner and player 1 goes first
        return
    if len(cornersOpen) > 0: #if more than 1 corner available choose a random one
        mC = random.choice(cornersOpen)
        insertMove(mC, assignXO)
        return

    if 5 in availableMoves: # if centre available take it
        insertMove(5, assignXO)
        return

    #if all of the above fulfilled pick random move - should be only positions [2,4,6,8] left
    finalMove = random.choice(availableMoves) 
    last = finalMove
    insertMove(last, assignXO)



def aiMoveRand(aiGoFirstSecond): # Basic Random ai used for testing later
    if aiGoFirstSecond == 0: # 0 implies 1st and assigns x - 1 implies 2nd assigns o
        assignXO = 'x'
    else:
        assignXO = 'o'
    availableMoves = [number for number,space in enumerate(current_game)
                        if space == ' ']
    availableMoves.pop(0)  #remove unused index 0
    rP = random.choice(availableMoves)
    insertMove(rP, assignXO)



def spaceFree(position):
    '''
    Checks position on Tic Tac Toe
    game board is free
    '''
    return current_game[position] == ' '
    # returns true if player selected position is free



def insertMove(position, letter):
    '''
    Inserts player move on
    Tic Tac Toe game board
    '''
    current_game [position] = letter



def checkWin(currentBoard, xORo):
    '''
    Checks for a game win by either
    player.
    '''
    return ((currentBoard[1] == xORo and currentBoard[2] == xORo and currentBoard[3] == xORo) or
            (currentBoard[4] == xORo and currentBoard[5] == xORo and currentBoard[6] == xORo) or
            (currentBoard[7] == xORo and currentBoard[8] == xORo and currentBoard[9] == xORo) or
            (currentBoard[1] == xORo and currentBoard[4] == xORo and currentBoard[7] == xORo) or
            (currentBoard[2] == xORo and currentBoard[5] == xORo and currentBoard[8] == xORo) or
            (currentBoard[3] == xORo and currentBoard[6] == xORo and currentBoard[9] == xORo) or
            (currentBoard[1] == xORo and currentBoard[5] == xORo and currentBoard[9] == xORo) or
            (currentBoard[3] == xORo and currentBoard[5] == xORo and currentBoard[7] == xORo))



def checkBoardFull(gameinprogress):
    '''
    Checks if game board is full
    '''
    if gameinprogress.count(' ') > 1:
        return False
    else:
        return True



# Execute functions in game - put in main()
def main():
    clear()

    print("Welcome to Padraic's Tic Tac Toe")

    choice = 'FirstSecond'
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("Would you like to go first (type 1) or second (type 2)? ")
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        if choice.isdigit():
            if int(choice) in range(1,3):
                within_range = True
            else:
                within_range = False
    choice = int(choice)

    display_board(current_game)

    counter = 1 #starts a counter for game moves - used for algorithm to decide initial moves
    while (checkBoardFull(current_game)) == False:
        if checkWin(current_game, 'o') == False:
            if choice == 1:
                player1Move()
            else:
                aiMove(0,counter) #here parameter (0) indicates computer is taking 1st move
            
            display_board(current_game)
        
        else:
            print("o has won this time!")
            break
        
        if checkWin(current_game, 'x') == False:
            if checkBoardFull(current_game) == False:
                if choice == 2:
                    player2Move()
                else:
                    aiMove(1,counter) #here parameter (1) indicates computer is taking 2nd move

                display_board(current_game)
            else:
                break
            counter += 1
        else:
            print("x has won this time!")
            break

    if (checkBoardFull(current_game) and
        checkWin(current_game, 'x') == False and
        checkWin(current_game, 'o') == False):
            print ("It's a draw!")
        # All 3 conditions must be satisified
        # for a draw - true,false,false.


#-------------------------------------------------
    # if spaceFree(5) == True:
    #     print("free space")
    # else:
    #     print("not free")

    # print(list(enumerate(current_game)))


main()

#ENDS