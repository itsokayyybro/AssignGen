from pathlib import Path
from typing import List, Dict

IGNORED_DIRS = {"bin", "obj", ".vs"}


def scan_assignment(assignment_path: str) -> List[Dict]:
    root = Path(assignment_path).resolve()
    if not root.exists():
        raise FileNotFoundError(f"{root} does not exist")

    programs = []

    # ---------- C# (.NET) projects ----------
    for csproj in root.rglob("*.csproj"):
        if any(part in IGNORED_DIRS for part in csproj.parts):
            continue

        project_root = csproj.parent
        source_files = [
            f for f in project_root.rglob("*.cs")
            if not any(p in IGNORED_DIRS for p in f.parts)
        ]

        programs.append({
            "name": csproj.stem,
            "language": "csharp",
            "root_path": project_root,
            "source_files": source_files,
            "project_file": csproj
        })

    # ---------- Python ----------
    py_files = [
        f for f in root.rglob("*.py")
        if not any(p in IGNORED_DIRS for p in f.parts)
    ]
    if py_files:
        programs.append({
            "name": f"{root.name}_python",
            "language": "python",
            "root_path": root,
            "source_files": py_files,
            "project_file": None
        })

    # ---------- C++ ----------
    cpp_files = [
        f for f in root.rglob("*.cpp")
        if not any(p in IGNORED_DIRS for p in f.parts)
    ]
    if cpp_files:
        programs.append({
            "name": f"{root.name}_cpp",
            "language": "cpp",
            "root_path": root,
            "source_files": cpp_files,
            "project_file": None
        })

    return programs
