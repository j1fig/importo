import typer

from . import main


def entrypoint():
    typer.run(main)


if __name__ == "__main__":
    entrypoint()
