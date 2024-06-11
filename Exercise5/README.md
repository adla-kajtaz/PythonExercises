# Exercise 5

### Battleship Game

One of the exercises included in this repository is a one-player version of the classic board game Battleship. In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. The player will have 4 guesses to try to sink the ship.

### Steps to Implement the Battleship Game:

1. Create the Game Board

   - Create a variable board and set it to an empty list.
   - Use a loop to generate a 5x5 grid of "O"s to represent the ocean.
   - Append five rows of five "O"s to board.

2. Print the Game Board

   - To display the board to the player, we'll define a function `print_board()`

3. Hide the Battleship

   - Define two functions, `random_row` and `random_col`, that return a random index for a row and column, respectively.
   - Store the ship's location in `ship_row` and `ship_col`.

4. Get Player's Guess

   - Prompt the user to enter their guess for the row and column.

5. Check Player's Guess

   - Compare the player's guess to the ship's location and provide feedback.
   - If the guess is correct, print a success message.
   - If the guess is incorrect, print a miss message and mark the board with an "X".

6. Allow Multiple Guesses
   - Allow the player to make up to 4 guesses.
   - Print the turn number at the beginning of each turn.
