# Rock Paper Scissors Game
A fun, simple, and interactive console-based version of the classic game, Rock, Paper, Scissors! Challenge the computer, make your move, and see if you can beat it. The game will keep track of your choices and let you play as many rounds as you like. Ready to play?

## Table of Contents
- [How to Play](#how-to-play)
- [Game Features](#game-features)
- [Installation](#installation)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)

## How to Play
The classic game of Rock, Paper, Scissors where you play against the computer. The rules are simple:
1. **Rock** beats **Scissors**.
2. **Scissors** beats **Paper**.
3. **Paper** beats **Rock**.

When you run the program, you will be prompted to choose:
- `0` for Rock
- `1` for Paper
- `2` for Scissors

The computer will randomly make its choice, and the winner will be determined based on the rules mentioned above. You can play multiple rounds until you choose to exit.

## Game Features
- Simple text-based interface.
- Ability to play as many rounds as you want.
- Computer randomly chooses its move.
- Clear and fun display of results using ASCII art.

## Installation
To run the game, you need to have Python installed on your machine. Follow the steps below:

1. Clone the repository or copy the game code to your local machine.
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the directory containing the game code.
    ```bash
    cd rock-paper-scissors
    ```
3. Run the game using Python.
    ```bash
    python main.py
    ```

## Code Explanation

The game code is organized into several key parts:

1. **ASCII Art**: The `rock`, `paper`, and `scissors` variables contain the ASCII representations of each move. This adds a visual element to the game when displaying the results.
   
2. **`user_input()` function**: This function prompts the user to select their move (Rock, Paper, or Scissors) by typing `0`, `1`, or `2`. It ensures valid input by catching any errors and re-prompting if necessary.

3. **Game Loop**: The `while game_is_on:` loop continuously runs the game until the player decides to quit. Inside this loop:
    - The user’s choice is taken as input, and the computer makes a random choice.
    - The results are displayed with ASCII art.
    - The winner is determined based on standard Rock, Paper, Scissors rules.

4. **`continue_game()` function**: After each round, this function asks the user if they want to play again. It ensures valid input by re-prompting if necessary. The loop continues until the user decides to exit.

5. **Decision-Making Logic**: The game uses `if-elif` statements to determine the winner of each round based on the user's and the computer's choices.

## Contributing

Feel free to improve the game, fix any bugs, or add new features. All contributions are welcome!
