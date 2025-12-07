from typing import List
from adventofcode.utils.Puzzle import Puzzle
import math


class Day6(Puzzle):
  day = 6

  def __init__(self, data=None, debug=False):
    super().__init__(data, debug)

    def parse_fixed_columns(lines):
      marker_line = lines[-1]
      data_lines = lines[:-1]
      # Find marker positions
      marker_indices = [i for i, c in enumerate(marker_line) if c != " "]
      column_slices = []
      for idx, start in enumerate(marker_indices):
        end = marker_indices[idx + 1] if idx + 1 < len(marker_indices) else len(marker_line)
        column_slices.append((start, end))
      # Parse each data line
      parsed = []
      for line in data_lines:
        row = [line[start:end] for start, end in column_slices]
        parsed.append(row)
      return parsed

    self.parsed_data = parse_fixed_columns(self.data)
    self.operations = [op for op in self.data[-1].split() if op]

  def do_homework(self, op: str, inputs: List[int]) -> int:
    match op:
      case "*":
        return math.prod(inputs)
      case "+":
        return sum(inputs)
      case _:
        raise ValueError(f"Unknown math operation to perform: `{op}`")

  def part1(self) -> int:
    results: List[int] = []
    for i, op in enumerate(self.operations):
      inputs = [int(row[i]) for row in self.parsed_data]
      results.append(self.do_homework(op, inputs))

    return sum(results)

  def part2(self) -> int:
    results: List[int] = []
    # reverse the operations
    for i, op in enumerate(reversed(self.operations)):
      # reverse the ordering of columns (retrieve from the end first)
      nums = [row[len(row) - 1 - i] for row in self.parsed_data]
      inputs = []
      for c in range(len(nums[0]), 0, -1):
        # Maybe by luck or intention, there are no 0's in my input
        # so I can do this hack in case all rows for a column are empty space
        number = int("".join([n[c - 1][::-1] for n in nums]).strip() or 0)
        if number:
          inputs.append(number)

      results.append(self.do_homework(op, inputs))

    return sum(results)
