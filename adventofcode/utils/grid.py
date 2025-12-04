# delta row / delta column
# right, left, up, down, up-left, up-right, down-left, down-right (respectively)
# modified from day15, 2021
from typing import Any, Tuple, Iterable, List
from collections import defaultdict

DR = [0, 0, -1, 1, -1, -1, 1, 1]
DC = [1, -1, 0, 0, -1, 1, -1, 1]

# Tuple in (y,x) form
UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)


def deltas_2d() -> Iterable[Tuple[int, int]]:
  return zip(DR, DC)


class Grid:
  """Creates a dictionary of coordinates to value.
    e.g. {(0,0): "@", (0,1): ".", (1,1): "@"}

  NOTE: the coordinates are in (y,x) form and NOT (x,y) form
  """

  def __init__(self, grid: List[str]) -> None:
    self.grid = defaultdict(
      lambda: "",
      {(y, x): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))},
    )

  def neighbors(self, coordinate: Tuple[int, int]) -> List[Any]:
    """Returns a list of values for each of the 8 possible neighbors of the given coordinate"""
    y, x = coordinate
    return [self.grid.get((y + delta_y, x + delta_x)) for delta_x, delta_y in deltas_2d()]
