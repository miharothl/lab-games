"""
Implement Tetris game in Python using PyGame
"""
import random
import sys

import pygame as pygame

from domain.game import Game
from config import Config
from infrastructure.display import Display


def main():
    config = Config()

    display = Display(config)

    clock = pygame.time.Clock()

    # Initialize the game grid
    grid = [[config.BLACK] * config.GRID_WIDTH for _ in range(config.GRID_HEIGHT)]

    game = Game(grid)

    # Initialize the current shape
    current_shape = random.choice(config.SHAPES)
    current_color = random.choice(config.SHAPE_COLORS)
    current_x = config.INITIAL_X
    current_y = config.INITIAL_Y

    running = True

    fall_step = 0
    while running:
        clock.tick(config.FRAME_RATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    if not game.check_collision(current_shape, current_x - 1, current_y, grid):
                        current_x -= 1
                elif event.key == pygame.K_l:
                    if not game.check_collision(current_shape, current_x + 1, current_y, grid):
                        current_x += 1
                elif event.key == pygame.K_k:
                    rotated_shape = game.rotate_clockwise(current_shape)
                    if not game.check_collision(rotated_shape, current_x, current_y, grid):
                        current_shape = rotated_shape
                elif event.key == pygame.K_j:
                    rotated_shape = game.rotate_anticlockwise(current_shape)
                    if not game.check_collision(rotated_shape, current_x, current_y, grid):
                        current_shape = rotated_shape
                elif event.key == pygame.K_a:
                    if not game.check_collision(current_shape, current_x, current_y - 1, grid):
                        current_y -= 1
                elif event.key == pygame.K_SPACE:
                    if not game.check_collision(current_shape, current_x, current_y + 1, grid):
                        current_y += 1

        if not game.check_collision(current_shape, current_x, current_y + 1, grid):

            fall_step += 1
            if fall_step % config.FALL_RATE == 0:
                fall_step = 0
                current_y += 1
        else:
            game.merge_shape(current_shape, current_x, current_y, grid, current_color)
            game.remove_completed_rows(grid)

            # Reset the current shape
            current_shape = random.choice(config.SHAPES)
            current_color = random.choice(config.SHAPE_COLORS)
            current_x = config.INITIAL_X
            current_y = config.INITIAL_Y

            if game.check_collision(current_shape, current_x, current_y, grid):
                running = False

        pygame.display.update()

        display.clear()

        display.draw_grid()

        display.draw_falling_shape(current_shape, current_x, current_y, current_color)

        display.draw_filled_cells(grid)

    pygame.quit()
    sys.exit()




if __name__ == "__main__":
    main()
