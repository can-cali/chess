from board import Board
from piece import Piece
class Player:
    def __init__(self, color):
        self.color = color

    def make_move(self, board):
        pass

    def __str__(self):
        return f"Player is: {self.color.capitalize()}"