# Pearl Puzzle
Pearl puzzle is a game played on a grid of squares.

At the start of the game, white and black tokens are placed randomly on the grid. When traversing the grid
the player needs to go through each token and finish where they started.

##Playing The Game

###Rules of the Game
The player can start on any square they wish. Click on the edge of the square you wish to depart from.
Clicking with the mouse inside a square to the right will cause a line to go right, clicking inside a square
to the bottom, will cause a line to go down, etc. There are a few conditions the player must adhere to
when drawing a line:
* White pearls must have the line go straight through them
* Black pearls must have the line turn inside them
* White pearls must have a turn directly before or after them
* Black pearls must never have turn directly before or after them
* The path can never intersect with itself except to close the path

###How to Win
As long as all of the rules above are adhered to and the line becomes a circuit (a closed path) when you
get back to where you started, you will win and a message will be displayed on the screen.

###How to Lose
There are certain conditions that can occur where the game is not winnable. If one of these happens, a message
a will be displayed on the screen indicating you lost.
* Closing the loop without visiting all the pearls.
* A white pearl being placed in one of the corners.

##Running the Game

The game cannot be run on the OSU engineering server since PyGame utilizes a GUI to run. This program must
be run on a local machine with a native Python 3 installation.

###Usage

```commandline
python3 pearls.py
```

##On NP-Completeness
We can state that Pearl Puzzle is NP. If we are given a game board and a specified path, it is very easy
to verify that the solution is valid in polynomial time. The path serves as the certificate and the game with the board serve
as the verifier. In other words

> Is there a closed, non-intersecting path passing through every pearl so that
> 1. the path turns at every black pearl, but does not turn immediately before or after
> 2. the path does not turn at any white pearl, but does turn immediately before or after


