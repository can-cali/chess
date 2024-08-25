from typing import Any
from piece import *
from player import Player
from pprint import pprint
class Board:
    def __init__(self):
        self.player1 = Player("white")
        self.player2 = Player("black")
        self.current_player = self.player1

        self.board = self.__create_board()
        self.__create_pieces()
        self.__draw_board()
        
    def __create_board(self):
        # create board
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(None)
            board.append(row)

        # add pawns
        for i in range(8):
            for j in range(8):
                board[1][j] = "Pw"
                board[6][j] = "Pw"
        
        for i in range(8):
            for j in range(8):
                if (i, j) in [(0,0), (0,7), (7,7), (7,0)]:
                    if j != 7:
                        rook = Rook("white", (i, j))
                    else:
                        rook = Rook("black", (i, j))
                    board[i][j] = rook
                if (i, j) in [(1,0), (1,7), (6,7), (6,0)]:
                    if j != 7:
                        knight = Knight("white", (j,i))
                    else:
                        knight = Knight("black", (j,i))
                    board[j][i] = knight
                if (i, j) in [(2,0), (2,7), (5,7), (5,0)]:
                    if j != 7:
                        bishop = Bishop("white", (j,i))
                    else:
                        bishop = Bishop("black", (j,i))
                    board[j][i] = bishop
                if (i, j) in [(3,0), (3,7)]:
                    if j != 7:
                        queen = Queen("white", (j,i))
                    else:
                        queen = Queen("black", (j,i))
                    board[j][i] = queen
                if (i, j) in [(4,0), (4,7)]:
                    if j != 7:
                        king = King("white", (j,i))
                    else:
                        king = King("black", (j,i))
                    board[j][i] = king
        
        return board
    
    def __draw_board(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is None:
                    print("--", end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print()

    def __create_pieces(self):
        pass