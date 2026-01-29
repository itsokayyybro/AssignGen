from scanner import scan_assignment
from executors.registry import EXECUTOR_REGISTRY


def run_assignment(path):
    programs = scan_assignment(path)

    for program in programs:
        executor_cls = EXECUTOR_REGISTRY[program["language"]]
        executor = executor_cls(program)

        executor.build()
        executor.run()

        print(f"\n=== {program['name']} ({program['language']}) ===")
        print(program["stdout"])


if __name__ == "__main__":
    run_assignment("Hello_not_world")
