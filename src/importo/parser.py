from . import utils

from rich import print
from rich.console import Console
from rich.table import Table


PROFILE_PREFIX = "import time:"
SORT_INDEX = {
    "cumulative": 2,
    "self": 1,
    "name": 0,
}

# Switching to stderr for the time being.
# Formatting for piping/output to other tools is
# still under definition.
# So for now we'll focus on the best human interface
# and then boil down the machine-useful bits to stdout .
console = Console(stderr=True)


def parse(profiles):
    stats = {}
    iterations = len(profiles)
    for stream in profiles:
        for (
            lineno,
            l,
        ) in enumerate(stream):
            if lineno == 0:
                continue
            if not l.startswith(PROFILE_PREFIX):
                continue
            tokens = l.strip().lstrip(PROFILE_PREFIX).split("|")
            self_, cumulative, explicit_import = [t.strip() for t in tokens]
            if explicit_import not in stats:
                stats[explicit_import] = {
                    "self": [int(self_)],
                    "cumulative": [int(cumulative)],
                }
            else:
                stats[explicit_import]["self"].append(int(self_))
                stats[explicit_import]["cumulative"].append(int(cumulative))
    for i in stats:
        s = stats[i]["self"]
        c = stats[i]["cumulative"]
        stats[i]["self_avg"] = utils.avg(s)
        stats[i]["self_p90"] = utils.percentile(s, 90)
        stats[i]["self_p99"] = utils.percentile(s, 99)
        stats[i]["cumulative_avg"] = utils.avg(c)
        stats[i]["cumulative_p90"] = utils.percentile(c, 90)
        stats[i]["cumulative_p99"] = utils.percentile(c, 99)

    return stats


def view(stats, depth, match, sort, quiet):
    ordered = []
    for s in stats:
        # if its not a root module, skip it.
        if len(s.split(".")) > (depth + 1):
            continue
        if match is not None and match not in s:
            continue
        ordered.append((s, stats[s]["self_p99"], stats[s]["cumulative_p99"]))
    ordered = sorted(ordered, key=lambda t: t[SORT_INDEX[sort]], reverse=True)
    table = Table("cumulative", "self", "import")
    for o in ordered:
        table.add_row(o[2], o[1], o[0])
    console.print(table)
