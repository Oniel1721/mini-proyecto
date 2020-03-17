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
  

def not_valid(board,fil,col):
  return fil + col > 12 or board[fil][col] != "*"

def seleccionar():
  fil = int(input("Indique fila: "))
  col = int(input("Indique columna: "))
  return fil,col

def tipo_ficha(turno):
  if turno == 1: return "☺",2
  return "☻",1

def goteo(board,turno,white,black):
  print('Para colocar:')
  fil,col = seleccionar()
  if not_valid(board,fil,col):
    print('Ups la coordenada es incorrecta.')
    print('Intentalo de nuevo.')
    return goteo(board,turno,white,black)
  ficha,turno = tipo_ficha(turno)
  board [fil][col] = ficha
  if ficha == '☺' and len(white) > 0:
    white.pop()
  if ficha == '☻' and len(black) > 0:         black.pop()
  return board,turno,white,black


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


def dezlice(board,turno,prot):
  print('Para Seleccionar:')
  fil,col = seleccionar()
  allow_x,direccion_x = horizontal_moves(board,fil,col)
  allow_y,direccion_y = vertical_moves(board,fil,col)
  print('x / y')
  print(direccion_x,direccion_y)
  print(allow_x,allow_y)
  if allow_x or allow_y:
    if ficha_move(board,turno,fil,col):
      board[fil][col] = 'X'
      print_board(board)
      board,prot = moves(board,turno,fil,col,direccion_x,direccion_y,prot)
      print('movio exitosamente')
    else:
      print('Esa no es tu ficha.')
      return dezlice(board,turno,prot)
  else:
    print('No tiene movimientos')
    return dezlice(board,turno,prot)
  if turno == 1: turno = 2
  else: turno = 1
  print('retorno dezlice')
  return board,turno,prot

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

# def todo_molino(board,ficha):
#   # if ficha == '☺': ficha = '☻'
#   # else: ficha = '☺'
#   prot = []
#   elim = []
#   mol = True
#   i = 0
#   while mol and i < 7:
#     mol,f,prot = molino(board,prot)
#     print(prot)
#     if f != ficha:
#       elim.append(prot[-1])
#     i += 1
#   for el in elim:
#     prot.remove(el)
#   print("mol/f/prot 2")
#   print(mol,f,prot)
#   for x in prot:    
#     for i in range(0,6,2):
#       board[x[i]][x[i+1]] = 'O'
#   num_f = 0
#   print('all fil')
#   for fil in board:
#     num_f += fil.count(ficha)
#     print(fil)
#   print(num_f)
#   if num_f == 0:
#     return True
#   return False

def eliminar(board,ficha,white,black,prot):
  # if todo_molino(board,ficha):
  #   print('Todas estan en molino')
  #   return board,white,black
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


def win(board,white,black):
  if len(white) <= 2 or len(black) <= 2:
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
  white = ['☺','☺','☺','☺','☺','☺','☺','☺','☺']
  black = ['☻','☻','☻','☻','☻','☻','☻','☻','☻']
  prot = []
  game_over = False
  while game_over == False:
    if turno == 1:
      fase = white
      print('Turno 1 ☺')

    else: 
      fase = black
      print('Turno 2 ☻')

    print('Marcadas')
    print(prot)
    print('')
    print_board(board)
    if len(fase) > 0:
      game_over = win(board,white,black)
      if game_over:
        break
      print('')
      print(white)
      print(black)
      board,turno,white,black = goteo(board,turno,white,black)
      mol,f,prot = molino(board,prot)
      print(mol,f,prot)
      if mol:
        print_board(board)
        if f == '☺':
          print('Elimina ☻')
          board = eliminar(board,'☻',white,black,prot)
        else:
          print('Elimina ☺')
          board = eliminar(board,'☺',white,black,prot)
      continue

    if len(fase) == 0:
      game_over = win(board,white,black)
      if game_over:
        break
      board,turno,prot = dezlice(board,turno,prot)
      mol,f,prot = molino(board,prot)
      if mol:
        print_board(board)
        if f == '☺':
          board = eliminar(board,'☻',white,black,prot)
        else: board = eliminar(board,'☺',white,black,prot)
  print(who_win(board))

game_loop()
print('End Game')

