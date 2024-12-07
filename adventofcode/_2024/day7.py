from typing import List, Set

from adventofcode.utils.Puzzle import Puzzle


def can_make(result: int, nums: List[int], concat=False) -> bool:
  if len(nums) == 1:
    return nums[0] == result

  last = nums[-1]

  if result % last == 0:
    could_mult = can_make(result // last, nums[:-1], concat=concat)
  else:
    could_mult = False

  if concat:
    # Cheated off of reddit after failing to do string manipulation
    next_power_of_10 = 1
    while next_power_of_10 <= last:
      next_power_of_10 *= 10
    if (result - last) % next_power_of_10 == 0:
      could_concat = can_make((result - last) // next_power_of_10, nums[:-1], concat=concat)
    else:
      could_concat = False
  else:
    could_concat = False

  if (result - last) > 0:
    could_add = can_make(result - last, nums[:-1], concat=concat)
  else:
    could_add = False

  return could_mult or could_add or could_concat


class Day7(Puzzle):
  day = 7

  def part1(self) -> int:
    valid_results: Set[int] = set()
    for line in self.data:
      res = int(line.split(": ")[0])
      nums = [int(n) for n in line.split(": ")[1].split(" ")]
      if can_make(res, nums):
        valid_results.add(res)
    return sum(valid_results)

  def part2(self) -> int:
    valid_results: Set[int] = set()
    for line in self.data:
      res = int(line.split(": ")[0])
      nums = [int(n) for n in line.split(": ")[1].split(" ")]
      if can_make(res, nums, concat=True):
        valid_results.add(res)
    return sum(valid_results)

