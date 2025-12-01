from adventofcode.utils.Puzzle import Puzzle


class Day1(Puzzle):
    day = 1

    pos = 50

    zero_passes = 0

    @staticmethod
    def movement(rotation: str) -> int:
      direction = rotation[0]
      if direction == "L":
        return -int(rotation[1:])
      else:
        return int(rotation[1:])

    def move(self, clicks: int):
      starting_pos = self.pos
      ending_pos = (self.pos + clicks)
      self.pos = ending_pos % 100
      passes = 0
      # We must've wrapped if the position doesn't match the ending_pos
      if self.pos != ending_pos or ending_pos == 0:
        if ending_pos < 100 and starting_pos != 0:
          passes += 1
        passes += abs(ending_pos) // 100
      self.log(f"Passed {passes} times while moving {clicks} clicks to {self.pos}")
      self.zero_passes += passes

    def part1(self) -> int:
      zeros = 0
      for line in self.data:
        self.log(f"Currently at: {self.pos}. Preparing to move {line}")
        self.move(self.movement(line))
        if self.pos == 0:
          zeros += 1

      return zeros

    def part2(self) -> int:
      return self.zero_passes
