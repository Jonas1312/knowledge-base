"""
Script to update the README.md file with the tree of the project.

Only the folders are shown, not the files.
"""

import os
import sys
import urllib
from collections import deque
from pathlib import Path

"""This module provides RP Tree main module.

Source: https://github.com/realpython/rptree
"""


PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


def dir_path_to_str(path: Path, linkify: bool) -> str:
    """Convert a directory path to a string.

    If linkify is True, the path will be converted to a markdown link.
    """
    if not linkify:
        return path.name

    # If the directory only contains other directories (no files), we don't need to link to it.
    if all(file.is_dir() for file in path.iterdir()):
        return path.name

    # If there is only one markdown file in the directory, link to that file directly.
    # Only link to the markdown file if other files' names are in the single markdown file.
    markdown_files = list(path.glob("*.md"))
    if len(markdown_files) == 1:
        # Get the names of all the files in the directory, except the markdown file.
        filenames = [
            file.name
            for file in path.iterdir()
            if file.is_file() and file.name != markdown_files[0].name
        ]
        markdown_file_str = markdown_files[0].read_text(encoding="utf-8")
        # Check if all the filenames are in the markdown file.
        if all(
            (filename in markdown_file_str) or (urllib.parse.quote(filename) in markdown_file_str)  # type: ignore
            for filename in filenames
        ):
            return f"[{path.name}](<{markdown_files[0].as_posix()}>)"

    # Otherwise, link to the directory.
    return f"[{path.name}](<{path.as_posix()}>)"


class TreeGenerator:
    """TreeGenerator class."""

    def __init__(self, root_dir):
        self._root_dir = Path(root_dir)
        self.tree = deque()

        self.tree.append(f"{self._root_dir}<br>")  # tree head
        self._tree_body(self._root_dir)

    def _tree_body(self, directory, prefix=""):
        entries = self._prepare_entries(directory)
        last_index = len(entries) - 1
        for index, entry in enumerate(entries):
            connector = ELBOW if index == last_index else TEE
            if entry.is_dir():
                if index == 0:
                    self.tree.append(prefix + PIPE)
                self._add_directory(entry, index, last_index, prefix, connector)

    def _prepare_entries(self, directory):
        entries = sorted(directory.iterdir())
        return [entry for entry in entries if entry.is_dir()]

    def _add_directory(self, directory, index, last_index, prefix, connector):
        self.tree.append(f"{prefix}{connector} {dir_path_to_str(directory, linkify=True)}<br>")
        if index != last_index:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(directory=directory, prefix=prefix)
        if prefix := prefix.rstrip():
            self.tree.append(prefix)


header_readme = """# Knowledge Base

This is a collection of notes and resources that I have gathered over the years.

I hope that they will be useful to you.

## Table of Contents

{tree}"""


def main() -> None:
    root_dir = Path("./base")

    tree = TreeGenerator(root_dir).tree
    tree = [line for line in tree if not line.endswith("│")]
    tree = "\n".join(tree)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(header_readme.format(tree=tree))


if __name__ == "__main__":
    main()
