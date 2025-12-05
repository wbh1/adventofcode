from typing import List
from adventofcode.utils.Puzzle import Puzzle


class Day5(Puzzle):
  day = 5

  def __init__(self, data=None, debug=False):
    super().__init__(data, debug)

    split = self.data.index("")
    self.ingredient_ranges = self.data[:split]
    self.ingredients = self.data[split + 1 :]

  def part1(self) -> int:
    self.log(f"Ingredient ranges: {self.ingredient_ranges}")
    self.log(f"Ingredients: {self.ingredients}")

    results: List[int] = []
    for i in self.ingredients:
      fresh = False
      for r in self.ingredient_ranges:
        low, high = r.split("-", 1)
        fresh = int(low) <= int(i) <= int(high)
        if fresh:
          break

      if fresh:
        results.append(int(i))

    return len(results)

  def flatten_ranges(self):
    """Combine ranges to the maximum possible extent"""
    combined_ranges = self._flatten_ranges()
    while combined_ranges != 0:
      combined_ranges = self._flatten_ranges()

  def _flatten_ranges(self) -> int:
    """Combine ranges where possible and return number of ranges that were altered"""
    new_ranges: List[str] = []
    combined_ct = 0
    self.log("Starting a flattening...")
    for i1, r1 in enumerate(self.ingredient_ranges):
      if r1 == "":
        continue
      r1_start, r1_end = r1.split("-", 1)
      combined = False
      for i2, r2 in enumerate(self.ingredient_ranges):
        if i1 == i2:
          continue
        if r2 == "":
          continue
        r2_start, r2_end = r2.split("-", 1)

        if (
          (int(r2_start) <= int(r1_end) or r1_start == r2_start) and int(r2_end) >= int(r1_end)
        ) or r1 == r2:
          new_ranges.append(f"{r1_start}-{r2_end}")
          self.log(f"  Combined '{r1}' and '{r2}' into '{r1_start}-{r2_end}'")
          self.ingredient_ranges[i2] = ""
          combined = True
          combined_ct += 1
          break
      if not combined:
        new_ranges.append(r1)
    self.ingredient_ranges = sorted(new_ranges, key=lambda x: int(x.split("-")[0]))
    return combined_ct

  def part2(self) -> int:
    self.ingredient_ranges = sorted(self.ingredient_ranges, key=lambda x: int(x.split("-")[0]))
    self.flatten_ranges()
    for r in self.ingredient_ranges:
      self.log(f"{r}")

    fresh_ids = 0
    for r in self.ingredient_ranges:
      low, high = r.split("-", 1)
      fresh_ids += int(high) - int(low) + 1

    return fresh_ids
