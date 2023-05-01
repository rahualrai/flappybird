# Flappy Bird

This is a simple Flappy Bird game created using Pygame just out of boredom lol.

## How to Play

- Press the Space key to make the bird flap and avoid the pipes.
- Each pipe successfully passed through gives you 1 point.
- If you collide with a pipe or the ground, the game is over.
- Press R to replay or Esc to quit the game when the game is over.

## Requirements

Python 3.x, you can install the latest version of Python here: [Python's Official Website](https://www.python.org/downloads/) 

Pygame. To install Pygame. Run this command on your terminal:
```bash 
pip install pygame
```

## How to Install

1. Clone the repository:
    ```bash
    git clone https://github.com/luminaa/flappybird
    cd flappybird
    ```

2. Run the game by running the following command in your terminal:
    ```bash
    python flappybird.py
    ```

## Customizations

You can change the game window size by modifying the WINDOW_WIDTH and WINDOW_HEIGHT variables in `flappybird.py`

You can change the pipe speed and bird gravity by modifying the `self.gravity` value in the `Bird` class and the `self.x -=` value in the update method of the `Pipe` class.
