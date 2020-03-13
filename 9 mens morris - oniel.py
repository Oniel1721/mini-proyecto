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


def horizontal_moves(board,fil,col):
  if fil < 3:
    move = (6-fil) - 3
  elif fil > 3:
    move = fil - 3
  else:
    move = 1

  if col-move >= 0 and col+move <= 6:
    if board[fil][col-move] == '*' and board[fil][col+move] == '*':
      return True,'='
    elif board[fil][col-move] == '*':
      return True,'-'
    elif board[fil][col+move] == '*':
      return True,'+'
  if col+move > 6:
    if board[fil][col-move] == '*':
      return True,'-'
  if col-move < 0:
    if board[fil][col+move] == '*':
      return True,'+'
  return False,'!'

def vertical_moves(board,fil,col):
  if col < 3:
    move = (6-col) - 3
  elif col > 3:
    move = col - 3
  else:
    move = 1
  
  if fil-move >= 0 and fil+move <= 6:
    if board[fil-move][col] == '*' and board[fil+move][col] == '*':
      return True,'='
    elif board[fil-move][col] == '*':
      return True,'-'
    elif board[fil+move][col] == '*':
      return True,'+'
  if fil+move > 6:
    if board[fil-move][col] == '*':
      return True,'-'
  if fil-move < 0:
    if board[fil+move][col] == '*':
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
    if direccion_y == '-':
      board[fil][col] = '*'
      fil -= move_y 
      board[fil][col] = ficha
      finish = True
    
  if direccion_y == '!':
    if direccion_x == '+':
      board[fil][col] = '*'
      col += move_x 
      print(fil,col)
      board[fil][col] = ficha
      finish = True
    if direccion_x == '-':
      board[fil][col] = '*'
      col -= move_x 
      board[fil][col] = ficha
      finish = True

  print('')

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
  return board


def dezlice(board,turno):
  fil,col = seleccionar(board,turno)
  allow_x,direccion_x = horizontal_moves(board,fil,col)
  allow_y,direccion_y = vertical_moves(board,fil,col)
  print('x / y')
  print(direccion_x,direccion_y)
  print(allow_x,allow_y)
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

def molino(board):
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

      if board[fil][col] == f or board[fil][col_2] == f:
        if board[fil][col+move] == f or board[fil][col_2+move] == f:
          if board[fil][col+(move*2)] == f or board[fil][col_2+(move*2)] == f:
            return True,f

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

      if board[fil][col] == f or board[fil_2][col] == f:
        if board[fil+move][col] == f or board[fil_2+move][col] == f:
          if board[fil+(move*2)][col] == f or board[fil_2+(move*2)][col] == f:
            return True,f
  
  return False,'!'

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
        
    if etapa == 2:
      board,turno = dezlice(board,turno)
    mol,f = molino(board)
    if mol:
      if f == '☺':
        print('Hay un molino de ☺')
      else: print('Hay un molino de ☻')

game_loop()
