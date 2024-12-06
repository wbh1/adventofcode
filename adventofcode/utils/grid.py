# delta row / delta column
# right, left, up, down, up-left, up-right, down-left, down-right (respectively)
# modified from day15, 2021
from typing import Tuple, Iterable


DR = [0, 0, -1, 1, -1, -1, 1, 1]
DC = [1, -1, 0, 0, -1, 1, -1, 1]

# Tuple in (y,x) form
UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)


def deltas_2d() -> Iterable[Tuple[int, int]]:
  return zip(DR, DC)
