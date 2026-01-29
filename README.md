# AssignGen

<p align="center">
  <strong>🚀 Automated Assignment Documentation Generator</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/itsokayyybro/AssignGen?style=for-the-badge&logo=github&color=yellow" alt="Stars">
  <img src="https://img.shields.io/github/forks/itsokayyybro/AssignGen?style=for-the-badge&logo=github&color=blue" alt="Forks">
  <img src="https://img.shields.io/github/watchers/itsokayyybro/AssignGen?style=for-the-badge&logo=github&color=green" alt="Watchers">
  <img src="https://img.shields.io/github/license/itsokayyybro/AssignGen?style=for-the-badge&color=orange" alt="License">
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/itsokayyybro/AssignGen?style=for-the-badge&logo=git&color=purple" alt="Last Commit">
  <img src="https://img.shields.io/github/repo-size/itsokayyybro/AssignGen?style=for-the-badge&logo=github&color=teal" alt="Repo Size">
  <img src="https://img.shields.io/github/issues/itsokayyybro/AssignGen?style=for-the-badge&logo=github&color=red" alt="Issues">
  <img src="https://img.shields.io/github/issues-pr/itsokayyybro/AssignGen?style=for-the-badge&logo=github&color=cyan" alt="Pull Requests">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/C%23-.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white" alt="C#">
  <img src="https://img.shields.io/badge/Word-Document-2B579A?style=for-the-badge&logo=microsoftword&logoColor=white" alt="Word">
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#supported-languages">Languages</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#project-structure">Structure</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

## 📖 Overview

**AssignGen** is a powerful command-line tool that automatically generates professional Word documents (`.docx`) from your programming assignments. It scans your project folder, compiles and executes code, captures the output as images, and bundles everything into a beautifully formatted document — perfect for academic submissions!

No more manual copy-pasting of code and screenshots. Let AssignGen handle it for you! ✨

---

## ✨ Features

- 🔍 **Auto-Detection** — Automatically scans and detects programming files in your assignment folder
- 🏗️ **Multi-Language Support** — Works with Python, C++, and C# (.NET) projects
- ⚡ **Build & Execute** — Compiles and runs your programs automatically
- 📸 **Output Capture** — Captures program output and renders it as styled images
- 📄 **Document Generation** — Creates professional Word documents with:
  - Program titles and language labels
  - Syntax-highlighted source code (Consolas font)
  - Execution output screenshots
  - Clean page breaks between programs
- 🔌 **Extensible Architecture** — Easy to add support for new programming languages

---

## 🌐 Supported Languages

| Language | File Extension | Build Tool | Notes |
|----------|---------------|------------|-------|
| **Python** | `.py` | None | Looks for `main.py` first, falls back to first file |
| **C++** | `.cpp` | `g++` | Compiles all `.cpp` files together |
| **C# (.NET)** | `.cs` / `.csproj` | `dotnet` | Detects `.csproj` project files |

---

## 📦 Installation

### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.8+**
- **pip** (Python package manager)

#### For C++ Support:
```bash
# Ubuntu/Debian
sudo apt install g++

# macOS
xcode-select --install

# Windows
# Install MinGW or use Visual Studio Build Tools
```

#### For C# Support:
```bash
# Install .NET SDK from https://dotnet.microsoft.com/download
dotnet --version
```

### Install AssignGen

1. **Clone the repository:**
   ```bash
   git clone https://github.com/itsokayyybro/AssignGen.git
   cd AssignGen
   ```

2. **Install Python dependencies:**
   ```bash
   pip install python-docx Pillow
   ```

---

## 🚀 Usage

### Basic Usage

```bash
cd AssignGen
python main.py <path-to-assignment-folder>
```

### Example

```bash
# Generate documentation for an assignment folder
python main.py ../assignment

# Output: assignment.docx
```

### Sample Folder Structure

```
my_assignment/
├── problem1/
│   └── main.py
├── problem2/
│   ├── Program.cs
│   └── problem2.csproj
└── problem3/
    └── solution.cpp
```

Running `python main.py my_assignment` will:
1. ✅ Scan for all supported program files
2. ✅ Build and execute each program
3. ✅ Capture outputs as images
4. ✅ Generate `my_assignment.docx` with all code and outputs

---

## 📂 Project Structure

```
AssignGen/
├── AssignGen/
│   ├── main.py              # Entry point - CLI interface
│   ├── scanner.py           # Scans folders for supported programs
│   ├── doc_builder.py       # Generates Word documents
│   ├── capture_runner.py    # Coordinates output capture
│   ├── output_capture.py    # Renders text output to images
│   ├── executors/
│   │   ├── base.py          # Abstract base executor class
│   │   ├── registry.py      # Language-to-executor mapping
│   │   ├── python_exec.py   # Python executor
│   │   ├── cpp.py           # C++ executor
│   │   └── csharp.py        # C# executor
│   └── outputs/             # Generated output images
├── assignment/              # Sample assignment for testing
├── LICENSE
└── README.md
```

---

## 🔧 How It Works

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   1. SCAN       │────▶│   2. EXECUTE    │────▶│   3. CAPTURE    │
│                 │     │                 │     │                 │
│ Detect files    │     │ Build & run     │     │ Output → Image  │
│ by extension    │     │ programs        │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │   4. GENERATE   │
                                               │                 │
                                               │ Create .docx    │
                                               │ with code &     │
                                               │ outputs         │
                                               └─────────────────┘
```

1. **Scanner** (`scanner.py`) — Recursively scans the assignment folder for supported file types
2. **Executors** (`executors/`) — Language-specific handlers that build and run programs
3. **Output Capture** (`output_capture.py`) — Renders console output as styled PNG images
4. **Document Builder** (`doc_builder.py`) — Assembles everything into a Word document

---

## 🛠️ Adding New Language Support

To add support for a new programming language:

1. **Create a new executor** in `AssignGen/executors/`:

   ```python
   # AssignGen/executors/java.py
   from executors.base import BaseExecutor

   class JavaExecutor(BaseExecutor):
       def build(self):
           self.program["build_command"] = ["javac", "Main.java"]
           self._execute(self.program["build_command"])

       def run(self):
           self.program["run_command"] = ["java", "Main"]
           result = self._execute(self.program["run_command"])
           self.program["stdout"] = result.stdout
           self.program["stderr"] = result.stderr
           self.program["return_code"] = result.returncode
   ```

2. **Register the executor** in `AssignGen/executors/registry.py`:

   ```python
   from executors.java import JavaExecutor

   EXECUTOR_REGISTRY = {
       # ... existing executors
       "java": JavaExecutor,
   }
   ```

3. **Update the scanner** in `AssignGen/scanner.py` to detect the new file type.

---

## ⚙️ Configuration

### Timeout Settings

By default, programs have a **5-second timeout**. To modify this, update the executor initialization in `base.py`:

```python
class BaseExecutor(ABC):
    def __init__(self, program, timeout=10):  # Change timeout here
        ...
```

### Output Image Styling

Customize the output image appearance in `output_capture.py`:

```python
render_output_to_image(
    text,
    output_path,
    width=900,           # Image width
    padding=20,          # Padding around text
    bg_color=(30, 30, 30),        # Dark background
    text_color=(230, 230, 230)    # Light text
)
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError: Folder not found` | Ensure the assignment path exists and is correct |
| `g++: command not found` | Install GCC/G++ compiler for C++ support |
| `dotnet: command not found` | Install .NET SDK for C# support |
| `ModuleNotFoundError: No module named 'docx'` | Run `pip install python-docx` |
| `ModuleNotFoundError: No module named 'PIL'` | Run `pip install Pillow` |
| Program timeout | Increase the timeout in `BaseExecutor` |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contributions

- [ ] Add Java support
- [ ] Add JavaScript/Node.js support
- [ ] Add syntax highlighting in Word documents
- [ ] Add PDF export option
- [ ] Add interactive input support for programs
- [ ] Add GUI interface
- [ ] Add support for test cases

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Om Prajapati**

- GitHub: [@itsokayyybro](https://github.com/itsokayyybro)

---

## ⭐ Show Your Support

If this project helped you, give it a ⭐ on GitHub!

---

<p align="center">
  Made with ❤️ for students everywhere
</p>