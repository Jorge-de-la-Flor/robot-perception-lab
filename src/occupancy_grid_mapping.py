"""
Occupancy grid mapping demonstration.

Generates a simple 2D occupancy grid with randomly placed obstacles and
visualizes it as a grayscale image.
"""

import numpy as np
import matplotlib.pyplot as plt


GRID_SIZE = 50


def generate_obstacles(grid: np.ndarray, num_obstacles: int = 200) -> None:
    """Randomly mark cells in the grid as occupied.

    Args:
        grid: 2D numpy array representing the occupancy grid (0 = free, 1 = occupied).
        num_obstacles: Number of occupied cells to sample uniformly at random.
    """
    for _ in range(num_obstacles):
        x = np.random.randint(0, GRID_SIZE)
        y = np.random.randint(0, GRID_SIZE)
        grid[x, y] = 1


if __name__ == "__main__":
    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    generate_obstacles(grid)

    plt.imshow(grid, cmap="gray", origin="lower")
    plt.title("Occupancy grid")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.savefig("../assets/occupancy_grid.png")
