from executors.base import BaseExecutor


class CSharpExecutor(BaseExecutor):

    def build(self):
        self.program["build_command"] = ["dotnet", "build"]
        self._execute(self.program["build_command"])

    def run(self):
        self.program["run_command"] = ["dotnet", "run", "--no-build"]
        result = self._execute(self.program["run_command"])

        self.program["stdout"] = result.stdout
        self.program["stderr"] = result.stderr
        self.program["return_code"] = result.returncode
