##############################################################
##################### CHECKERS GAME ##########################
##############################################################

# GENERAL RULES #
https://en.wikipedia.org/wiki/Draughts

# IMPLEMENTED CHECKERS RULES #
- Pieces can capture only *forward*.
- Pieces move one square at a time.
- Kings move like regular pieces but can also capture *backwards*.
- Capturing is not mandatory.
- The white player starts the game.
- The player who captures all the opponent's pieces wins.

# HOW TO PLAY #
- Use the left mouse button to select the game mode.
- Use the ESCAPE key or close the window to exit the game.
- If you’re in-game, you can return to the menu by pressing ESCAPE,
  but you’ll lose your progress.
- To move a piece, click it with the left mouse button,
  then click the square where you want to move it.

# HOW TO RUN THE GAME #
To run the game, you need to have Python installed along with the pygame library.

# COMMAND #
python main.py

# Program inspired by Tim Ruscica’s project #
https://www.youtube.com/watch?v=vnd3RfeG3NM
##############################################################

==============
| DOCUMENTATION |
==============

1) main.py:
- main_menu():
    Creates a menu with two buttons to choose the game mode:
    a) [player vs player]
    b) [player vs computer]

- game_vs_player():
    Starts the checkers game in [player vs player] mode.

- game_vs_computer():
    Starts the checkers game in [player vs computer] mode.

- position_from_mouse():
    Gets the position from MOUSEBUTTONDOWN -> pygame.mouse.get_pos()
    and calculates the corresponding board square.

==========  
/assets/ | contains all images, music, etc., used in the program.
==========

==========
/checkers/
==========

2) __init__.py:
    Initializes the `checkers` folder as a package/module, 
    allowing things to be imported directly from it.

3) constants.py:
    Stores constant variables.

4) board.py:
    - Class Board:
        Represents the game board.

        - __init__():
            Initializes the board data and calls the init_board() method.

        - init_board():
            Initializes a 2D array representing the board with either
            Piece objects or 0 for empty squares.

        - draw_board():
            Draws the board and the pieces on the appropriate squares
            using draw_piece() from the Piece class.

        - move():
            Executes a move by swapping array values.
            Also calls move_piece() from the Piece class and, if a piece
            reaches the last row, calls make_king() to promote it.

        - get_square():
            Returns the content (piece or empty) of a specific square.

        - get_valid_moves():
            Calculates the valid moves for a given piece by checking diagonals,
            using recursive methods diagonal_traverse_left() and diagonal_traverse_right().

        - diagonal_traverse_left():
            Recursively checks diagonals up-left and down-left until
            movement or capture is no longer possible.

        - diagonal_traverse_right():
            Recursively checks diagonals up-right and down-right.

        - remove_skipped_piece():
            Removes the captured pieces.

        - is_winner():
            Checks if there’s a winner and returns the winning side.

        - score():
            Used by AI to calculate the best move score:
            score = pieces_G1 - pieces_G2 + (kings_G1 * x - kings_G2 * x)
            (used in minimax algorithm)

        - get_all_pieces():
            Scans the board and returns all pieces of the specified color 
            (used by minimax algorithm).

5) piece.py:
    - Class Piece:
        Represents a game piece.

        - __init__():
            Initializes piece data and calculates position (via calc_position()).

        - calc_position():
            Calculates the center of the square where the piece should be drawn.

        - make_king():
            Promotes a piece to a king.

        - draw_piece():
            Draws the piece and the king (if promoted).

        - move_piece():
            Updates the piece’s coordinates and recalculates its position.

6) game.py
    - Class Game:
        Handles game state, board, and piece movement.

        - __init__():
            Creates the Board object and sets initial turn to player at the bottom.
            Initializes selected piece and valid moves.

        - update():
            Updates the game board display.

        - select():
            Selects a piece; if already selected, tries to move it.
            Uses get_square() and checks for valid moves.
            Returns True on successful selection/move, False otherwise.

        - move():
            Moves a piece if the move is valid.
            Also removes captured pieces using remove_skipped_piece().

        - draw_valid_moves():
            Highlights valid moves for the selected piece.

        - change_turn():
            Switches the active player.

        - get_board():
            Returns the Board object (used in algorithm.py for AI).

        - ai_move():
            Updates the board and switches the turn (used by AI).

        - winner():
            Returns the winner (via Board's is_winner()).

==========
/minimax/
==========

7) algorithm.py:
    Implements AI.

    - from copy import deepcopy:
        Used to clone the board for simulations (deep copy copies the entire object).

    - minimax():
        Recursive implementation of the MINIMAX ALGORITHM.
        If depth limit is reached, returns score and board state.
        Otherwise, evaluates all possible moves using get_all_moves()
        and simulates outcomes recursively for max and min players.

        The function is called in main.py. Deeper depth increases accuracy
        but also computational cost. Depth = 3 is chosen for balance.

    - get_all_moves():
        Computes all possible moves from current board state.
        For each move, simulates it using simulate_move()
        (deep copy ensures current state isn’t modified).

    - simulate_move():
        Simulates a move and returns the resulting board state.

=======================================
AI for Checkers: THE MINIMAX ALGORITHM:
https://en.wikipedia.org/wiki/Minimax

Evaluates all possible moves and counter-moves.
Uses a minimax score:
score = pieces_G1 - pieces_G2

G1 aims to maximize the score.
G2 aims to minimize the score.

---------------
DECISION TREE:
---------------

                        root(2)
                /         |         \            
        G1_move_1<--->G1_move_2<--->G1_move_3
          (-4)           (-3)           (2)
        /   \            |           /      \
G2_move_1  G2_move_2  G2_move_3  G2_move_4  G2_move_5
   (-4)       (1)       (-3)        (2)       (6)     
   
...

G1 moves first.
The numbers in "(...)" represent the score G2 could get
after each G1 move. G1 chooses the move with the best possible outcome
for itself, assuming G2 will respond optimally to minimize G1's gain.

This alternating process repeats...

=======================================
