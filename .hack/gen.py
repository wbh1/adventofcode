import datetime
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace
from os import path
import sys
from typing import Dict

from jinja2 import Environment, FileSystemLoader, select_autoescape

TMPL_NAMES = ["day_n.py.j2", "test_day_n.py.j2"]


def _args() -> Namespace:
    parser = ArgumentParser(
        prog="gen.py",
        description="AoC solution skeleton generator",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("day", help="which day to run")
    parser.add_argument(
        "-y", "--year", help="which year to run", default=datetime.datetime.now().year
    )
    return parser.parse_args()


def _template(env: Environment, tmpl_name: str, ctx: Dict[str, str]) -> str:
    tmpl = env.get_template(tmpl_name)
    return tmpl.render(ctx)


if __name__ == "__main__":
    args = _args()
    env = Environment(loader=FileSystemLoader(".hack"), autoescape=select_autoescape())
    for tmpl in TMPL_NAMES:
        basepath = ""
        if tmpl.startswith("test"):
            basepath = path.join("tests", str(args.year))
        else:
            basepath = path.join("adventofcode", f"_{args.year}")

        fp = path.join(
            basepath,
            tmpl.replace(".j2", "").replace("_n", args.day),
        )
        if path.exists(fp):
            print(f"File already exists at {fp}")
            continue
        data = _template(env, tmpl, args.__dict__)
        with open(
            fp,
            "w",
        ) as f:
            f.write(data)
            print(f"Wrote new file to {f.name}")
