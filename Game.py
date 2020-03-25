import Player

P = {
  "1": Player.Player('Oniel','☺'),
  "2": Player.Player('Odabel','☻')
}


def create_board():
  return [['*','-','-','*','-','-','*'],
          ['|','*','-','*','-','*','|'],
          ['|','|','*','*','*','|','|'],
          ['*','*','*',' ','*','*','*'],
          ['|','|','*','*','*','|','|'],
          ['|','*','-','*','-','*','|'],
          ['*','-','-','*','-','-','*']]

def print_board(board):
  try:
    for x in board:
      print (x)
  except:
    print(board)

def steps_for_delete(board,mark,t,e):
  print_board(board)
  delete = False
  while delete == False:
    print('To delete:')
    row,column = P[t].select()
    if P[t].is_not_my_token(board,row,column):
      if all_mill(board,mark,P[e].token):
        if P[t].is_enemy_token(board,row,column):
          board = P[e].delete_a_token(board,row,column)
          P[e].tokens_in_board -= 1
          mark = delete_mill(board,mark)
          delete = True
          break
        elif token_in_mill(row,column,mark):
          print('You cannot delete a token in mill')
          continue
      elif P[t].is_enemy_token(board,row,column):
        board = P[e].delete_a_token(board,row,column)
        P[e].tokens_in_board -= 1
        mark = delete_mill(board,mark)
        delete = True
        break
      print("That's no an enemy token.")
  return board,mark

def all_mill(board,mark,token):
  for row in range(0,7):
    for column in range(0,7):
      if board[row][column] == token:
        if not token_in_mill(row,column,mark):
          return False
  return True


def delete_mill(board,mark):
  for x in mark:
    if board[x[0]][x[1]] == '☺' and board[x[2]][x[3]] == '☺' and board[x[4]][x[5]] == '☺':
      continue
    elif board[x[0]][x[1]] == '☻' and board[x[2]][x[3]] == '☻' and board[x[4]][x[5]] == '☻':
      continue
    else:
      mark.remove(x)
  return mark  

def token_in_mill(row,column,mark):
  for x in mark:
    for i in range(0,5,2):
      if row == x[i] and column == x[i+1]:
        return True
  return False

def lose_per_tokens():
  for i in range(1,3):
    if P[str(i)].tokens_in_board < 3 and P[str(i)].mens == 0:
      return P[str(i)].name
  return ""

def no_moves(board):
  loser = [True,True]
  for i in range(1,3):
    test = []
    for row in range(0,7):
      for column in range(0,7):
        if board[row][column] == P[str(i)].token:
          allowx=P[str(i)].horizontal_moves(board,row,column)
          allowy=P[str(i)].vertical_moves(board,row,column)
          if allowx == False and allowy == False:
            test.append(False)
          else:
            test.append(True)
    for x in test:
      if x == True:
        loser[i-1] = False
    else:
      loser[i-1] = False

  return loser


def win(board):
  loser = lose_per_tokens()
  if loser:
    return loser
  loser = no_moves(board)
  if loser[0]:
    return P["1"].name
  if loser[1]:
    return P["2"].name
  return False


def game_loop():
  board = create_board()
  turno = 1
  mark = []
  game_over = False
  while game_over == False:
    if turno == 1:
      turno = 2
      t = "1"
      e = "2"
    else:
      turno = 1 
      t = "2"
      e = "1"
    print('Turno: ' + P[t].numbers_of_tokens())
    print_board(board)
    if P[t].mens > 0:
      game_over = win(board)
      print(game_over)
      print(P["1"].tokens_in_board,P["2"].tokens_in_board)
      if game_over:
        break
      board = P[t].drip(board)
      mill,mark = P[t].is_mill(board,mark)
      if mill:
        board,mark = steps_for_delete(board,mark,t,e)
      continue
    if P[t].mens == 0:
      game_over = win(board)
      print(game_over)
      print(P["1"].tokens_in_board,P["2"].tokens_in_board)
      if game_over:
        break
      board = P[t].slide(board)
      mark = delete_mill(board,mark)
      mill,mark = P[t].is_mill(board,mark)
      if mill:    
        board,mark = steps_for_delete(board,mark,t,e)
  print(game_over)
  print(P["1"].tokens_in_board,P["2"].tokens_in_board)
  if game_over == P["1"].name:
    print("Congratulations "+P["2"].name)
  if game_over == P["2"].name:
    print("Congratulations "+ (P["1"].name))
