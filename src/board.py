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
            board[1][i] = Pawn("black", (1, i))
            board[6][i] = Pawn("white", (6, i))
        
        # add other pieces
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece_class in enumerate(piece_order):
            board[0][i] = piece_class("black", (0, i))
            board[7][i] = piece_class("white", (7, i))
        
        return board
    
    def __draw_board(self):
        # Print column labels
        print("   a  b  c  d  e  f  g  h")
        print("  ------------------------")

        for i in range(8):
            # Print row number
            print(f"{8-i}|", end=" ")

            for j in range(8):
                if self.board[i][j] is None:
                    print("--", end=" ")
                else:
                    if self.board[i][j].color == "black":
                        print(str(self.board[i][j])[:2].lower(), end=" ")
                    else:
                        print(str(self.board[i][j])[:2].upper(), end=" ")
            
            # Print row number again at the end of the row
            print(f"|{8-i}")

        # Print bottom border and column labels again
        print("  ------------------------")
        print("   a  b  c  d  e  f  g  h")
        
    def get_piece(self, position):
        return self.board[position[0]][position[1]]
    
    def redraw_board(self):
        self.__draw_board()

    def __create_pieces(self):
        pass