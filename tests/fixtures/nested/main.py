import sys


def run():
    from time import time
    s = time()
    def _run():
        import json
        e = time() - s
        limit = sys.getrecursionlimit()
        return limit
    return _run()
