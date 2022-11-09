from player import Player
from game import Game

un_player = Player('Teb')
otro_player = Player('Sep')

new_game = Game(un_player, otro_player)
new_game.start()