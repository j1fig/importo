#!/usr/bin/env python3
"""
Python import time profiler.
"""
from signal import signal, SIGPIPE, SIG_DFL
import sys
import argparse

from . import profiler, parser


# see https://stackoverflow.com/a/30091579
# this allows the output to be partially consumed.
signal(SIGPIPE, SIG_DFL)


def parse_args(argv):
    """ Parse and validate command line arguments """

    aparser = argparse.ArgumentParser(description=__doc__)
    aparser.add_argument(
        "module",
        help="module to profile",
    )
    aparser.add_argument("--depth", "-d", type=int, default=0, help="import tree depth")
    aparser.add_argument("--match", "-m", help="string to match module paths by")
    aparser.add_argument("--iterations", "-i", type=int, default=1, help="number of times the profiler will run.")
    aparser.add_argument("--parallelism", "-p", type=int, default=1, help="number of processes that are running the profiling")
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


def main(argv=None):
    """ Run this program """
    if argv is None:
        argv = sys.argv
    args = parse_args(argv)
    try:
        profiles = profiler.profile(args.module, args.parallelism)
        stats = parser.parse(profiles)
        parser.view(stats, args.depth, args.match, args.sort, args.quiet)
    except KeyboardInterrupt:
        sys.exit(-1)


if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
