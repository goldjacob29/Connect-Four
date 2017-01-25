import numpy
import sys

board = numpy.chararray((6,7))
board[:] = "_"
spacesLeft = 30

boardState = [5,5,5,5,5,5,5]

isWin = False
is1Turn = True
piece = ''

def makeMove():
	col = int(raw_input("Enter a column 0-6: "))
	while boardState[col] == -1:
		print "Invalid: column", col, "is full."
		col = int(raw_input("Choose another: "))
	else:
		row = boardState[col]
		board[row,col] = piece
		boardState[col]-=1
	print boardState
	print board
	return (row,col)

def checkWin(a):
	print "I am checkWin"

while True:
	piece = 'Y' if is1Turn else 'R'
	print board
	print "P1," if is1Turn else "P2,", "Make your move."
	play = makeMove()
	isWin = checkWin(play)
	if isWin:
		print "P1" if is1Turn else "P2", "is the winner!"
		break
	print "spaces remaining = ", spacesLeft
	spacesLeft-=1
	if spacesLeft == 0:
		print "It's a draw!"
		break
	is1Turn = not is1Turn

