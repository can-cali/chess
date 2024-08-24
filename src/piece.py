class Piece:
    def __init__(self, color, type, position):
        self.color = color
        self.type = type
        self.position = position

    def __str__(self):
        return f"This is a {self.color.capitalize()} {self.type.capitalize()} at position {self.position}"
    
    def move(self, new_position):
        self.position = new_position
        print(f"{self.color.capitalize()} {self.type.capitalize()} moved to {self.position}")
    
    def capture(self, piece):
        pass

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, "pawn", position)

    def move(self, new_position):
        super().move(new_position)
        print(f"{self.color.capitalize()} {self.type.capitalize()} moved to {self.position}")
    
    def capture(self, piece):
        pass

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, "rook", position)

    def move(self, new_position):
        super().move(new_position)
        print(f"{self.color.capitalize()} {self.type.capitalize()} moved to {self.position}")
    
    def capture(self, piece):
        pass

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, "knight", position)

    def move(self, new_position):
        super().move(new_position)
        print(f"{self.color.capitalize()} {self.type.capitalize()} moved to {self.position}")
    
    def capture(self, piece):
        pass

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, "bishop", position)

    def move(self, new_position):
        super().move(new_position)
        print(f"{self.color.capitalize()} {self.type.capitalize()} moved to {self.position}")
    
    def capture(self, piece):
        pass

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, "queen", position)

    def move(self, new_position):
        super().move(new_position)
        print(f"{self.color.capitalize()} {self.type.capitalize()} moved to {self.position}")
    
    def capture(self, piece):
        pass

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, "king", position)

    def move(self, new_position):
        super().move(new_position)
        print(f"{self.color.capitalize()} {self.type.capitalize()} moved to {self.position}")
    
    def capture(self, piece):
        pass

