from adventofcode.utils.Puzzle import Puzzle

class Day2(Puzzle):
    day = 2

    def __init__(self, data=None, debug=False):
      super().__init__(data, debug)
      self.ranges = [x for x in self.data[0].split(",")]

    def part1(self) -> int:
      total = 0
      for r in self.ranges:
        self.log(f"range={r}")
        start, end = tuple(r.split("-"))
        for x in range(int(start), int(end)+1):
          x = str(x)
          repeat = x[:len(x)//2]
          if x[:len(x)//2] == x[len(x)//2:]:
            self.log(f"    {x} repeats {repeat} twice")
            total += int(x)

      return total

    def part2(self) -> int:
      invalid_ids = []
      for r in self.ranges:
        self.log(f"range={r}")
        start, end = r.split("-")
        for x in range(int(start), int(end)+1):
          x = str(x)
          for part_len in range(1,len(x)//2+1):
              part = x[:part_len]
              # Ensure number splits into equally sized parts with this length
              if len(x) % part_len == 0:
                  # Check if multiplying the substring N times results in the original number
                  if part * (len(x)//part_len) == x:
                    invalid_ids.append(int(x))
                    break
      return sum(invalid_ids)
