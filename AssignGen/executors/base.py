import subprocess
from abc import ABC, abstractmethod


class BaseExecutor(ABC):
    def __init__(self, program, timeout=5):
        self.program = program
        self.timeout = timeout

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def _execute(self, command):
        return subprocess.run(
            command,
            cwd=self.program["root_path"],
            capture_output=True,
            text=True,
            timeout=self.timeout
        )
