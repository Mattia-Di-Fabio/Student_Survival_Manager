from sys import stdout

from src.cli.menu import run


if __name__ == "__main__":
    stdout.reconfigure(encoding="utf-8")
    run()
