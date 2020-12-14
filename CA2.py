# CA2 Initial Thoughts
# Tasks:
# Create user interface and board
# Initially a 2 player game
# Handle user input
# playe1 move
# player2 move
# winner?
# draw?
# AI implementation
# pylint?
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



current_game = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
# Initialise our blank board



def display_board(board): # Board user interface function
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
    pass



def player2Move():
    pass



def aiMove():
    pass



def spaceFree():
    pass



def insertMove():
    pass



def checkWin():
    pass



def checkBoardFull():
    pass



# Execute functions in game - put in main()
def main():
    clear()
    print("Welcome to Padraic's Tic Tac Toe")
    # user_choice()

    

    display_board(current_game)


   
    #  testing
    print(list(enumerate(current_game)))

    print("Thank you for playing. Hope to see you soon!")



main()

