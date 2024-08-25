from player import Player
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
    
    def __str__(self):
        return("Ro")

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Knight", position)
    
    def __str__(self):
        return("Kn")

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Bishop", position)
    
    def __str__(self):
        return("Bi")

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, "Queen", position)
    
    def __str__(self):
        return("Qu")

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, "King", position)
    
    def __str__(self):
        return("Ki")
