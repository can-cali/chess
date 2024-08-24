from piece import Piece
class Board:
    def __init__(self, player="white"):
        self.player = player
        self.board = self.__create_board()
        
    def __create_board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(None)
            board.append(row)
        return board
    
    def draw_board(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None:
                    print(self.board[i][j], end=" ")
                else:
                    print("X", end=" ")
            print()

    def __create_pieces(self, board):
        pass