import sys

from . import main


def entrypoint():
    sys.exit(main(sys.argv) or 0)


if __name__ == "__main__":
    entrypoint()
