from game import Game

def main():
    print('Welcome to Chess! May the best player win!')
    print("--------------------")
    game = Game()
    game.start_game()
    print("--------------------")

    while True:
        # Display current player
        print(f"Current player: {game.board.current_player}")
        
        # Get move from player
        move = input("Enter your move (e.g., 'e2 e4') or 'quit' to end the game: ")
        
        if move.lower() == 'quit':
            print("Thanks for playing!")
            break
        
        # Parse the move
        try:
            from_pos, to_pos = move.split()
        except ValueError:
            print("Invalid input. Please enter two positions separated by a space.")
            continue
        
        # Make the move
        if game.make_move(from_pos, to_pos):
            print("--------------------")
        else:
            print("Invalid move. Please try again.")
        
"""
        # Check for game end conditions
        if game.is_checkmate():
            print(f"Checkmate! {game.board.current_player} wins!")
            break
        elif game.is_stalemate():
            print("Stalemate! The game is a draw.")
            break
"""

if __name__ == '__main__':
    main()