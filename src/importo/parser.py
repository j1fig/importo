PROFILE_PREFIX = "import time:"
SORT_INDEX = {
    "cumulative": 2,
    "self": 1,
    "name": 0,
}


def parse(stream):
    stats = {}
    for lineno, l, in enumerate(stream):
        if lineno == 0:
            continue
        if not l.startswith(PROFILE_PREFIX):
            continue
        tokens = l.strip().lstrip(PROFILE_PREFIX).split("|")
        self_, cumulative, explicit_import = [t.strip() for t in tokens]
        stats[explicit_import] = {"self": int(self_), "cumulative": int(cumulative)}
    return stats


def view(stats, depth, match, sort, quiet):
    ordered = []
    for s in stats:
        # if its not a root module, skip it.
        if len(s.split(".")) > (depth + 1):
            continue
        if match is not None and match not in s:
            continue
        ordered.append((s, stats[s]["self"], stats[s]["cumulative"]))
    ordered = sorted(ordered, key=lambda t: t[SORT_INDEX[sort]], reverse=True)
    print("cum\tself\timport")
    for o in ordered:
        print(f"{o[2]}\t{o[1]}\t{o[0]}")
