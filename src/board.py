from piece import Pawn, Rook, Knight, Bishop, Queen, King
from player import Player
class Board:
    def __init__(self):
        self.player1 = Player("white")
        self.player2 = Player("black")
        self.current_player = self.player1

        self.board = self.__create_board()
        self.__draw_board()
        
    def __create_board(self):
        # create empty board
        board = [[None for _ in range(8)] for _ in range(8)]

        # add pawns
        for i in range(8):
            board[1][i] = Pawn("white", (1, i))
            board[6][i] = Pawn("black", (6, i))
        
        # add other pieces
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece_class in enumerate(piece_order):
            board[0][i] = piece_class("white", (0, i))
            board[7][i] = piece_class("black", (7, i))
        
        return board
    
    def __draw_board(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is None:
                    print("--", end=" ")
                else:
                    print(str(self.board[i][j])[:2], end=" ")  # Print first two characters of piece string representation
            print()
    
    def get_piece(self, position):
        return self.board[position[0]][position[1]]
    
    def redraw_board(self):
        self.__draw_board()

    def __create_pieces(self):
        pass