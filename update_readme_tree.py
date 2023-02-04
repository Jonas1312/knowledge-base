"""
Script to update the README.md file with the tree of the project.

Only the folders are shown, not the files.
"""

from pathlib import Path


def dir_path_to_str(path: Path, linkify: bool) -> str:
    """Convert a directory path to a string.

    If linkify is True, the path will be converted to a markdown link.
    """
    if linkify:
        return f"[{path.name}](<{path.as_posix()}>)"
    return path.name


def get_tree(base_dir: Path, linkify: bool, is_root: bool) -> str:
    """Get the tree of the project directories and subdirectories as a string."""
    subdirs = [dir_ for dir_ in base_dir.iterdir() if dir_.is_dir()]
    level = len(base_dir.parts) - 1
    indent = "│    " * (level)
    tree = f"{dir_path_to_str(base_dir, linkify)}<br>\n" if is_root else ""
    for subdir in subdirs:
        sep = "└─── " if subdir == subdirs[-1] else "├─── "
        tree += f"{indent}{sep}{dir_path_to_str(subdir, linkify)}<br>\n"
        tree += get_tree(subdir, linkify=linkify, is_root=False)
    return tree


header_readme = """# Knowledge Base

This is a collection of notes and resources that I have gathered over the years. I hope that they will be useful to you.

## Table of Contents

{tree}"""


def main() -> None:
    tree = get_tree(base_dir=Path("./base"), linkify=True, is_root=True)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(header_readme.format(tree=tree))


if __name__ == "__main__":
    main()
