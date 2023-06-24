import pygame


class Display:

    def __init__(self, config):
        self.config = config

        pygame.init()
        self.window = pygame.display.set_mode((self.config.GRID_WIDTH * self.config.GRID_SIZE, self.config.GRID_HEIGHT * self.config.GRID_SIZE))
        pygame.display.set_caption("Tetris")

    def draw_grid(self):
        for x in range(self.config.GRID_WIDTH):
            for y in range(self.config.GRID_HEIGHT):
                pygame.draw.rect(
                    self.window,
                    self.config.WHITE,
                    (x * self.config.GRID_SIZE, y * self.config.GRID_SIZE, self.config.GRID_SIZE, self.config.GRID_SIZE),
                    1
                )

    def draw_falling_shape(self, shape, x, y, color):
        shape_height = len(shape)
        shape_width = len(shape[0])

        for row in range(shape_height):
            for col in range(shape_width):
                if shape[row][col]:
                    pygame.draw.rect(
                        self.window,
                        color,
                        (
                            (x + col) * self.config.GRID_SIZE,
                            (y + row) * self.config.GRID_SIZE,
                            self.config.GRID_SIZE,
                            self.config.GRID_SIZE
                        )
                    )

    def draw_filled_cells(self, grid):
        # Draw the filled cells
        for row in range(self.config.GRID_HEIGHT):
            for col in range(self.config.GRID_WIDTH):
                if grid[row][col] != self.config.BLACK:
                    pygame.draw.rect(
                        self.window,
                        grid[row][col],
                        (
                            col * self.config.GRID_SIZE,
                            row * self.config.GRID_SIZE,
                            self.config.GRID_SIZE,
                            self.config.GRID_SIZE
                        )
                    )

    def clear(self):
        # Clear the screen
        self.window.fill(self.config.BLACK)
