from board import Board
from player import Player
from piece import Piece

class Game():
    def __init__(self):
        self.board = Board()
    
    def start_game(self):
        current_player = self.board.player1
        print (current_player)
        current_player.change_turn(self.board.player2)
        current_player = self.board.player2
        print (current_player)