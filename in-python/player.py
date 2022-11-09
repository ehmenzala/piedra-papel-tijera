class Player:

  def __init__(self, nickname):
    self.nickname = nickname
    self.points = 0
  
  def add_point(self):
    self.points += 1
