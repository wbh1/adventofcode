from typing import List, Tuple
from adventofcode.utils.Puzzle import Puzzle
from adventofcode.utils import grid


class Day4(Puzzle):
  day = 4

  def __init__(self, data=None, debug=False):
    super().__init__(data, debug)
    self.grid = grid.Grid(self.data)

  def is_accessible(self, roll: Tuple[int, int]) -> bool:
    neighbors = self.grid.neighbors(roll)
    return neighbors.count("@") < 4

  def pickable_rolls(self) -> List[Tuple[int, int]]:
    pickable = []
    for c, value in self.grid.grid.items():
      if value == "@":
        if self.is_accessible(c):
          pickable.append(c)
    return pickable

  def part1(self) -> int:
    return len(self.pickable_rolls())

  def part2(self) -> int:
    removed = 0
    pickable_rolls = self.pickable_rolls()
    while len(pickable_rolls) != 0:
      for c in pickable_rolls:
        self.grid.grid[c] = "."

      removed += len(pickable_rolls)
      pickable_rolls = self.pickable_rolls()
    return removed
