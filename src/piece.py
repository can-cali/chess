class Piece:
    def __init__(self, color, type, position):
        self.color = color
        self.type = type
        self.position = position
        self.is_alive = True

    def __str__(self):
        # child entities will override to print their symbol to the chessboard
        pass

    def is_valid_move(self, new_position, board):
        # This method should be overridden by child classes
        return False

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Pawn", position)
    
    def is_valid_move(self, new_position, board):
        # Pawns can move one step forward
        direction = 1 if self.color == "black" else -1

        # Special move for the first move
        if (self.position[0] == 1 and new_position[0] == 3 and new_position[1] == self.position[1] and board[2][self.position[1]] is None
        or self.position[0] == 6 and new_position[0] == 4 and new_position[1] == self.position[1] and board[5][self.position[1]] is None):
            return True
        
        # Normal move
        if new_position[1] == self.position[1] and new_position[0] == self.position[0] + direction:
            return board[new_position[0]][new_position[1]] is None

        # Capture move
        if abs(new_position[1] - self.position[1]) == 1 and new_position[0] == self.position[0] + direction:
            target_piece = board[new_position[0]][new_position[1]]
            return target_piece is not None and target_piece.color != self.color

        return False
    
    def __str__(self):
        return "Pw"
    
class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Rook", position)
    
    def is_valid_move(self, new_position, board):
        # Rooks can move horizontally or vertically
        if new_position[1] == self.position[1] or new_position[0] == self.position[0]:
            # Check if there is a piece in the path
            if new_position[1] == self.position[1]:
                start = min(new_position[0], self.position[0])
                end = max(new_position[0], self.position[0])
                for i in range(start + 1, end):
                    if board[i][new_position[1]] is not None:
                        return False
            else:
                start = min(new_position[1], self.position[1])
                end = max(new_position[1], self.position[1])
                for i in range(start + 1, end):
                    if board[new_position[0]][i] is not None:
                        return False
            if new_position[0] == self.position[0]:
                start = min(new_position[1], self.position[1])
                end = max(new_position[1], self.position[1])
                for i in range(start + 1, end):
                    if board[new_position[0]][i] is not None:
                        return False
                    
            # Check if there is a piece in the target position
            target_piece = board[new_position[0]][new_position[1]]
            if target_piece is not None: # If there is a piece in the target position
                return target_piece.color != self.color # Capture move
            return board[new_position[0]][new_position[1]] is None
        return False
    
    def __str__(self):
        return("Ro")

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Knight", position)
    
    def __str__(self):
        return("Kn")

    def is_valid_move(self, new_position, board):
        # Knights can move in an L shape
        if abs(new_position[0] - self.position[0]) == 2 and abs(new_position[1] - self.position[1]) == 1:
            # Check if new position is not filled with a piece of the same color
            target_piece = board[new_position[0]][new_position[1]]
            if target_piece is not None:
                return target_piece.color != self.color
            return True
        if abs(new_position[0] - self.position[0]) == 1 and abs(new_position[1] - self.position[1]) == 2:
            # Check if new position is not filled with a piece of the same color
            target_piece = board[new_position[0]][new_position[1]]
            if target_piece is not None:
                return target_piece.color != self.color
            return True
        return False
        

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Bishop", position)
    
    def __str__(self):
        return("Bi")
    
    def is_valid_move(self, new_position, board):
        # Bishops can move diagonally
        if abs(new_position[0] - self.position[0]) == abs(new_position[1] - self.position[1]):
            # Check if there is a piece in the path
            if new_position[0] > self.position[0] and new_position[1] > self.position[1]:
                for i in range(1, new_position[0] - self.position[0]):
                    if board[self.position[0] + i][self.position[1] + i] is not None:
                        return False
            elif new_position[0] > self.position[0] and new_position[1] < self.position[1]:
                for i in range(1, new_position[0] - self.position[0]):
                    if board[self.position[0] + i][self.position[1] - i] is not None:
                        return False
            elif new_position[0] < self.position[0] and new_position[1] > self.position[1]:
                for i in range(1, self.position[0] - new_position[0]):
                    if board[self.position[0] - i][self.position[1] + i] is not None:
                        return False
            else:
                for i in range(1, self.position[0] - new_position[0]):
                    if board[self.position[0] - i][self.position[1] - i] is not None:
                        return False
            # Check if new position is not filled with a piece of the same color
            # Capture move
            target_piece = board[new_position[0]][new_position[1]]
            if target_piece is not None:
                return target_piece.color != self.color
            return True

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Queen", position)
    
    def __str__(self):
        return("Qu")
    
    def is_valid_move(self, new_position, board):
        # Queens can move horizontally or vertically
        if new_position[1] == self.position[1] or new_position[0] == self.position[0]:
            # Check if there is a piece in the path
            if new_position[1] == self.position[1]:
                start = min(new_position[0], self.position[0])
                end = max(new_position[0], self.position[0])
                for i in range(start + 1, end):
                    if board[i][new_position[1]] is not None:
                        return False
            else:
                start = min(new_position[1], self.position[1])
                end = max(new_position[1], self.position[1])
                for i in range(start + 1, end):
                    if board[new_position[0]][i] is not None:
                        return False
            if new_position[0] == self.position[0]:
                start = min(new_position[1], self.position[1])
                end = max(new_position[1], self.position[1])
                for i in range(start + 1, end):
                    if board[new_position[0]][i] is not None:
                        return False
                    
            # Check if there is a piece in the target position
            target_piece = board[new_position[0]][new_position[1]]
            if target_piece is not None: # If there is a piece in the target position
                return target_piece.color != self.color # Capture move
            return board[new_position[0]][new_position[1]] is None

        # Queens can move diagonally
        if abs(new_position[0] - self.position[0]) == abs(new_position[1] - self.position[1]):
            # Check if there is a piece in the path
            if new_position[0] > self.position[0] and new_position[1] > self.position[1]:
                for i in range(1, new_position[0] - self.position[0]):
                    if board[self.position[0] + i][self.position[1] + i] is not None:
                        return False
            elif new_position[0] > self.position[0] and new_position[1] < self.position[1]:
                for i in range(1, new_position[0] - self.position[0]):
                    if board[self.position[0] + i][self.position[1] - i] is not None:
                        return False
            elif new_position[0] < self.position[0] and new_position[1] > self.position[1]:
                for i in range(1, self.position[0] - new_position[0]):
                    if board[self.position[0] - i][self.position[1] + i] is not None:
                        return False
            else:
                for i in range(1, self.position[0] - new_position[0]):
                    if board[self.position[0] - i][self.position[1] - i] is not None:
                        return False
            # Check if new position is not filled with a piece of the same color
            # Capture move
            target_piece = board[new_position[0]][new_position[1]]
            if target_piece is not None:
                return target_piece.color != self.color
            return True
        return False

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, "King", position)
    
    def __str__(self):
        return("Ki")
    
    def is_valid_move(self, new_position, board):
        # Calculate the difference in position
        dx = abs(new_position[0] - self.position[0])
        dy = abs(new_position[1] - self.position[1])

        # Kings can move one step in any direction (horizontally, vertically, or diagonally)
        if dx <= 1 and dy <= 1:
            # Check if the target position is empty or contains an opponent's piece
            target_piece = board[new_position[0]][new_position[1]]
            if target_piece is None or target_piece.color != self.color:
                return True

        return False