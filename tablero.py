class Player():
  def __init__(self,name,token):
    self.name = name
    self.token = token
    self.mens = 9
  
  def numbers_of_tokens(self):
    return self.token * self.mens

  def select(self):
    print('Please numbers between 1-7.')
    try:
      row = int(input('Select a Row: '))
      column = int(input('Select a Column: '))
      if (row < 1 or row > 7) or (column < 1 or column > 7):
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

  def move(self,movements):
    print('Moves allowed ' + movements)
    direction = input('Select direction: ')
    if direction not in movements:
      print (direction + ' its not an allowed move.')
      return self.move(movements)
    return direction

