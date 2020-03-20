import Player

P = {
  "1": Player.Player('Oniel','☺'),
  "2": Player.Player('Fulano','☻')
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



def moves(board,turno,fil,col,direccion_x,direccion_y,prot):

  if fil < 3:
    move_x = (6-fil) - 3
  elif fil > 3:
    move_x = fil - 3
  else:
    move_x = 1

  if col < 3:
    move_y = (6-col) - 3
  elif col > 3:
    move_y = col - 3
  else:
    move_y = 1


  ficha,turno = tipo_ficha(turno)


  finish = False

  if direccion_x == '!':
    if direccion_y == '+':
      board[fil][col] = '*'
      fil += move_y 
      board[fil][col] = ficha
      finish = True
      print('solo')
    if direccion_y == '-':
      board[fil][col] = '*'
      fil -= move_y 
      board[fil][col] = ficha
      finish = True
      print('solo')
    
  if direccion_y == '!':
    if direccion_x == '+':
      board[fil][col] = '*'
      col += move_x 
      print(fil,col)
      board[fil][col] = ficha
      finish = True
      print('solo')
    if direccion_x == '-':
      board[fil][col] = '*'
      col -= move_x 
      board[fil][col] = ficha
      finish = True
      print('solo')

  if finish:
    print('sin while')

  while finish == False:
    if direccion_x == '=' and direccion_y == '=':
      ubi = input('Escribe nueva ubicacion (u)(d)(l)(r)')
      if ubi == 'u':
        board[fil][col] = '*'
        fil -= move_y 
        board[fil][col] = ficha
        finish = True
      elif ubi == 'd':
        board[fil][col] = '*'
        fil += move_y 
        board[fil][col] = ficha
        finish = True
      elif ubi == 'l':
        board[fil][col] = '*'
        col -= move_x 
        board[fil][col] = ficha
        finish = True
      elif ubi == 'r':
        board[fil][col] = '*'
        col += move_x 
        board[fil][col] = ficha
        finish = True
    
    if direccion_x == '=':
      if direccion_y == '-':
        ubi = input('Escribe nueva ubicacion (u)(l)(r)')
        if ubi == 'u':
          board[fil][col] = '*'
          fil -= move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'l':
          board[fil][col] = '*'
          col -= move_x 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'r':
          board[fil][col] = '*'
          col += move_x 
          board[fil][col] = ficha
          finish = True
      if direccion_y == '+':
        ubi = input('Escribe nueva ubicacion (d)(l)(r)')
        if ubi == 'd':
          board[fil][col] = '*'
          fil += move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'l':
          board[fil][col] = '*'
          col -= move_x 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'r':
          board[fil][col] = '*'
          col += move_x 
          board[fil][col] = ficha
          finish = True
      
      if direccion_y == '!':
        ubi = input('Escribe nueva ubicacion (l)(r)')
        if ubi == 'l':
          board[fil][col] = '*'
          col -= move_x 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'r':
          board[fil][col] = '*'
          col += move_x 
          board[fil][col] = ficha
          finish = True

    if direccion_y == '=':
      if direccion_x == '-':
        ubi = input('Escribe nueva ubicacion (u)(d)(l)')
        if ubi == 'u':
          board[fil][col] = '*'
          fil -= move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'd':
          board[fil][col] = '*'
          fil += move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'l':
          board[fil][col] = '*'
          col -= move_x 
          board[fil][col] = ficha
          finish = True

      if direccion_x == '+':
        ubi = input('Escribe nueva ubicacion (u)(d)(r)')
        if ubi == 'u':
          board[fil][col] = '*'
          fil -= move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'd':
          board[fil][col] = '*'
          fil += move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'r':
          board[fil][col] = '*'
          col += move_x 
          board[fil][col] = ficha
          finish = True
      
      if direccion_x == '!':
        ubi = input('Escribe nueva ubicacion (u)(d)')
        if ubi == 'u':
          board[fil][col] = '*'
          fil -= move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'd':
          board[fil][col] = '*'
          fil += move_y 
          board[fil][col] = ficha
          finish = True

    if direccion_x == '+':
      if direccion_y == '+':
        ubi = input('Escribe nueva ubicacion (d)(r)')
        if ubi == 'd':
          board[fil][col] = '*'
          fil += move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'r':
          board[fil][col] = '*'
          col += move_x 
          board[fil][col] = ficha
          finish = True
      if direccion_y == '-':
        ubi = input('Escribe nueva ubicacion (u)(r)')
        if ubi == 'u':
          board[fil][col] = '*'
          fil -= move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'r':
          board[fil][col] = '*'
          col += move_x 
          board[fil][col] = ficha
          finish = True
    
    if direccion_x == '-':
      if direccion_y == '+':
        ubi = input('Escribe nueva ubicacion (d)(l)')
        if ubi == 'd':
          board[fil][col] = '*'
          fil += move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'l':
          board[fil][col] = '*'
          col -= move_x 
          board[fil][col] = ficha
          finish = True
      if direccion_y == '-':
        ubi = input('Escribe nueva ubicacion (u)(l)')
        if ubi == 'u':
          board[fil][col] = '*'
          fil -= move_y 
          board[fil][col] = ficha
          finish = True
        elif ubi == 'l':
          board[fil][col] = '*'
          col -= move_x 
          board[fil][col] = ficha
          finish = True

    if finish == False:
      input('algo anda mal')

  for x in prot:
    if board[x[0]][x[1]] == '☺' and board[x[2]][x[3]] == '☺' and board[x[4]][x[5]] == '☺':
      continue
    elif board[x[0]][x[1]] == '☻' and board[x[2]][x[3]] == '☻' and board[x[4]][x[5]] == '☻':
      continue
    else:
      prot.remove(x)

  print('retorno')
  return board,prot


def molino(board,prot):

  ficha = ['☺','☻']

  for f in ficha:
    for fil in range(0,7):
      if fil < 3:
        move = (6-fil) - 3
        col = fil
        col_2 = col
      elif fil > 3:
        move = fil - 3
        col = 6-fil
        col_2 = col
      else:
        move = 1
        col = 0
        col_2 = 4

      if fil != 3:
        if board[fil][col] == f:
          if board[fil][col+move] == f:
            if board[fil][col+(move*2)] == f:
              if [fil,col,fil,col+move,fil,col+(move*2)] not in prot:
                print('por fil')
                prot.append([fil,col,fil,col+move,fil,col+(move*2)])
                return True,f,prot
      else:
        if board[fil][col_2] == f:
          if board[fil][col_2+move] == f:
            if board[fil][col_2+(move*2)] == f:
              if [fil,col_2,fil,col_2+move,fil,col_2+(move*2)] not in prot:
                print('por fil')
                prot.append([fil,col_2,fil,col_2+move,fil,col_2+(move*2)])
                return True,f,prot
              

    for col in range(0,7):
      if col < 3:
        move = (6-col) - 3
        fil = col
        fil_2 = fil
      elif col > 3:
        move = col - 3
        fil = 6-col
        fil_2 = fil
      else:
        move = 1
        fil = 0
        fil_2 = 4

      if col != 3:
        if board[fil][col] == f:
          if board[fil+move][col] == f:
            if board[fil+(move*2)][col] == f:
              if [fil,col,fil+move,col,fil+(move*2),col] not in prot:
                print('por col')
                prot.append([fil,col,fil+move,col,fil+(move*2),col])
                return True,f,prot
      else:
        if board[fil_2][col] == f:
          if board[fil_2+move][col] == f:
            if board[fil_2+(move*2)][col] == f:
              if [fil_2,col,fil_2+move,col,fil_2+(move*2),col] not in prot:
                print('por col')
                prot.append([fil_2,col,fil_2+move,col,fil_2+(move*2),col])
                return True,f,prot

  return False,'!',prot

def eliminar(board,ficha,white,black,prot):
  print('Para Eliminar:')
  fil,col = seleccionar()
  if board[fil][col] != ficha:
    print('Debes seleccionar ' + ficha)
    return eliminar(board,ficha,white,black,prot)
  for x in prot:
    for i in range(0,5,2):
      print(i)
      if fil == x[i] and col == x[i+1]:
        print('No puedes eliminar un ficha en molino')
        return eliminar(board,ficha,white,black,prot)

  board[fil][col] = '*'
  return board

def two(board,ficha):
  simbolo = 0
  for i in board:
    simbolo += i.count(ficha)
  if simbolo == 2:
    return True
  return False

def no_moves(board,f):
  test = []
  for fil in range(0,7):
    for col in range(0,7):
      if board[fil][col] == f:
        allowx,x=horizontal_moves(board,fil,col)
        allowy,y=vertical_moves(board,fil,col)
        if allowx == False and allowy == False:
          test.append(False)
        else:
          test.append(True)
  for x in test:
    if x == True:
      return False
  return True


def win(board):
  if P["1"].mens <= 2 or P["2"].mens <= 2:
    lose_1_1 = two(board,'☺')
    lose_1_2 = two(board,'☻')

    lose_2_1 = no_moves(board,'☺')
    lose_2_2 = no_moves(board,'☻')
    
    loser_two = lose_1_1 or lose_2_1
    loser_move = lose_1_2 or lose_2_2

    return loser_two or loser_move
  return False

def who_win(board):
  white_two = two(board,'☺')
  black_two = two(board,'☻')

  white_moves = no_moves(board,'☺')
  black_moves = no_moves(board,'☻')

  if white_two or white_moves:
    return 'Felicitaciones ☻!!!'
  if black_two or black_moves:
    return 'Felicitaciones ☺!!!'

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
      if game_over:
        break
      board = P[t].drip(board)
      mill,mark = P[t].is_mill(board,mark)
      if mill:
        print_board(board)
        delete = False
        while delete == False:
          row,column = P[t].select()
          if P[t].is_not_my_token(board,row,column):
            board = P[e].delete_a_token(board,row,column)
            delete = True
            break
          print("That's no an enemy token.")
      continue
    if P[t].mens == 0:
      game_over = win(board)
      if game_over:
        break
      board = P[t].slide(board)
      mill,mark = P[t].is_mill(board,mark)
      if mill:
        print_board(board)
        delete = False
        while delete == False:
          row,column = P[t].select()
          if P[t].is_not_my_token(board,row,column):
            board = P[e].delete_a_token(board,row,column)
            delete = True
            break
          print("That's no an enemy token.")
  print(who_win(board))

game_loop()
print('End Game')

