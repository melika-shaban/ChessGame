# the following list represents a chess board
#P represents a pawn on the black team
#p represents a pawn on the white team
#K represents the king on the black team
#k represents the king on the white team
#H represents the knight (horse) on the black team
#h represents the knight (horse) on the white team
#B represents the bishop on the black team
#b represents the bishop on the white team
#R represents the rook on the black team
#r represents the rook on the white team
#Q represents the queen on the black team
#q represents the queen on the white team
chessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
]


#complete the function called locate_piece(pc): where pc is a character representing a piece on the board
#ie. pc could be any of (ie. R, H, B, Q, K, P, r, h, b, q, k, p)
#the function should return a list of tuples representing all of the locations on the board where that piece can be found
#eg. locate_piece('H') should return [(0, 1), (0, 6)]   ******note the tuples are in the format (row, col), not (col, row)***
#Assume the top left is location (0, 0) and the bottom right is location (7,7)


#this should be inside of your function, otherwise it adds to the existing list every time locate_piece is called (Mr. H)
list = []
def locate_piece(pc):
  
  row_counter = 0
  for rows in chessboard:
    index_counter = 0
    for items in rows:
      if items == pc:
        r = row_counter
        c = index_counter
        list.append((r,c))
      index_counter += 1
    row_counter += 1
  return list

pieceList = ['R', 'H', 'B', 'Q', 'K', 'p']
testList = []
for pc in pieceList:
  testList.append(locate_piece(pc))
print (testList==[[(0, 0), (0, 7)], [(0, 1), (0, 6)], [(0, 2), (0, 5)], [(0, 3)], [(0, 4)], [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)]])

#complete the function read_pawn_puzzle()
#the file "pawn puzzle.txt" represents a chessboard. Read in the contents of the file, convert it to a 2D list in the same format as the chessboard variable above, and assign this 2D list to the chessboard variable. Each line in the file represents a row in the chessboard. The character s represents an empty space. All other characters i nthe .txt file are the same as described at the top of this main.py file

def read_pawn_puzzle():
  with open("puzzles/pawn puzzle.txt", "r") as text:
    chess_pieces = text.readlines()
  lists = [[], [], [], [], [], [], [], []]
  another_list = []
  list_counter = 0
  for rows in chess_pieces:
    index_counter = 0
    for i in range(0,8):
      if rows[index_counter] == "s":
        lists[list_counter].append(' ')
      elif rows[index_counter] == "P":
        lists[list_counter].append("P")
      elif rows[index_counter] == "p":
        lists[list_counter].append("p")
      elif rows[index_counter] == "K":
        lists[list_counter].append("K")
      elif rows[index_counter] == "k":
        lists[list_counter].append("k")
      elif rows[index_counter] == "H":
        lists[list_counter].append("H")
      elif rows[index_counter] == "h":
        lists[list_counter].append("h")
      elif rows[index_counter] == "B":
        lists[list_counter].append("B")
      elif rows[index_counter] == "b":
        lists[list_counter].append("b")
      elif rows[index_counter] == "R":
        lists[list_counter].append("R")
      elif rows[index_counter] == "r":
        lists[list_counter].append("r")
      elif rows[index_counter] == "Q":
        lists[list_counter].append("Q")
      elif rows[index_counter] == "q":
        lists[list_counter].append("q")
      index_counter += 1
    list_counter += 1
  chessboard = lists
  return chessboard

# print(read_pawn_puzzle())
# print(chessboard)


#create a function called move_pawn(startpos, endpos): 
#startpos is a tuple representing the current row and column of the piece you want to move
#endpos is a tuple representing the row and column of the space to move the piece to
#the function should check if the move is valid according to the pawn movement rules

#if the move is valid...
#update chessboard so the character at startpos is relocated to endpos
#at startpos there should be an empty space
#return True

#if the move is invalid, 
#return False and don't update the board

#note, the piece must also be a pawn for the move to be valid
def move_pawn(startpos, endpos):
   # write your code here
  global row_of_startpos, col_of_startpos, endpos_col, endpos_row
  row_of_startpos, col_of_startpos = startpos
  endpos_row, endpos_col = endpos
  def something_in_spot(tuple):
    row, col = tuple
    cat = chessboard[row]
    hampster = cat[col]
    return hampster
  piece  = something_in_spot(startpos)

  def move_piece(startpos, endpos):
    start_piece = something_in_spot(startpos)
    making_startpos_empty = chessboard[row_of_startpos]
    making_startpos_empty[col_of_startpos] = ' '
    moving_to_endpos = chessboard[endpos_row]
    moving_to_endpos[endpos_col] = start_piece
    return chessboard

  
  if something_in_spot(endpos) == ' ':
    if piece == 'P':
      if col_of_startpos == endpos_col and row_of_startpos == endpos_row - 1:
        move_piece(startpos, endpos)
        return True
    if piece == 'p':
      if col_of_startpos == endpos_col and row_of_startpos == endpos_row + 1:
        move_piece(startpos, endpos)
        return True

  if something_in_spot(endpos) == ' ':
    if piece == 'P':
      if row_of_startpos == 1:
        if something_in_spot((row_of_startpos + 1, col_of_startpos)) == ' ':
          if endpos_col == col_of_startpos and row_of_startpos == endpos_row - 2:
            move_piece(startpos, endpos)
            return True
    if piece == 'p':
      if row_of_startpos == 6:
        if something_in_spot((row_of_startpos - 1, col_of_startpos)) == ' ':
          if endpos_col == col_of_startpos and row_of_startpos == endpos_row + 2:
            move_piece(startpos, endpos)
            return True
#for the diagonal check
  if endpos_col == col_of_startpos + 1 or endpos_col == col_of_startpos - 1:
    some = something_in_spot(endpos)
    if piece == 'P':
      if some  == 'p' or some == 'r' or some == 'h' or some == 'b' or some == 'q' or some == 'k':
        if row_of_startpos == endpos_row - 1:
          move_piece(startpos, endpos)
          return True
    if piece == 'p':
      if  some == something_in_spot(endpos) == 'P' or some == 'R' or some == 'H' or some == 'B' or some == 'Q' or some == 'K':
        if row_of_startpos == endpos_row + 1:
          move_piece(startpos, endpos)
          return True
  return False

            
# print(move_pawn((7,0), (1,0)))
# print(chessboard)


#pawn movement rules
# Initial Move: When a pawn makes its very first move, it has the option to move forward one or two squares, not just one. This initial move rule allows pawns to quickly occupy the center of the board. However, they cannot skip over other pieces in their path. It's worth noting that if a pawn does not make a two-square move on its initial move, it loses the opportunity to do so later in the game.

# Regular Move: After the initial move, pawns can only move forward one square at a time. They cannot move backward; their movement is always in the direction of the opponent's side of the board. Pawns also cannot move sideways.

# Capturing: Pawns capture differently from how they move. To capture an opponent's piece, a pawn moves one square diagonally forward. For example, if an opponent's piece is one square diagonally in front of your pawn, you can capture it by moving your pawn to that square. Capturing is the only way pawns can remove opposing pieces.

# Blocking: Pawns cannot move through or jump over other pieces. If a piece is blocking the path of a pawn, that pawn cannot move in that direction. Pawns also cannot capture pieces that are directly in front of them.


#Optional extensions
#create a movement function for any type of piece you wish 
#make sure the movement follows the rules of chess


#leave these tests here

def test1():
  # Enter code here
  global chessboard
  chessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  newchessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]

  if(move_pawn((1,1), (3,1))==True and chessboard==newchessboard):
    print("passed")
  else:
    print("failed")
    
def test2():
  # Enter code here
  global chessboard
  chessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  newchessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  
  if((move_pawn((1,3), (2,3))==True and chessboard==newchessboard)):
    print("passed")
  else:
    print("failed")
    
def test3():
  # Enter code here
  global chessboard
  chessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'p', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', ' ', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  newchessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'p', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', ' ', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  
  if(move_pawn((4,3), (3,3))==False and chessboard==newchessboard):
    print("passed")
  else:
    print("failed")

def test4():
  # Enter code here
  global chessboard
  chessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  newchessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  
  if(move_pawn((2,7), (1,7))==False and chessboard==newchessboard):
    print("passed")
  else:
    print("failed")


def test5():
  # Enter code here
  global chessboard
  chessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', ' ', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  newchessboard = [
    ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'p', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', ' ', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  if(move_pawn((4,2), (3,1))==True and chessboard==newchessboard):
  # note, it is clear that test 5 believes the chessboard was updated, so the condition was changed to True as necessary 
    print("passed")
  else:
    print("failed")


def test6():
  # Enter code here
  global chessboard
  chessboard = [
    ['R', ' ', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'H', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', ' ', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  newchessboard = [
    ['R', ' ', 'B', 'Q', 'K', 'B', 'H', 'R'],
    ['P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'H', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', ' ', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
  ]
  if(move_pawn((2,1), (3,2))==False and chessboard==newchessboard):
    print("passed")
  else:
    print("failed")
  print(chessboard)
    
test1()
test2()
test3()
test4()
test5()
test6()


