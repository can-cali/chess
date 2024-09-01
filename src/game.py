from board import Board
from player import Player
from piece import Piece

class Game():
    def __init__(self):
        self.board = Board()
    
    def start_game(self):
        current_player = self.board.player1
        print(current_player)
    
    def make_move(self, position, new_position):
        position = self.convert_notation(position)
        new_position = self.convert_notation(new_position)
        
        current_piece = self.board.board[position[0]][position[1]]
        if current_piece is None:
            print("Invalid move. There is no piece in that position.")
            return False
        
        if current_piece.color != self.board.current_player.get_color():
            print("Invalid move. You can't move the other player's piece.")
            return False
        
        if current_piece.is_valid_move(new_position, self.board.board):
            # Capture logic
            target_piece = self.board.board[new_position[0]][new_position[1]]
            if target_piece is not None:
                target_piece.is_alive = False
                print(f"Captured {target_piece.color} {target_piece.type}")
            
            # Update the board
            self.board.board[new_position[0]][new_position[1]] = current_piece
            self.board.board[position[0]][position[1]] = None
            current_piece.position = new_position
            
            # Switch players
            if self.board.current_player == self.board.player1:
                self.board.current_player = self.board.player2
            else:
                self.board.current_player = self.board.player1
            
            # Change turns
            self.board.player1.change_turn(self.board.player2)
            
            # Redraw the board
            self.board.redraw_board()
            
            return True
        else:
            print("Invalid move for this piece.")
            return False

    def convert_notation(self, notation):
        if len(notation) != 2 or not notation[0].isalpha() or not notation[1].isdigit():
            raise ValueError("Invalid chess notation")
        
        col = ord(notation[0].lower()) - ord('a')
        row = 8 - int(notation[1])
        
        if row < 0 or row > 7 or col < 0 or col > 7:
            raise ValueError("Invalid chess notation")
        
        return (row, col)