#-------- Global Variables --------

#game board
board = ["-", "-", "-", 
         "-", "-", "-",
         "-", "-", "-"]

#if game is still going
game_still_going = True

#who won? Or tie?
winner = None

#whos turn is it
current_player = "X"


         


def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
 
  # Display inital board
  #display_board()
 
  while game_still_going:

    handle_turn(current_player)

    check_if_game_over()

    flip_player()

  # The game has ended
  if winner == "X" or winner == "O":
   print(winner + " won.")
  elif winner == None:
   print("Tie.")


def handle_turn(player):

 print(player + "'s turn.")

 position = input("choose a position from 1-9: ")

 while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
   position = input("invalid input. choose a position from 1-9: ") 

 position = int(position) - 1

 board[position] = player

display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

  global winner
  
  
  row_winner = check_rows()
  
  colomn_winner = check_colomns()
  
  diagonal_winner = check_diagonals()


  if row_winner:
    winner = row_winner
  elif colomn_winner:
    winner = colomn_winner
  elif diagonal_winner:
   winner = diagonal_winner
  return

def check_rows():

 global game_still_going

 row_1 = board[0] == board[1] == board [2] != "-"
 row_2 = board[3] == board[4] == board [5] != "-"
 row_3 = board[6] == board[7] == board [8] != "-"

 if row_1 or row_2 or row_3:
   game_still_going = False

 if row_1:
  return board[0]
 if row_2:
  return board[3]
 if row_3:
  return board[6]
 return

def check_colomns():

 global game_still_going

 colomn_1 = board[0] == board[3] == board [6] != "-"
 colomn_2 = board[1] == board[4] == board [7] != "-"
 colomn_3 = board[2] == board[5] == board [8] != "-"

 if colomn_1 or colomn_2 or colomn_3:
   game_still_going = False

 if colomn_1:
    return board[0]
 if colomn_2:
    return board[1]
 if colomn_3:
    return board[2]
 return

def check_diagonals():

 global game_still_going

 diagonal_1 = board[0] == board[4] == board [8] != "-"
 diagonal_2 = board[6] == board[4] == board [2] != "-"

 if diagonal_1 or diagonal_2:
   game_still_going = False

 if diagonal_1:
    return board[0]
 if diagonal_2:
    return board[6]
 return


def check_if_tie():
 global game_still_going
 if "-" not in board:
   game_still_going = False
 return

def flip_player():

  global current_player

  display_board()

  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
   current_player = "X" 
  return

play_game()
