BLACK = (0, 0, 0)


class Game:

    def __init__(self, grid):
        self.grid = grid

        self.grid_width = len(grid[0])
        self.grid_height = len(grid)

    def check_collision(self, shape, x, y, grid):
        shape_height = len(shape)
        shape_width = len(shape[0])

        for row in range(shape_height):
            for col in range(shape_width):
                if (
                        x + col < 0
                        or x + col >= self.grid_width
                        or y + row >= self.grid_height
                        or (shape[row][col] and grid[y + row][x + col] != BLACK)
                ):
                    return True
        return False

    def merge_shape(self, shape, x, y, grid, current_color):
        shape_height = len(shape)
        shape_width = len(shape[0])

        for row in range(shape_height):
            for col in range(shape_width):
                if shape[row][col]:
                    grid[y + row][x + col] = current_color

    def remove_completed_rows(self, grid):
        rows_to_remove = []
        for row in range(self.grid_height):
            if all(cell != BLACK for cell in grid[row]):
                rows_to_remove.append(row)

        for row in rows_to_remove:
            del grid[row]
            grid.insert(0, [BLACK] * self.grid_width)

    def rotate_clockwise(self, shape):
        """
        Rotates the shape clockwise by 90 degrees.
        """
        return list(zip(*reversed(shape)))

    def rotate_anticlockwise(self, shape):
        """
        Rotates the shape anticlockwise by 90 degrees.
        """
        return list(reversed(list(zip(*shape))))
