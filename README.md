# Tic-Tac-Toe AI (Minimax)
*A project from [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2024/)*

This project implements an unbeatable Tic-Tac-Toe AI using the **Minimax algorithm**. A simple GUI is provided using **Pygame**, allowing you to play against the AI.

## Project Goals

- Implement the **Minimax** algorithm for turn-based decision making.
- Model game states and simulate future outcomes.
- Understand game theory and terminal states.
- Build a GUI using **Pygame** to make the game interactive.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/constantin-catalina/tic-tac-toe.git
cd tic-tac-toe
```

### 2. Install Dependencies
```bash
pip3 install -r requirements.txt
```

## How to play
To start the game run:
```bash
python runner.py
```
- You play as O and the AI plays as X
- The game continues until there is a win or a tie

## File Descriptions
| File               | Description                                    |
| ------------------ | ---------------------------------------------- |
| `tictactoe.py`     | Contains the core logic and AI decision-making |
| `runner.py`        | Graphical interface using Pygame (provided)    |
| `requirements.txt` | Python dependency file (requires `pygame`)     |

## Functions
| Function                | Description                                                   |
| ----------------------- | ------------------------------------------------------------- |
| `player(board)`         | Returns the player who has the next turn (`X` or `O`)         |
| `actions(board)`        | Returns a set of all available actions `(i, j)`               |
| `result(board, action)` | Returns a new board with the move applied at `(i, j)`         |
| `winner(board)`         | Returns the winner of the game (`X`, `O`, or `None`)          |
| `terminal(board)`       | Returns `True` if the game is over, `False` otherwise         |
| `utility(board)`        | Returns `1` if X wins, `-1` if O wins, `0` for a tie          |
| `minimax(board)`        | Returns the optimal move `(i, j)` using the Minimax algorithm |


## License
This project was completed as part of CS50 AI 2024. It is intended for educational purposes only.
