from typing import Set, Tuple

from adventofcode.utils.grid import DOWN, LEFT, RIGHT, UP
from adventofcode.utils.Puzzle import Puzzle


class Day6(Puzzle):
  day = 6

  def find_guard(self, grid=None) -> Tuple[int, int]:
    if grid is None:
      grid = self.data
    for y in range(len(grid)):
      for x in range(len(grid[y])):
        if grid[y][x] == "^":
          return (y, x)

    raise LookupError("Couldn't find the guard anywhere in the dataset")

  def patrol(self, grid=None) -> Tuple[Set[Tuple[Tuple[int, int], Tuple[int, int]]], bool]:
    """
    returns a Tuple of (Set(positions_visited, direction_when_visited), exited_map)
    """

    if grid is None:
      grid = self.data

    def leaves_map(point: Tuple[int, int]):
      next_y, next_x = point
      if (0 > next_y or 0 > next_x) or (next_y > len(grid) - 1 or next_x > len(grid[0]) - 1):
        return True
      return False

    directions = [UP, RIGHT, DOWN, LEFT]
    facing = UP
    position = self.find_guard(grid=grid)
    visited: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()
    loops = 0
    exited_map = False
    while (position, facing) not in visited:
      if loops >= 99999:
        raise RecursionError("I'm lost and wandering aimlessly.")
      visited.add((position, facing))
      next_y, next_x = position[0] + facing[0], position[1] + facing[1]
      turns = 1
      dir_idx = directions.index(facing)
      while not leaves_map((next_y, next_x)) and grid[next_y][next_x] == "#":
        if turns >= 4:
          raise RecursionError("I'm spinning in circles. Make it stop!!!")
        facing = directions[(dir_idx + turns) % len(directions)]
        next_y, next_x = position[0] + facing[0], position[1] + facing[1]
        turns += 1
      if leaves_map((next_y, next_x)):
        exited_map = True
        break
      position = (next_y, next_x)
      loops += 1
    return (visited, exited_map)

  def part1(self) -> int:
    return len(set(v[0] for v in self.patrol()[0]))

  def part2(self) -> int:
    """
    Tip: Run with pypy (instead of cpython) for part2 so it completes in ~2s instead of ~15s
    """
    initial_path = set(v[0] for v in self.patrol()[0])
    grid = [list(line) for line in self.data]
    obstructions: Set[Tuple[int, int]] = set()
    for pos in initial_path:
      y, x = pos
      if grid[y][x] != ".":
        continue
      grid[y][x] = "#"
      _, exited_map = self.patrol(grid=grid)
      if not exited_map:
        obstructions.add((y, x))
      grid[y][x] = "."

    return len(obstructions)

