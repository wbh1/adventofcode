from adventofcode.utils.Puzzle import Puzzle
import itertools

class Day3(Puzzle):
    day = 3

    @staticmethod
    def max_joltage_part1(bank) -> int:
      return max([int("".join(x)) for x in itertools.combinations(bank, 2)])

    def max_joltage_part2(self, bank: str) -> int:
      digits = 11
      joltage = ""
      self.log(f"bank='{bank}'")
      for i in range(digits, -1, -1):
        if len(bank) == i+1:
          joltage += "".join(bank)
          break
        highest = max(bank[:len(bank)-i])
        self.log(f"  msg='Highest in {bank[:len(bank)-i]} is {highest}' digits='{i}'")
        joltage += highest
        bank = bank[bank.index(highest)+1:]
        self.log(f"  msg='Bank is now {bank}' digits='{i}' joltage='{joltage}'")
      return int(joltage)

    def part1(self) -> int:
      return sum([self.max_joltage_part1(b) for b in self.data])

    def part2(self) -> int:
      return sum([self.max_joltage_part2(b) for b in self.data])
