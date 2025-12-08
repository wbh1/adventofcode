from typing import Dict
from adventofcode.utils.Puzzle import Puzzle


class Day7(Puzzle):
  day = 7
  beams: Dict[int, int]
  splits: int

  def traverse_manifold(self):
    if hasattr(self, "splits") and hasattr(self, "beams"):
      return
    start_col = self.data[0].index("S")
    beams = {start_col: 1}
    splits = 0
    for row in self.data[1:]:
      next_beams = {}
      for col, count in beams.items():
        if row[col] == "^":
          next_beams[col - 1] = next_beams.get(col - 1, 0) + count
          next_beams[col + 1] = next_beams.get(col + 1, 0) + count
          splits += 1
        else:
          # No split: beam continues straight
          next_beams[col] = next_beams.get(col, 0) + count
      beams = next_beams
    self.beams = beams
    self.splits = splits

  def part1(self) -> int:
    self.traverse_manifold()
    return self.splits

  def part2(self) -> int:
    self.traverse_manifold()
    return sum(self.beams.values())  # total paths (tachyon count)

