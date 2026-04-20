"""shushu command-line entry point."""

from __future__ import annotations

import argparse
from typing import Sequence

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="shushu", description="shushu CLI")
    parser.add_argument("--version", action="version", version=f"shushu {__version__}")
    parser.set_defaults(func=_default)
    return parser


def _default(_args: argparse.Namespace) -> int:
    print(f"shushu {__version__}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
