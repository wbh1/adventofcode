#!/usr/bin/env python3
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from importlib import import_module
import datetime
import os
import sys

if not __package__:
    # Make CLI runnable from source tree with
    #    python src/package
    package_source_path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, package_source_path)

parser = ArgumentParser(
    prog="aoc.py",
    description="AoC Solution Runner",
    formatter_class=ArgumentDefaultsHelpFormatter,
)
parser.add_argument("day", help="which day to run")
parser.add_argument(
    "-y", "--year", help="which year to run", default=datetime.datetime.now().year
)
parser.add_argument(
    "-i",
    "--input",
    help='directory with inputs for the year (named like "day10.txt"). Defaults to inputs/{year}/',
)
args = parser.parse_args()

input_dir = args.input or os.path.join("inputs", args.year)
os.environ["AOC_INPUT_DIR"] = input_dir

day = getattr(
    import_module(f"adventofcode.{args.year}.day{args.day}"), f"Day{args.day}"
)()

day.solve()
