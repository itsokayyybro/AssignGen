import sys
from pathlib import Path

from scanner import scan_assignment
from executors.registry import EXECUTOR_REGISTRY
from capture_runner import capture_program_output
from doc_builder import build_document


OUTPUT_DIR = Path("WordDocuments")


def run_pipeline(assignment_path: Path):
    # ---- Ask user for document name ----
    doc_name = input(
        "\nEnter name for the Word document (without .docx): "
    ).strip()

    if not doc_name:
        print("❌ Document name cannot be empty.")
        sys.exit(1)

    # ---- Create output directory if not exists ----
    OUTPUT_DIR.mkdir(exist_ok=True)

    output_doc_path = OUTPUT_DIR / f"{doc_name}.docx"

    # ---- Scan assignment ----
    programs = scan_assignment(str(assignment_path))

    if not programs:
        print("❌ No valid C# assignment found.")
        sys.exit(1)

    # ---- Execute programs ----
    for program in programs:
        executor_cls = EXECUTOR_REGISTRY[program["language"]]
        executor = executor_cls(program)

        executor.build()
        executor.run()

        capture_program_output(program)

    # ---- Build Word document ----
    build_document(programs, output_path=output_doc_path)

    print(f"\n✅ Document generated successfully:")
    print(f"📄 {output_doc_path.resolve()}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <assignment_folder>")
        sys.exit(1)

    assignment_path = Path(sys.argv[1]).resolve()

    if not assignment_path.exists():
        print(f"❌ Assignment folder not found: {assignment_path}")
        sys.exit(1)

    run_pipeline(assignment_path)


if __name__ == "__main__":
    main()
