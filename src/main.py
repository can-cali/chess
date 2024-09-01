from game import Game
def main():
    print('May the best one win!')
    print("--------------------")
    game = Game()
    game.start_game()
    print("--------------------")
    # i dont know how to make game playable by moving the pieces
    game.make_move("a7", "a6")
    print("--------------------")
    game.make_move("a2", "a3")

if __name__ == '__main__':
    main()