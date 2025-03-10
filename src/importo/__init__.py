#!/usr/bin/env python3
"""
Python import time profiler.
"""

from signal import signal, SIGPIPE, SIG_DFL

from typing_extensions import Annotated
from rich import print
import typer

from . import fs, profiler, parser


# see https://stackoverflow.com/a/30091579
# this allows the output to be partially consumed.
signal(SIGPIPE, SIG_DFL)


def parse_args(argv):
    """Parse and validate command line arguments"""

    aparser = argparse.ArgumentParser(description=__doc__)
    aparser.add_argument(
        "module",
        help="module to profile",
    )
    aparser.add_argument("--depth", "-d", type=int, default=0, help="import tree depth")
    aparser.add_argument("--match", "-m", help="string to match module paths by")
    aparser.add_argument(
        "--iterations",
        "-i",
        type=int,
        default=1,
        help="number of times the profiler will run.",
    )
    aparser.add_argument(
        "--sort",
        "-s",
        default="cumulative",
        help="sort key for results by {cumulative,self,name} - defaults to cumulative",
    )
    aparser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="displays just the cumulative time taken to import the selected module",
    )

    args = aparser.parse_args(argv[1:])
    return args


def main(path: Annotated[str, typer.Argument()] = ".", depth: int = 0, iterations: int = 1, sort: str = "cumulative", quiet: bool = False, match: str = None):
    print(fs.list_py(path))
