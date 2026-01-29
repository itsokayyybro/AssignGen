from executors.base import BaseExecutor


class PythonExecutor(BaseExecutor):

    def build(self):
        self.program["build_command"] = None

    def run(self):
        main_file = next(
            (f for f in self.program["source_files"] if f.name == "main.py"),
            self.program["source_files"][0]
        )

        self.program["run_command"] = ["python", main_file.name]
        result = self._execute(self.program["run_command"])

        self.program["stdout"] = result.stdout
        self.program["stderr"] = result.stderr
        self.program["return_code"] = result.returncode
