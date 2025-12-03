from adventofcode.utils.Puzzle import Puzzle

class Day3(Puzzle):
    day = 3

    @staticmethod
    def max_joltage(bank, batteries=2) -> int:
      joltage = ""
      for i in range(batteries-1, -1, -1):
        if len(bank) == i+1:
          joltage += "".join(bank)
          break
        highest = max(bank[:len(bank)-i])
        joltage += highest
        bank = bank[bank.index(highest)+1:]
      return int(joltage)

    def part1(self) -> int:
      return sum([self.max_joltage(b) for b in self.data])

    def part2(self) -> int:
      return sum([self.max_joltage(b, batteries=12) for b in self.data])
