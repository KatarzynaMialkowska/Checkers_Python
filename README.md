# CHECKERS GAME

A simple Checkers game implemented in Python using Pygame.

---

## GENERAL RULES

You can find the general rules of Checkers (Draughts) here:  
https://en.wikipedia.org/wiki/Draughts

---

## IMPLEMENTED CHECKERS RULES

- Pieces can capture only **forward**.  
- Pieces move one square at a time.  
- Kings move like regular pieces but can also capture **backwards**.  
- Capturing is **not mandatory**.  
- The white player starts the game.  
- The player who captures all the opponent's pieces **wins**.  

---

## HOW TO PLAY

- Use the **left mouse button** to select the game mode.  
- Use the **ESCAPE** key or close the window to exit the game.  
- Press **ESCAPE** during the game to return to the menu (you’ll lose your progress).  
- To move a piece:
  - Click the piece.
  - Click the square you want to move it to.

---

## HOW TO RUN THE GAME

Make sure you have Python installed along with the Pygame library.

### Command to run:
```bash
python main.py
```

Inspired by Tim Ruscica’s project:  
https://www.youtube.com/watch?v=vnd3RfeG3NM

---

## DOCUMENTATION

### 1) main.py

- `main_menu()`  
  Creates a menu with two buttons:
  - Player vs Player
  - Player vs Computer

- `game_vs_player()`  
  Starts the game in player vs player mode.

- `game_vs_computer()`  
  Starts the game in player vs computer mode.

- `position_from_mouse()`  
  Gets the position from a mouse click and converts it to board coordinates.

---

### /assets/

Contains all images, music, and other resources used in the program.

---

### /checkers/

#### 2) \_\_init\_\_.py  
Initializes the `checkers` folder as a package/module.

#### 3) constants.py  
Stores constant variables used throughout the program.

#### 4) board.py  
Contains the `Board` class that represents the game board.

- `__init__()` – Initializes the board and calls `init_board()`.  
- `init_board()` – Fills the board with pieces or empty spaces.  
- `draw_board()` – Draws the board and pieces.  
- `move()` – Moves a piece, promotes to king if applicable.  
- `get_square()` – Returns what's at a specific square.  
- `get_valid_moves()` – Calculates possible moves.  
- `diagonal_traverse_left()` and `diagonal_traverse_right()` – Used to explore valid diagonal captures.  
- `remove_skipped_piece()` – Removes captured pieces.  
- `is_winner()` – Checks for a winner.  
- `score()` – Evaluates board score for AI.  
- `get_all_pieces()` – Gets all pieces of a given color.

#### 5) piece.py  
Contains the `Piece` class that represents a game piece.

- `__init__()` – Initializes piece data.  
- `calc_position()` – Finds where to draw the piece.  
- `make_king()` – Promotes a piece to a king.  
- `draw_piece()` – Draws the piece.  
- `move_piece()` – Updates coordinates and recalculates position.

#### 6) game.py  
Contains the `Game` class, managing game state and player moves.

- `__init__()` – Sets up the board and initializes turn/selection.  
- `update()` – Updates the game window.  
- `select()` – Selects or moves a piece.  
- `move()` – Performs a move and removes any captured pieces.  
- `draw_valid_moves()` – Highlights valid moves.  
- `change_turn()` – Switches players.  
- `get_board()` – Returns the board object.  
- `ai_move()` – Makes an AI move.  
- `winner()` – Returns the winner.

---

### /minimax/

#### 7) algorithm.py  
Implements the **Minimax algorithm** for AI.

- `minimax()` – Recursively evaluates best moves using simulated board states.  
- `get_all_moves()` – Generates all possible moves for a player.  
- `simulate_move()` – Simulates and returns a new board state.

Uses deep copies to preserve original state while simulating future moves.

---

## AI FOR CHECKERS: THE MINIMAX ALGORITHM

Based on: https://en.wikipedia.org/wiki/Minimax

The AI simulates all possible player moves and counter-moves, assigning scores:  
`score = pieces_player1 - pieces_player2`

- Player 1 maximizes the score.  
- Player 2 minimizes the score.

---

## DECISION TREE EXAMPLE

```
                        root(2)
                /        |        \
         move_1(-4)  move_2(-3)  move_3(2)
          /   \         |         /   \
      (-4)   (1)      (-3)     (2)   (6)
```

Each level alternates between player moves. The AI assumes both players play optimally.
