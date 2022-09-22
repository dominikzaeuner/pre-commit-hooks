#!/usr/bin/env python3
"""Wrapper script for clazy."""
import sys
from typing import List

from .utils import StaticAnalyzerCmd


class ClazyCmd(StaticAnalyzerCmd):
    """Class for the clazy command."""

    command = "clazy"
    lookbehind = "clazy version "

    def __init__(self, args: List[str]):
        super().__init__(self.command, self.lookbehind, args)
        self.parse_args(args)

    def run(self):
        """Run clazy only compiling outputting to /dev/null."""
        for filename in self.files:
            self.run_command(self.args + ['-c', filename, '-o/dev/null'])
            self.exit_on_error()


def main(argv: List[str] = sys.argv):
    cmd = ClazyCmd(argv)
    cmd.run()


if __name__ == "__main__":
    main()
