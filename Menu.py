def vs():
  decision = input("Player vs Bot (1)\nPlayer vs Player (2)")
  if decision == "1" or decision == "2":
    return decision
  print("Please numbers between 1-2.")
  return vs()

def name(Player):
  return input(Player +" Write your name: ")

def difficulty():
  decision = input("Easy (1)\nNormal (2)\nHard (3)")
  if decision in ["1","2","3"]:
    return decision
  print("Please numbers between 1-3.")
  return difficulty()

