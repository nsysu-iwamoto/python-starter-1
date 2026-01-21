# UV Project Management Guide

## ⚠️ Important Notice

**This guide is OPTIONAL and intended for motivated students who want to learn modern Python development tools.**

**For most students: Please use the standard pip method described in the [Getting Started Guide](getting_started.md).**

---

This guide introduces `uv`, a modern Python package and project manager.

## What is uv?

`uv` is a fast Python package manager written in Rust. It's an alternative to `pip` and `venv` that is:

- **Much faster** than pip (10-100x faster)
- **Easier to use** for managing projects
- **More reliable** with dependency resolution

## Installation

### On macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### On Windows:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Alternative: Using pip
```bash
pip install uv
```

After installation, verify it works:
```bash
uv --version
```

## Using uv with this Project

### Option 1: Quick Start (Recommended for Beginners)

Instead of using `pip`, you can use `uv pip`:

```bash
# Install dependencies
uv pip install -r requirements.txt

# Run tests
python -m pytest
```

This is the **easiest way** to get started - it works exactly like pip but faster!

### Option 2: Using uv for Full Project Management (Advanced)

For students who want to learn modern Python development practices.

This project includes a `pyproject.toml` file that allows uv to manage everything automatically.

#### 1. Sync dependencies
```bash
uv sync
```

This command:
- Creates a virtual environment automatically
- Installs all required packages
- Creates a `uv.lock` file for reproducibility

#### 2. Run commands in the environment
```bash
uv run python task01_hello.py
uv run pytest
```

The `uv run` command automatically uses the project's virtual environment.

#### 3. Add new packages (if needed)
```bash
uv add numpy          # Add numpy to dependencies
uv add --dev mypy     # Add mypy as development dependency
```

## Comparison: pip vs uv

### Traditional way with pip:
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run code
python task01_hello.py
```

### Modern way with uv:
```bash
# One command does everything!
uv sync

# Run code (no activation needed)
uv run python task01_hello.py
```

## Advantages of uv

1. **Speed**: Much faster installation times
2. **Simplicity**: No need to manually manage virtual environments
3. **Reproducibility**: `uv.lock` ensures everyone has the same dependencies
4. **Modern**: Follows current Python best practices

## Commands Cheat Sheet

| Task | Traditional | With uv |
|------|-------------|---------|
| Install dependencies | `pip install -r requirements.txt` | `uv sync` |
| Run Python script | `python script.py` | `uv run python script.py` |
| Run tests | `python -m pytest` | `uv run pytest` |
| Add package | `pip install numpy` | `uv add numpy` |
| Remove package | `pip uninstall numpy` | `uv remove numpy` |

## Understanding pyproject.toml

The `pyproject.toml` file is the modern way to configure Python projects.

```toml
[project]
name = "python-starter-1"
version = "0.1.0"
description = "Python self-study exercises for physics students"
requires-python = ">=3.8"

dependencies = [
    "pytest>=7.0.0",
    "pytest-timeout>=2.0.0",
]
```

Key sections:
- `[project]`: Project metadata
- `dependencies`: Required packages
- `requires-python`: Minimum Python version

## When to Use What

### Use `uv pip` if:
- You're just getting started
- You want something familiar (like pip)
- You only need faster package installation

### Use `uv sync` and `uv run` if:
- You want to learn modern Python workflows
- You're working on larger projects
- You value reproducibility

## Troubleshooting

### Problem: `uv: command not found`
**Solution**: uv may not be in your PATH. Try:
```bash
# Check if uv is installed
which uv

# If not found, reinstall or add to PATH
```

### Problem: `uv sync` fails
**Solution**: Make sure you have Python 3.8 or higher:
```bash
python --version
```

### Problem: Want to use traditional venv instead
**Solution**: That's perfectly fine! uv is optional. You can use the traditional pip method.

## Additional Resources

- [uv Official Documentation](https://docs.astral.sh/uv/)
- [uv GitHub Repository](https://github.com/astral-sh/uv)
- [Why uv is Fast](https://astral.sh/blog/uv)

## Summary

- `uv` is a **faster, modern alternative** to pip
- **This is completely OPTIONAL** - use it only if you're interested!
- Most students should stick with the standard pip method
- For motivated students: You can start simple with `uv pip`
- Advanced users can use `uv sync` for full project management
