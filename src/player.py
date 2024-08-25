class Player:
    def __init__(self, color):
        self.color = color
        if color == "white":
            self.turn = True
        else:
            self.turn = False
    
    def get_color(self):
        return self.color

    def change_turn(self, other_player):
        self.turn = not self.turn
        other_player.turn = not other_player.turn

    def make_move(self, board):
        pass

    def __str__(self):
        return f"Current player is: {self.color.capitalize()}"