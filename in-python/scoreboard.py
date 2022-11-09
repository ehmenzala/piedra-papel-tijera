import json

class Scoreboard:

  def __init__(self):
    self.contenidos_json = ''
    pass
  
  def read_JSON(self):
    with open('./data.txt') as data:
      contenidos_string = data.read()
      if (len(contenidos_string) != 0):
        self.contenidos_json = json.loads(contenidos_string)
      else:
        print('Aún no hay un historial de victorias')

    return self.contenidos_json      
  
  def add_registry(self, winner, looser):
    current_registry = {
      'winner': winner,
      'looser': looser
    }
    history = self.read_JSON()
    history.append(current_registry)

    with open('./data.txt', 'w') as data:
      data.write(json.dumps(history))