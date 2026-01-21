# python-starter-1

An Introductory exercise for numerical analysis, prepared for Sho's lecture course “[Math and Coding in Physics](https://www2.nsysu.edu.tw/iwamoto/physmath2.html)”.

---

## 🚀 Quick Start

**New to this course? Start here!**

👉 **[Getting Started Guide](docs/getting_started.md)** - Complete setup instructions

### Essential Guides

- 📚 [Getting Started Guide](docs/getting_started.md) - Setup and how to complete tasks
- 🔧 [Git Introduction](docs/git_intro.md) - Learn Git basics
- ⚡ [uv Guide](docs/uv_guide.md) - **Optional:** Modern tools for motivated students

---

## Tasks

- [ ] 1. [Hello, World!](task01_hello.md) - Basic functions and output
- [ ] 2. [Iteration](task02_iteration.md) - Loops and user input
- [ ] 3. [FizzBuzz](task03_fizzbuzz.md) - Conditionals and logic
- [ ] 4. [Fibonacci sequence](task04_fibonacci.md) - Combining concepts

Each task includes:

- Basic problems (required)
- Optional problems (advanced, for extra learning)

---

## How to Work on Tasks

### Method 1: Edit on GitHub (Simplest)

You can edit `.py` files directly on GitHub through your web browser.

### Method 2: Work on Your Computer (Recommended)

**This is the recommended approach for learning Git and proper development workflow.**

1. **Clone** this repository to your computer
2. **Edit** files on your computer
3. **Test** your code locally
4. **Commit** your changes
5. **Push** to GitHub

See the [Getting Started Guide](docs/getting_started.md) for detailed instructions.

---

## Testing Your Code

You may "test" your code automatically.

### Setup

To run tests on your computer, you need to install test tools:

```bash
# commands may be python3 and pip3 on your system,
python --version  # Check version >= 3.11
pip --version     # Check your pip is for correct Python version

pip install pytest pytest-timeout
```

**Detailed setup instructions:** See the [Getting Started Guide](docs/getting_started.md)

### Running Tests

```bash
# Run all tests
python -m pytest

# Run tests for a specific task
python -m pytest tests/test_01_hello.py -v

# Include optional problems
python -m pytest --optional
```

**Note:** Test codes may have bugs - you are the first testers! Please report any issues.

---

## Project Structure

```text
python-starter-1/
├── docs/                  # Documentation
│   ├── getting_started.md # Setup guide
│   ├── git_intro.md       # Git tutorial
│   └── uv_guide.md        # Optional: Modern tools
├── task*.md               # Task instructions
├── task*.py               # Your code
├── tests/                 # Test files
└── requirements.txt       # Dependencies
```

---

## Getting Help

1. Read the documentation in the [`docs/`](docs/) folder
2. Check error messages carefully
3. Ask your instructor or classmates
4. Search online for Python concepts

---

## For Motivated Students

Want to go beyond the basics?

- ⚡ Learn modern Python tools: [uv Guide](docs/uv_guide.md)
- 🎯 Complete all optional problems in each task
- 🚀 Explore Python libraries for physics: NumPy, SciPy, Matplotlib

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
