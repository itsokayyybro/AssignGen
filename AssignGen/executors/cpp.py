from executors.base import BaseExecutor


class CppExecutor(BaseExecutor):

    def build(self):
        output_name = self.program["name"]
        self.program["build_command"] = [
            "g++",
            *[f.name for f in self.program["source_files"]],
            "-o",
            output_name
        ]
        self._execute(self.program["build_command"])

    def run(self):
        self.program["run_command"] = [f"./{self.program['name']}"]
        result = self._execute(self.program["run_command"])

        self.program["stdout"] = result.stdout
        self.program["stderr"] = result.stderr
        self.program["return_code"] = result.returncode
