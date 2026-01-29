import sys
from pathlib import Path

from scanner import scan_assignment
from executors.registry import EXECUTOR_REGISTRY
from capture_runner import capture_program_output
from doc_builder import build_document


def run_pipeline(assignment_path: Path):
    programs = scan_assignment(str(assignment_path))

    for program in programs:
        executor_cls = EXECUTOR_REGISTRY[program["language"]]
        executor = executor_cls(program)

        executor.build()
        executor.run()

        capture_program_output(program)

    output_doc = assignment_path.name + ".docx"
    build_document(programs, output_path=output_doc)

    print(f"\n✅ Generated: {output_doc}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <assignment_folder>")
        sys.exit(1)

    assignment_path = Path(sys.argv[1]).resolve()

    if not assignment_path.exists():
        print(f"❌ Folder not found: {assignment_path}")
        sys.exit(1)

    run_pipeline(assignment_path)


if __name__ == "__main__":
    main()
