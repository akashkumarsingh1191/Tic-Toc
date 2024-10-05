# Tic-Tac-Toe: A Simple Game
=====================================
# Author: Akash Kumar Singh
# Date: 2021-12-15 10:30:00
=====================================

# Introduction:

Tic-Tac-Toe is a simple two-player game played on a 3x3 grid.
The players alternate turns, with one playing as 'X' and the other as 'O'.
The objective is to be the first to mark three squares in a row (horizontally, vertically, or diagonally).

# Game Description:

The game begins with an empty 3x3 grid.
Player X always goes first, and players take turns.
The game ends when one player marks three squares in a row or when all squares are filled with no winner (a draw).

# Game Rules:
The game starts with an empty 3x3 grid.
Player X goes first.
Players alternate turns between X and O.
A player can only mark a square that is empty.
The game ends when:
    One player has three in a row (horizontally, vertically, or diagonally).
All squares are filled, and there is no winner (draw).

# Game Flow:
The game follows a simple loop where players alternate turns.
After each move:
The grid is checked for a winning condition.
If no winner and moves remain, the next player takes their turn.
If the grid is full with no winner, the game ends in a draw.
