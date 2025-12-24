import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # Project root (from .automation -> repo root)
README_PATH = ROOT / "README.md"

IGNORED_DIRS = {".git", "tools", "__pycache__", ".venv", "venv", "node_modules"}
THIS_SCRIPT_NAME = Path(__file__).name
IGNORED_FILES = {"README.md", THIS_SCRIPT_NAME}

HEADER = """# Developer Toys Collection

> [!NOTE]  
> To update this README, run `.automation\\update_readme.bat`.

---

A collection of useful dev toys and more.

## Table of contents

"""


def is_ignored_dir(dirname: str) -> bool:
    return dirname in IGNORED_DIRS or dirname.startswith(".")


def is_ignored_file(filename: str) -> bool:
    if filename in IGNORED_FILES:
        return True
    if filename.startswith("."):
        return True
    return False


def collect_structure():
    structure = {}
    for root, dirs, files in os.walk(ROOT):
        rel_root = Path(root).relative_to(ROOT)

        # Filter directories
        dirs[:] = [d for d in dirs if not is_ignored_dir(d)]

        # Skip root level (.) for path names
        if rel_root == Path("."):
            folder_key = None
        else:
            folder_key = str(rel_root).replace("\\", "/")

        visible_files = [f for f in files if not is_ignored_file(f)]
        if not visible_files:
            continue

        structure.setdefault(folder_key, [])
        for f in sorted(visible_files):
            structure[folder_key].append(f)

    return structure


def make_readme(structure):
    lines = [HEADER]

    # First, sort folders at the top level
    top_level_folders = sorted(
        [k for k in structure.keys() if k is not None and "/" not in k]
    )

    # Files directly in the root 
    if None in structure:
        for filename in sorted(structure[None]):
            rel_path = filename
            lines.append(f"- [{filename}]({rel_path})")
        lines.append("")

    for folder in top_level_folders:
        folder_display = folder  
        
        # Make all top-level folders collapsible
        lines.append(f"- <details>")
        lines.append(f"  <summary><strong>{folder_display}/</strong></summary>")
        lines.append("")

        # Subfolders 
        subfolders = sorted(
            [k for k in structure.keys() if k is not None and k.startswith(folder + "/")]
        )

        # Files directly in the folder
        if structure[folder]:
            for filename in structure[folder]:
                rel_path = f"{folder}/{filename}"
                lines.append(f"  - [{filename}]({rel_path})")
            lines.append("")

        # Make all subfolders collapsible 
        for sub in subfolders:
            sub_rel = sub[len(folder) + 1 :]
            lines.append(f"  - <details>")
            lines.append(f"    <summary><strong>{sub_rel}/</strong></summary>")
            lines.append("")
            for filename in structure[sub]:
                rel_path = f"{sub}/{filename}"
                lines.append(f"    - [{filename}]({rel_path})")
            lines.append("")
            lines.append(f"  </details>")

        lines.append("</details>")
        lines.append("")

    content = "\n".join(lines).rstrip() + "\n"
    README_PATH.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    s = collect_structure()
    make_readme(s)
