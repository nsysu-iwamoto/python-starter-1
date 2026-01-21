# uv Project Management Guide

This guide introduces `uv`, a modern Python package and project manager.

*This is OPTIONAL and intended for motivated students who want to learn modern Python development tools.*

## What is uv?

`uv` is a fast Python package manager written in Rust. It's a modern alternative to `pip` and `venv` that is:

- **Much faster** than pip (10-100x faster)
- **Easier to use** for managing projects
- **More reliable** with dependency resolution

## Installation

See [the official installation guide](https://docs.astral.sh/uv/#installation).

After installation, verify it works:

```bash
uv --version
```

## Using uv with this Project

This project includes a `pyproject.toml` file that allows uv to manage everything automatically.

### 1. Sync dependencies

```bash
uv sync
```

This command:

- creates a virtual environment automatically
- installs all required packages
- creates a `uv.lock` file for reproducibility (but you don't need to worry about this)

### 2. Run commands in the environment

Now you replace any command (like `python`) with `uv run <command>`.

```bash
uv run python task01_hello.py
uv run pytest
uv run pytest tests/test_02_iteration.py
```

The `uv run` command automatically uses the project's virtual environment.

#### 3. Add new packages (if needed)

```bash
uv add numpy          # Add numpy to dependencies
```

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

## Additional Resources

- [uv Official Documentation](https://docs.astral.sh/uv/)
- [uv GitHub Repository](https://github.com/astral-sh/uv)
- [Why uv is Fast](https://astral.sh/blog/uv)
