import random

class Player():
  def __init__(self,name,token):
    self.name = name
    self.token = token
    self.mens = 9
    self.tokens_in_board = 9
  
  def numbers_of_tokens(self):
    return self.name+' '+self.token * self.mens

  def select(self):
    print('Please numbers between 1-7.')
    try:
      row = int(input('Select a Row: '))
      column = int(input('Select a Column: '))
      if row not in range(1,8) or column not in range(1,8):
        return self.select()
    except:
      return self.select()    
    return row-1,column-1
  
  def put_token(self,board,row,column):
    board[row][column] = self.token
    if self.mens > 0:
      self.mens -=1
    return board
  
  def delete_a_token(self,board,row,column):
    board[row][column] = '*'
    return board

  def selelct_direction(self,movements):
    print('Moves allowed ' + movements)
    direction = input('Select direction: ')
    if direction not in movements:
      print (direction + ' its not an allowed move.')
      return self.selelct_direction(movements)
    return direction

  def is_valid(self,board,row,column):
    return board[row][column] == '*'
  
  def steps_allowed(self,position):
    if position < 3:
      return (6-position) - 3
    elif position > 3:
      return position - 3
    else:
      return 1
  
  def horizontal_moves(self,board,row,column):
    move = self.steps_allowed(row)
    if column-move >= 0 and column+move <= 6:
      if board[row][column-move] == '*' and board[row][column+move] == '*':
        return 'lr'
      elif board[row][column-move] == '*':
        return 'l'
      elif board[row][column+move] == '*':
        return 'r'
    if column+move > 6:
      if board[row][column-move] == '*':
        return 'l'
    if column-move < 0:
      if board[row][column+move] == '*':
        return 'r'
    return ''
  
  def vertical_moves(self,board,row,column):
    move = self.steps_allowed(column) 
    if row-move >= 0 and row+move <= 6:
      if board[row-move][column] == '*' and board[row+move][column] == '*':
        return 'ud'
      elif board[row-move][column] == '*':
        return 'u'
      elif board[row+move][column] == '*':
        return 'd'
    if row+move > 6:
      if board[row-move][column] == '*':
        return 'u'
    if row-move < 0:
      if board[row+move][column] == '*':
        return 'd'
    return ''
  
  def is_my_token(self,board,row,column):
    return board[row][column] == self.token

  def is_not_my_token(self,board,row,column):
    return board[row][column] != self.token
  
  def is_enemy_token(self,board,row,column):
    return board[row][column] != self.token and board[row][column] != '|' and board[row][column] != '-' and board[row][column] != '*' and board[row][column] != ' ' 

  
  def confirm_move(self,direction):
    if direction == 'u':
      word = 'up'
    if direction == 'd':
      word = 'down'
    if direction == 'l':
      word = 'left'
    if direction == 'r':
      word = 'right'

    decision=input('This tile can only be moved '+word+', do you agree?(N = No, Any word = Yes)')

    return decision != 'N'

  def just_one_move(self,direction_x,direction_y):
    return len(direction_x + direction_y) == 1

  def auto_move(self,board,row,column,direction,move_x,move_y):
    change = False
    if direction == 'd':
      if self.confirm_move(direction):
          board = self.delete_a_token(board,row,column)
          board = self.put_token(board,row+move_y,column)
          change = True
    elif direction == 'u':
      if self.confirm_move(direction):
          board = self.delete_a_token(board,row,column)
          board = self.put_token(board,row-move_y,column)
          change = True
    elif direction == 'r':
      if self.confirm_move(direction):
        board = self.delete_a_token(board,row,column)
        board = self.put_token(board,row,column+move_x)
        change = True
    elif direction == 'l':
      if self.confirm_move(direction):
        board = self.delete_a_token(board,row,column)
        board = self.put_token(board,row,column-move_x)
        change = True
    
    if change == False:
      return self.slide(board)
    
    return board
  
  def move(self,board,row,column,movements,move_x,move_y):

    selected = self.selelct_direction(movements)

    if selected == 'u':
      board = self.delete_a_token(board,row,column)
      board = self.put_token(board,row-move_y,column)
    elif selected == 'd':
      board = self.delete_a_token(board,row,column)
      board = self.put_token(board,row+move_y,column)
    elif selected == 'r':
      board = self.delete_a_token(board,row,column)
      board = self.put_token(board,row,column+move_x)
    elif selected == 'l':
      board = self.delete_a_token(board,row,column)
      board = self.put_token(board,row,column-move_x)

    return board

  def drip(self,board):
    print('To place:')
    row,column = self.select()
    if self.is_valid(board,row,column):
      self.put_token(board,row,column)
      return board
    print('Select an empty space.')
    return self.drip(board)

  def slide(self,board):
    print('To Select:')
    row,column = self.select()
    if self.is_not_my_token(board,row,column):
      print("that's not your token")
      return self.slide(board)
    direction_x = self.horizontal_moves(board,row,column)
    direction_y = self.vertical_moves(board,row,column)
    move_x = self.steps_allowed(row)
    move_y = self.steps_allowed(column)

    if direction_x or direction_y:
      if self.just_one_move(direction_x,direction_y):
        board = self.auto_move(board,row,column,direction_x+direction_y,move_x,move_y)
      else:
        board = self.move(board,row,column,direction_x+direction_y,move_x,move_y)
    else:
      print('That token has no movements')
      return self.slide(board)
    return board
  
  def is_mill(self,board,mark):

    for row in range(0,7):
      move = self.steps_allowed(row)
      column = row
      i = 1
      if row > 3:
        column = 6-row
      if row == 3:
        column = 0
        i = 2
      for z in range(0,i):
        if board[row][column] == self.token:
          if board[row][column+move] == self.token:
            if board[row][column+(move*2)] == self.token:
              if [row,column,row,column+move,row,column+(move*2)] not in mark:
                mark.append([row,column,row,column+move,row,column+(move*2)])
                return True,mark
        column = 4
                
    for column in range(0,7):
      move = self.steps_allowed(column)
      row = column
      i = 1
      if column > 3:
        row = 6-column
      if column == 3:
        row = 0
        i = 2
      for z in range(0,i):
        if board[row][column] == self.token:
          if board[row+move][column] == self.token:
            if board[row+(move*2)][column] == self.token:
              if [row,column,row+move,column,row+(move*2),column] not in mark:
                mark.append([row,column,row+move,column,row+(move*2),column])
                return True,mark
        row = 4

    return False,mark

class Bot(Player):
  def __init__(self,name,token,difficulty):
    super().__init__(name,token)
    self.difficulty = difficulty

  def selelct_direction(self,movements):
    i = random.randrange(len(movements))
    return movements[i]

  def auto_move(self,board,row,column,direction,move_x,move_y):
    if direction == 'd':
          board = self.delete_a_token(board,row,column)
          board = self.put_token(board,row+move_y,column)
    elif direction == 'u':
          board = self.delete_a_token(board,row,column)
          board = self.put_token(board,row-move_y,column)
    elif direction == 'r':
        board = self.delete_a_token(board,row,column)
        board = self.put_token(board,row,column+move_x)
    elif direction == 'l':
        board = self.delete_a_token(board,row,column)
        board = self.put_token(board,row,column-move_x) 
    return board
  
  def move(self,board,row,column,movements,move_x,move_y):

    selected = self.selelct_direction(movements)

    if selected == 'u':
      board = self.delete_a_token(board,row,column)
      board = self.put_token(board,row-move_y,column)
    elif selected == 'd':
      board = self.delete_a_token(board,row,column)
      board = self.put_token(board,row+move_y,column)
    elif selected == 'r':
      board = self.delete_a_token(board,row,column)
      board = self.put_token(board,row,column+move_x)
    elif selected == 'l':
      board = self.delete_a_token(board,row,column)
      board = self.put_token(board,row,column-move_x)

    return board

  def places_of(self,board,objective):
    ROW = []
    COLUMN = []
    for row in range(0,7):
      for column in range(0,7):
        if board[row][column] == objective:
          ROW.append(row)
          COLUMN.append(column)
    return ROW,COLUMN
  
  def easy(self,board):
    row,column = self.places_of(board,"*")
    i = random.randrange(len(row))
    return row[i],column[i]

  def repetitive(self,start,places,number):
    for i in range(start,7):
      times = places.count(i)
      if times == number:
        return i
    return 100

  def normal(self,board,token,void,number):
    row_empty,column_empty = self.places_of(board,void)
    row_player,column_player = self.places_of(board,token)
    start,i,ready = 0,0,False
    while i != 100:
      i = self.repetitive(start,row_player,number)
      if i in row_empty:
        i = row_empty.index(i)
        ready = True
        break
      start = i+1
    start,i = 0,0
    while ready == False and i != 100:
      i = self.repetitive(start,column_player,number)
      if i in column_empty:
        i = column_empty.index(i)
        ready = True
        break
      start = i+1
    if ready == False:
      if token == "☺":
        return self.normal(board,"☻","*",number)
      else:
        i = random.randrange(len(row_empty))
    return row_empty[i],column_empty[i]

  def drip(self,board):
    if self.difficulty == "easy":
      row,column = self.easy(board)
    if self.difficulty == "normal":
      row,column = self.normal(board,"☺","*",2)
    if self.difficulty == "hard":
      row,column = self.normal(board,"☺","*",2)
    board = self.put_token(board,row,column)
    return board

  def easy_slide(self,board):
    row,column = self.places_of(board,self.token)
    i = random.randrange(len(row))
    direction_x = self.horizontal_moves(board,row[i],column[i])
    direction_y = self.vertical_moves(board,row[i],column[i])
    move_x = self.steps_allowed(row[i])
    move_y = self.steps_allowed(column[i])

    if direction_x or direction_y:
      if self.just_one_move(direction_x,direction_y):
        board = self.auto_move(board,row[i],column[i],direction_x+direction_y,move_x,move_y)
      else:
        board = self.move(board,row[i],column[i],direction_x+direction_y,move_x,move_y)
    else:
      return self.easy_slide(board)
    return board
  
  def normal_slide(self,board):
    row_empty,column_empty = self.places_of(board,"*")
    row_bot,column_bot = self.places_of(board,"☻")
    pass



  def slide(self,board):
    if self.difficulty == "easy":
      return self.easy_slide(board)
    if self.difficulty == "normal":
      return self.easy_slide(board)
    if self.difficulty == "hard":
      return self.normal_slide(board)

