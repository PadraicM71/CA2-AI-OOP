# CA2 Initial Thoughts
# Tasks:
# Create user interface and board - complete
# Initially a 2 player game - in progress
# Handle user input - in progress
# playe1 move - in progress
# player2 move - in progress
# winner? - in progress
# draw? - in progress
# AI implementation - choose algorithm! - not started
# pylint? - continious
#
# Clean up code continiously before every commit
# Comments - function comments etc before every commit



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
    to display player input
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
    
    move = input ("Please select a position for x ")
    try:
        move = int(move)
        if move > 0 and move < 10:
            if spaceFree(move):
                insertMove(move, 'x')
                    
                # current_game [move] = 'x'
            else:
                print("This space is occupied!!")
          

    except:
        print(current_game) # debugging    



def player2Move():
    pass



def aiMove():
    pass



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
    return (currentBoard[1] == xORo and currentBoard[2] == xORo and currentBoard[3] == xORo)
    #more winning combinations to be inserted.


def checkBoardFull():
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
    # user_choice()

# Still testing basic functions above

    display_board(current_game)

    player1Move()

    display_board(current_game)

    #
    print(list(enumerate(current_game)))

    print("Thank you for playing. Hope to see you soon!")



main()

