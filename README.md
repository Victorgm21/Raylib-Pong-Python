This is a pong game made with pyray.

## Instructions

To play the game, use the `W` and `S` keys to move the player paddle.

## Code Explanation

The `Ball` class represents the ball in the game. It has a position, velocity, radius, and color. The `Ball` class also has methods for drawing the ball, checking for collisions, and playing a sound when the ball hits a paddle or the wall.

The `Paddle` class represents the player and cpu paddles. It has a position, velocity, width, and height. The `Paddle` class also has methods for drawing the paddle and moving it.

The `main.py` file is the main entry point for the game. It initializes the window, creates the ball and paddles, and starts the main game loop. The main game loop updates the ball and paddle positions, checks for collisions, and draws the game to the screen.

The `tablero.py` file contains the code for drawing the game table. The table is made up of 10 rows of green rectangles. The middle row is white and represents the center line of the table.

I hope you enjoy playing the game!