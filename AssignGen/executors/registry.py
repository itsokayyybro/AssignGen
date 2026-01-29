from executors.csharp import CSharpExecutor
from executors.python_exec import PythonExecutor
from executors.cpp import CppExecutor

EXECUTOR_REGISTRY = {
    "csharp": CSharpExecutor,
    "python": PythonExecutor,
    "cpp": CppExecutor,
}
