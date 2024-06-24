# list of constants to make the code more readable later
# X will be represented by a positive 1
# O is represented by a -1
# a clear space is represented by a 0
X = 1
CLEAR = 0
O = -1

# list of lists to represent a tic tac toe board
board  = [[CLEAR,CLEAR,CLEAR],[CLEAR,CLEAR,CLEAR],[CLEAR,CLEAR,CLEAR]]
# so the way to index the middle space would be board[1][1]


#TODO implement printBoard
# write a function that will take the board variable as a parameter
# and print it out in a pretty form for the user to see
# I think for loops would probably be your best option, don't
# forget to print out line breaks in between rows
def printBoard(board):
    pass

#TODO implement take player move
# this function should ask the player which space they want to go in, and which letter they 
# want to put there. It will ask which row they want to go in, then ask which column, then
# ask which letter. So if the player says row 2, column 3, X, you would type:
# board[1][2]=X (remember X is 1)
def takePlayerMove(board):
    pass

#TODO implement checkWin
# write a function that will check if either player has won, and will return
# a 1 (X) if X's win, a -1(O) if 0's win, and a 0(CLEAR)
# Hint: if board[0][0] == X and  board[0][1] == X and board[0][2] == X, then that would count as a win for x
# There's gotta be a way to use for loops to check every possibility faster than typing every possible win out,
# right?
def checkWin(board):
    pass

