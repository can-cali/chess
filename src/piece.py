class Piece:
    def __init__(self, color, type, position):
        self.color = color
        self.type = type
        self.position = position
        self.is_alive = True

    def __str__(self):
        # child entities will override to print their symbol to the chessboard
        pass

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Rook", position)
    
    def move(self, new_position):
        # Rooks can move horizontally or vertically
        # Check if the new position is in the same row or column
        if new_position[0] == self.position[0] or new_position[1] == self.position[1]:
            # Check if new position is not filled with a piece of the same color
            if self.color == "white":
                if self.board[new_position[0]][new_position[1]] is not None and self.board[new_position[0]][new_position[1]].color == "white":
                    print("Invalid move. You can't kill your own piece.")
                    return False
            else:
                if self.board[new_position[0]][new_position[1]] is not None and self.board[new_position[0]][new_position[1]].color == "black":
                    # If the new position is filled with a piece of the opposite color, kill it
                    self.board[new_position[0]][new_position[1]].is_alive = False
                    print(f"You killed a {self.board[new_position[0]][new_position[1]].color} {self.board[new_position[0]][new_position[1]].type}")

            self.position = new_position

            # Update the board
            self.board[new_position[0]][new_position[1]] = self
            self.board[self.position[0]][self.position[1]] = None
            self.board.redraw()
            
            # Change turn
            self.current_player.change_turn(self.other_player)

            return True
        return False
    
    def __str__(self):
        return("Ro")

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Knight", position)
    
    def __str__(self):
        return("Kn")

    def move(self, new_position):
        # Knights can move in an L shape
        # Check if the new position is in an L shape
        if (abs(new_position[0] - self.position[0]) == 2 and abs(new_position[1] - self.position[1]) == 1) or (abs(new_position[0] - self.position[0]) == 1 and abs(new_position[1] - self.position[1]) == 2):
            # Check if new position is not filled with a piece of the same color
            if self.color == "white":
                if self.board[new_position[0]][new_position[1]] is not None and self.board[new_position[0]][new_position[1]].color == "white":
                    print("Invalid move. You can't kill your own piece.")
                    return False
            else:
                if self.board[new_position[0]][new_position[1]] is not None and self.board[new_position[0]][new_position[1]].color == "black":
                    # If the new position is filled with a piece of the opposite color, kill it
                    self.board[new_position[0]][new_position[1]].is_alive = False
                    print(f"You killed a {self.board[new_position[0]][new_position[1]].color} {self.board[new_position[0]][new_position[1]].type}")

            self.position = new_position

            # Update the board
            self.board[new_position[0]][new_position[1]] = self
            self.board[self.position[0]][self.position[1]] = None
            self.board.redraw()
            
            # Change turn
            self.current_player.change_turn(self.other_player)

            return True
        return False

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Bishop", position)
    
    def __str__(self):
        return("Bi")
    
    def move(self, new_position):
        # Bishop can move diagonally
        # Check if the new position is in the same diagonal
        if abs(new_position[0] - self.position[0]) == abs(new_position[1] - self.position[1]):
            # Check if new position is not filled with a piece of the same color
            if self.color == "white":
                if self.board[new_position[0]][new_position[1]] is not None and self.board[new_position[0]][new_position[1]].color == "white":
                    print("Invalid move. You can't kill your own piece.")
                    return False
            else:
                if self.board[new_position[0]][new_position[1]] is not None and self.board[new_position[0]][new_position[1]].color == "black":
                    # If the new position is filled with a piece of the opposite color, kill it
                    self.board[new_position[0]][new_position[1]].is_alive = False
                    print(f"You killed a {self.board[new_position[0]][new_position[1]].color} {self.board[new_position[0]][new_position[1]].type}")

            self.position = new_position

            # Update the board
            self.board[new_position[0]][new_position[1]] = self
            self.board[self.position[0]][self.position[1]] = None
            self.board.redraw()
            
            # Change turn
            self.current_player.change_turn(self.other_player)

            return True
        return False

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Queen", position)
    
    def __str__(self):
        return("Qu")
    
    def move(self, new_position):
        # Queens can move horizontally, vertically or diagonally
        # Check if the new position is in the same row, column or diagonal
        if abs(new_position[0] - self.position[0]) == abs(new_position[1] - self.position[1]) or new_position[0] == self.position[0] or new_position[1] == self.position[1]:
            # Check if new position is not filled with a piece of the same color
            if self.color == "white":
                if self.board[new_position[0]][new_position[1]] is not None and self.board[new_position[0]][new_position[1]].color == "white":
                    print("Invalid move. You can't kill your own piece.")
                    return False
            else:
                if self.board[new_position[0]][new_position[1]] is not None and self.board[new_position[0]][new_position[1]].color == "black":
                    # If the new position is filled with a piece of the opposite color, kill it
                    self.board[new_position[0]][new_position[1]].is_alive = False
                    print(f"You killed a {self.board[new_position[0]][new_position[1]].color} {self.board[new_position[0]][new_position[1]].type}")

            self.position = new_position

            # Update the board
            self.board[new_position[0]][new_position[1]] = self
            self.board[self.position[0]][self.position[1]] = None
            self.board.redraw()
            
            # Change turn
            self.current_player.change_turn(self.other_player)

            return True
        return False

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, "King", position)
    
    def __str__(self):
        return("Ki")
    
    def move(self, new_position):
        # Kings can move horizontally, vertically or diagonally
        # Check if the new position is in the same row, column or diagonal
        if abs(new_position[0] - self.position[0]) == abs(new_position[1] - self.position[1]) or new_position[0] == self.position[0] or new_position[1] == self.position[1]:
            # Check if new position is not filled with a piece of the same color
            if self.color == "white":
                if self.board[new_position[0]][new_position[1]] is not None and self.board[new_position[0]][new_position[1]].color == "white":
                    print("Invalid move. You can't kill your own piece.")
                    return False
            else:
                if self.board[new_position[0]][new_position[1]] is not None and self.board[new_position[0]][new_position[1]].color == "black":
                    # If the new position is filled with a piece of the opposite color, kill it
                    self.board[new_position[0]][new_position[1]].is_alive = False
                    print(f"You killed a {self.board[new_position[0]][new_position[1]].color} {self.board[new_position[0]][new_position[1]].type}")

            self.position = new_position

            # Update the board
            self.board[new_position[0]][new_position[1]] = self
            self.board[self.position[0]][self.position[1]] = None
            self.board.redraw()
            
            # Change turn
            self.current_player.change_turn(self.other_player)

            return True
        return False
