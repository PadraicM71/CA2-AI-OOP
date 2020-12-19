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
# AI implementation - choose algorithm! - not started
# pylint? - continious
#
# Clean up code continiously before every commit
# Comments - function comments etc before every commit
# Function comments to be cleaned up yet
#
# Full debugging to be completed yet

import random

# Clear screen function
from os import system, name 
# Define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


#-----------------------------------------------------------
# Initial thoughts on function for handling user input below
# Most likely replace this function with try / except later
# def user_choice(): # Will do try/except later?
#     '''
#     User inputs a number (1-9) and we return this in integer form.
#     No parameter is passed when calling this function.
#     '''
#     choice = 'wrong'
#     within_range = False
#     while choice.isdigit() == False or within_range == False:
#         choice = input("Choose one of these numbers (1-9): ")
#         if choice.isdigit() == False:
#             print("Sorry that is not a digit!")
#         if choice.isdigit():
#             if int(choice) in range(1,9):
#                 within_range = True
#             else:
#                 within_range = False
#     clear()
#     return int(choice)
#-----------------------------------------------------------


current_game = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
# Initialise our blank board
# 10 items in list - will only use index 1 to 9 for 
# board



def display_board(board): # Board user interface function
    '''
    Tic Tac Toe Game Board
    User Interface
    Parameter passed is a list:
    Uses indices 1-9 in a list
    to display game board
    '''
    # clear()
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
                    # current_game debugging
                else:
                    print("This position is taken already!")
            else:
                print("Please provide a valid position between 1-9 Player 1!")

        except:
            print("Please provide a number Player1!!")
            print(current_game) # debugging



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
                    # current_game debugging
                else:
                    print("This position is taken already!")
            else:
                print("Please provide a valid position between 1-9 Player 2!")

        except:
            print("Please provide a number player2!!")
            print(current_game) # debugging



def aiMove(): # Advanced ai
    pass

def aiMoveRand(aiGoFirstSecond): # Basic Random ai used for testing later
    if aiGoFirstSecond == 0: # 0 implies 1st and assigns x - 1 implies 2nd assigns o
        assignXO = 'x'
    else:
        assignXO = 'o'
    availableMoves = [number for number,space in enumerate(current_game)
                        if space == ' ']
    availableMoves.pop(0)  #remove unused index 0
    print(availableMoves)
    moveP2 = random.choice(availableMoves)
    insertMove(moveP2, assignXO)

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

    choice = input ( "Would you like to go first (type 1) or second (type 2)? ")
    q = int(choice)
    #     if q == 1:
            
    #     elif x == 2:
    #         goFirst = aiMoveRand(1)
    #         goSecond = player2Move()
    #     else:
    #         print("That is not 1 or 2")
    # except:
    #     print("Please provide a valid input when you play next time!")


    display_board(current_game)


    while (checkBoardFull(current_game)) == False:
        if checkWin(current_game, 'o') == False:
            if q ==1:
                player1Move()
            else:
                aiMoveRand(0)
            
            display_board(current_game)
            #print(checkBoardFull(current_game)) #debugging
        else:
            print("o has won this time!")
            break
        
        if checkWin(current_game, 'x') == False:
            if checkBoardFull(current_game) == False:
                if q ==2:
                    player2Move()
                else:
                    aiMoveRand(1)

                display_board(current_game)
            else:
                break

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

# while True:
#     try:
#         goAgain = input("Whould you like to try again? Enter y for yes. ")
#         if goAgain == 'y':
#             main()
#         else:
#             break
#     except:
#         break
# print("Thank you for playing.")

