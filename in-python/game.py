from scoreboard import Scoreboard

class Game:

  def __init__(self, first_player, second_player):
    self.first_player = first_player
    self.second_player = second_player
    self.scoreboard = Scoreboard()

  def start(self):
    print('\n-------------------')
    print('Bienvenido, escoge una de las opciones')
    print('> [A] Iniciar partida')
    print('> [B] Ver historial de victorias')
    print('> [C] Salir')
    answer = input('\n>>> ')
    if (answer == 'A'):
      self.start_fight()
    elif (answer == 'B'):
      self.watch_scoreboard()
    elif (answer == 'C'):
      exit()

  def start_fight(self):
    while (self.first_player.points <= 2 and self.second_player.points <= 2):

      # Piedra 1 # Papel 2 # Tijera 3
      p1_attack = int(input(f'{self.first_player.nickname}, escoge una jugada:\n>>> Piedra (1)\n>>> Papel (2)\n>>> Tijeras (3)\n>>> '))
      p2_attack = int(input(f'{self.second_player.nickname}, escoge una jugada:\n>>> Piedra (1)\n>>> Papel (2)\n>>> Tijeras (3)\n>>> '))
      print('\n-----\n')

      if p1_attack == p2_attack:
          print(f"Both players selected {p1_attack}. It's a tie!")
      elif p1_attack == 1:
        if p2_attack == 3:
            self.first_player.add_point()
        else:
            self.second_player.add_point()
      elif p1_attack == 2:
        if p2_attack == 1:
            self.first_player.add_point()
        else:
            self.second_player.add_point()
      elif p1_attack == 3:
        if p2_attack == 2:
            self.first_player.add_point()
        else:
            self.second_player.add_point()
    
    self.find_winner()

  def watch_scoreboard(self):
    for d in self.scoreboard.read_JSON():
      print(f'W {d["winner"]} vs {d["looser"]} L')
    self.back_to_menu()

  def find_winner(self):

    if (self.first_player.points > self.second_player.points):
      print(f'Ha ganado {self.first_player.nickname}')
      self.scoreboard.add_registry(
          winner=self.first_player.nickname,
          looser=self.second_player.nickname
        )
    else:
      print(f'Ha ganado {self.second_player.nickname}')
      self.scoreboard.add_registry(
          winner=self.second_player.nickname,
          looser=self.first_player.nickname
        )
    self.start()

  def back_to_menu(self):
    answer = input('\nRegresar al menu principal? (M)\n>>> ')
    if (answer == 'M'):
      self.start()
      
