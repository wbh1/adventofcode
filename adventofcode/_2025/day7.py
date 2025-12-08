from typing import Set
from adventofcode.utils.Puzzle import Puzzle
from collections import Counter


class Day7(Puzzle):
  day = 7

  def count_splits(self, part2=False) -> int:
    active_beam_columns: Set[int] = set([self.data[0].index("S")])
    tachyons = Counter(active_beam_columns)
    splits = 0
    for row in self.data[1:]:
      for col, value in enumerate(row):
        if col in active_beam_columns and value == "^":
          active_beam_columns.remove(col)
          active_beam_columns.update([col - 1, col + 1])
          tachyons[col - 1] += tachyons[col]
          tachyons[col + 1] += tachyons[col]
          del tachyons[col]
          splits += 1
    if part2:
      return sum(tachyons.values())
    else:
      return splits

  def part1(self) -> int:
    return self.count_splits()

  def part2(self) -> int:
    return self.count_splits(part2=True)

