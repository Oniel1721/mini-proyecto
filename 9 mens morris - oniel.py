# def create_board():
#   return ['*--*--*',
#           '|*-*-*|',
#           '||***||',
#           '*** ***',
#           '||***||',
#           '|*-*-*|',
#           '*--*--*']

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
  if turno == 1:
    return "☺",2
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
    print('+En ambos')
    if board[fil][col-move] != '*' and board[fil][col+move] != '*':
      print('!en ambos')
      return False
  if col+move > 6:
    print ('+en solo izquierda')
    if board[fil][col-move] != '*':
      print ('!en solo izquierda')
      return False
  if col-move < 0:
    print ('+en solo derecha')
    if board[fil][col+move] != '*':
      print ('!en solo derecha')
      return False
  return True

def ficha_move(board,turno,fil,col):
  tipo,turno = tipo_ficha(turno)
  print('ficha_move')
  if board [fil][col] == tipo:
    return True
  return False


def dezlice(board,turno):
  fil,col = seleccionar(board,turno)
  if hor_ver_moves(board,fil,col) or hor_ver_moves(board,col,fil):
    if ficha_move(board,turno,fil,col):
      board[fil][col] = 'X'
    else:
      print('Esa ficha no te pertenece')
  else:
    print('No tiene movimientos')
    return dezlice(board,turno)
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
