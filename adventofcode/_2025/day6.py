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

  def part1(self) -> int:
    self.log(f"Parsed data: {self.parsed_data}")
    self.log(f"Operations: {self.operations}")
    results: List[int] = []
    for i, op in enumerate(self.operations):
      inputs = [int(row[i]) for row in self.parsed_data]
      self.log(f"str Inputs: {[row[i] for row in self.parsed_data]}")
      self.log(f"Inputs: {inputs}")
      match op:
        case "*":
          results.append(math.prod(inputs))
        case "+":
          results.append(sum(inputs))
        case _:
          raise ValueError(f"Unknown math operation to perform: `{op}`")

    return sum(results)

  def part2(self) -> int:
    results: List[int] = []
    for i, op in enumerate(reversed(self.operations)):
      nums = [row[len(row) - 1 - i] for row in self.parsed_data]
      self.log(f"Nums: {nums}")
      inputs = []
      for c in range(len(nums[0]), 0, -1):
        self.log(f"   nums={nums} c={c}")
        number = int("".join([n[c - 1][::-1] for n in nums]).strip() or 0)
        if number:
          inputs.append(number)

      self.log(f"Inputs: {inputs}; op=`{op}`")
      match op:
        case "*":
          results.append(math.prod(inputs))
        case "+":
          results.append(sum(inputs))
        case _:
          raise ValueError(f"Unknown math operation to perform: `{op}`")

    return sum(results)

