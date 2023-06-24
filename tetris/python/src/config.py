class Config:

    FRAME_RATE = 100
    FALL_RATE = 30

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    CYAN = (0, 255, 255)
    YELLOW = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    ORANGE = (255, 165, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Set the width and height of the screen (adjust as needed)
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    # Set the width and height of the grid
    GRID_WIDTH = 10
    GRID_HEIGHT = 20
    GRID_SIZE = 30

    # Set the initial position of the falling shape
    INITIAL_X = 4
    INITIAL_Y = 0

    SHAPES = [
        [[1, 1, 1, 1]],  # I-shape
        [[1, 0, 0], [1, 1, 1]],  # J-shape
        [[0, 0, 1], [1, 1, 1]],  # L-shape
        [[1, 1], [1, 1]],  # O-shape
        [[0, 1, 1], [1, 1, 0]],  # S-shape
        [[0, 1, 0], [1, 1, 1]],  # T-shape
        [[1, 1, 0], [0, 1, 1]]  # Z-shape
    ]

    SHAPE_COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, MAGENTA, RED]
