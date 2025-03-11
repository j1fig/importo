#!/usr/bin/env python3
from signal import signal, SIGPIPE, SIG_DFL

from typing_extensions import Annotated
from rich import print
import typer

from . import fs, profiler, parser, tree


# see https://stackoverflow.com/a/30091579
# this allows the output to be partially consumed.
signal(SIGPIPE, SIG_DFL)


def main(
    path:       Annotated[str,  typer.Argument(help="path to scan Python files from")] = ".",
    depth:      Annotated[int,  typer.Option(help="import tree depth")] = 0,
    iterations: Annotated[int,  typer.Option(help="number of times the profiler will run")] = 1,
    sort:       Annotated[str,  typer.Option(help="sort key for results by {cumulative,self,name}")] = "cumulative",
    quiet:      Annotated[bool, typer.Option(help="displays just the cumulative time taken to import the selected module")] = False,
    match:      Annotated[str,  typer.Option(help="string to match module paths by")] = None
):
    """
    A Python import profiler.
    """
    py_files = fs.list_py(path)
    if not quiet:
        print(f"Found {len(py_files)} Python files.")

    imports = {
        f: tree.parse_imports(f)
        for f in py_files
    }
    print(imports)
