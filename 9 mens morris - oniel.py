def create_board():
  return [['*','-','-','*','-','-','*'],
          ['|','*','-','*','-','*','|'],
          ['|','|','*','*','*','|','|'],
          ['*','*','*',' ','*','*','*'],
          ['|','|','*','*','*','|','|'],
          ['|','*','-','*','-','*','|'],
          ['*','-','-','*','-','-','*']]

def print_board(board):
  for x in board:
    print (x)
    
def fichas(board):
  num_white = 0
  num_black = 0
  for i in board:
    num_black += i.count("☻")
    num_white += i.count("☺")
  num_white = 3 - num_white
  num_black = 3 - num_black
  if num_black + num_white == 0:
    return False
  return [(str(num_white)+" "+"☺" * num_white),(str(num_black)+" "+"☻" * num_black)]
  

def not_valid(board,fil,col):
  return fil + col > 12 or board[fil][col] != "*"

def seleccionar(board,turno):
  fil = int(input("Indique fila: "))
  col = int(input("Indique columna: "))
  return fil,col

def tipo_ficha(turno):
  if turno == 1: return "☺",2
  return "☻",1

def goteo(board,turno):
  fil,col = seleccionar(board,turno)
  if not_valid(board,fil,col):
    print('Ups la coordenada es incorrecta.')
    print('Intentalo de nuevo.')
    return goteo(board,turno)
  ficha,turno = tipo_ficha(turno)
  board [fil][col] = ficha
  return board,turno


def hor_ver_moves(board,fil,col):
  if fil < 3:
    move = (6-fil) - 3
  elif fil > 3:
    move = fil - 3
  else:
    move = 1
  if col-move >= 0 and col+move <= 6:
    if board[fil][col-move] == '*' and board[fil][col+move] == '*':
      return True,'='
  if col+move > 6:
    if board[fil][col-move] == '*':
      return True,'-'
  if col-move < 0:
    if board[fil][col+move] == '*':
      return True,'+'
  return False,'!'

def ficha_move(board,turno,fil,col):
  tipo,turno = tipo_ficha(turno)
  print('ficha_move')
  if board [fil][col] == tipo:
    return True
  return False

def moves(board,turno,fil,col,direccion_x,direccion_y):
  if fil < 3:
    move = (6-fil) - 3
  elif fil > 3:
    move = fil - 3
  else:
    move = 1
  ficha,turno = tipo_ficha(turno)

  if direccion_x == '!':
    if direccion_y == '>':
      board[fil][col] = '*'
      col += move 
      board[fil][col] = ficha
      return board
    if direccion_y == '<':
      board[fil][col] = '*'
      col -= move 
      board[fil][col] = ficha
      return board
  
  if direccion_y == '!':
    if direccion_x == '>':
      board[fil][col] = '*'
      fil += move 
      board[fil][col] = ficha
      return board
    if direccion_x == '<':
      board[fil][col] = '*'
      fil -= move 
      board[fil][col] = ficha
      return board

  if direccion_x == '=' and direccion_y == '=':
    ubi = input('Escribe nueva ubicacion (u)(d)(l)(r)')
    if ubi == 'u':
      board[fil][col] = '*'
      col -= move 
      board[fil][col] = ficha
      return board
    elif ubi == 'd':
      board[fil][col] = '*'
      col += move 
      board[fil][col] = ficha
      return board
    elif ubi == 'l':
      board[fil][col] = '*'
      fil -= move 
      board[fil][col] = ficha
      return board
    elif ubi == 'r':
      board[fil][col] = '*'
      fil += move 
      board[fil][col] = ficha
      return board
    else: return moves(board,turno,fil,col,direccion_x,direccion_y)
  
  if direccion_x == '=':
    if direccion_y == '<':
      ubi = input('Escribe nueva ubicacion (u)(l)(r)')
      if ubi == 'u':
        board[fil][col] = '*'
        col -= move 
        board[fil][col] = ficha
        return board
      elif ubi == 'l':
        board[fil][col] = '*'
        fil -= move 
        board[fil][col] = ficha
        return board
      elif ubi == 'r':
        board[fil][col] = '*'
        fil += move 
        board[fil][col] = ficha
        return board
      else: return moves(board,turno,fil,col,direccion_x,direccion_y)
    if direccion_y == '>':
      ubi = input('Escribe nueva ubicacion (d)(l)(r)')
      if ubi == 'd':
        board[fil][col] = '*'
        col += move 
        board[fil][col] = ficha
        return board
      elif ubi == 'l':
        board[fil][col] = '*'
        fil -= move 
        board[fil][col] = ficha
        return board
      elif ubi == 'r':
        board[fil][col] = '*'
        fil += move 
        board[fil][col] = ficha
        return board
      else: return moves(board,turno,fil,col,direccion_x,direccion_y)

  if direccion_y == '=':
    if direccion_x == '<':
      ubi = input('Escribe nueva ubicacion (u)(d)(l)')
      if ubi == 'u':
        board[fil][col] = '*'
        col -= move 
        board[fil][col] = ficha
        return board
      elif ubi == 'd':
        board[fil][col] = '*'
        col += move 
        board[fil][col] = ficha
        return board
      elif ubi == 'l':
        board[fil][col] = '*'
        fil -= move 
        board[fil][col] = ficha
        return board
      else: return moves(board,turno,fil,col,direccion_x,direccion_y)

    if direccion_x == '>':
      ubi = input('Escribe nueva ubicacion (u)(d)(r)')
      if ubi == 'u':
        board[fil][col] = '*'
        col -= move 
        board[fil][col] = ficha
        return board
      elif ubi == 'd':
        board[fil][col] = '*'
        col += move 
        board[fil][col] = ficha
        return board
      elif ubi == 'r':
        board[fil][col] = '*'
        fil += move 
        board[fil][col] = ficha
        return board
      else: return moves(board,turno,fil,col,direccion_x,direccion_y)


def dezlice(board,turno):
  fil,col = seleccionar(board,turno)
  allow_x,direccion_x = hor_ver_moves(board,fil,col)
  allow_y,direccion_y = hor_ver_moves(board,col,fil)
  if allow_x or allow_y:
    if ficha_move(board,turno,fil,col):
      board[fil][col] = 'X'
      print_board(board)
      board = moves(board,turno,fil,col,direccion_x,direccion_y)
    else:
      print('Esa no es tu ficha.')
      return dezlice(board,turno)
  else:
    print('No tiene movimientos')
    return dezlice(board,turno)
  if turno == 1: turno = 2
  else: turno = 1
  return board,turno

def game_loop():
  board = create_board()
  turno = 1
  etapa = 1
  while turno == 1 or turno == 2:
    print_board(board)
    if etapa == 1:
      print (fichas(board))
      board,turno = goteo(board,turno)
      if fichas(board) == False:
        etapa = 2
      continue
    board,turno = dezlice(board,turno)

game_loop()
