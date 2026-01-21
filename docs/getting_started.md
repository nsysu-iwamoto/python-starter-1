# Getting Started Guide

Welcome to the Python Self-Study Course for Physics Students!

This guide will help you set up your environment and start working on the tasks.

## Prerequisites

Before starting, you should have:

1. **Python 3.8 or higher** installed on your computer
   - Check: `python --version` or `python3 --version`
   - Download from: https://www.python.org/downloads/

2. **Git** installed on your computer
   - Check: `git --version`
   - Download from: https://git-scm.com/downloads

3. A **GitHub account**
   - Sign up at: https://github.com/

4. A **text editor** or IDE
   - Recommended: [Visual Studio Code](https://code.visualstudio.com/)
   - Alternatives: PyCharm, Sublime Text, etc.

## Setup Steps

### Step 1: Clone the Repository

First, you need to download this repository to your computer.

1. Open your terminal (Terminal on Mac/Linux, Command Prompt or PowerShell on Windows)
2. Navigate to where you want to save the project:
   ```bash
   cd ~/Documents  # Or any folder you prefer
   ```
3. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd python-starter-1
   ```

**New to Git?** Check out our [Git Introduction Guide](git_intro.md)!

### Step 2: Install Dependencies

You need to install testing tools to check your work.

#### Standard Method: Using pip (Recommended)

**Most students should use this method:**

```bash
# Optional but recommended: Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Mac/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Advanced Alternative: Using uv (Optional - For Motivated Students)

**⚠️ This is optional and only for students who want to learn modern tools!**

If you're interested in learning cutting-edge Python development practices, see our [UV Project Management Guide](uv_guide.md) for installation and usage.

### Step 3: Verify Installation

Test that everything is working:

```bash
python -m pytest --version
```

You should see pytest version information.

## Understanding the Project Structure

```
python-starter-1/
├── README.md              # Overview and task list
├── docs/                  # Documentation
│   ├── getting_started.md # This file
│   ├── git_intro.md       # Git introduction
│   └── uv_guide.md        # UV guide
├── task01_hello.md        # Task 1 instructions
├── task01_hello.py        # Your code for task 1
├── task02_iteration.md    # Task 2 instructions
├── task02_iteration.py    # Your code for task 2
├── task03_fizzbuzz.md     # Task 3 instructions
├── task03_fizzbuzz.py     # Your code for task 3
├── task04_fibonacci.md    # Task 4 instructions
├── task04_fibonacci.py    # Your code for task 4
├── tests/                 # Test files
│   ├── test_01_hello.py   # Tests for task 1
│   ├── test_02_iteration.py
│   ├── test_03_fizzbuzz.py
│   └── test_04_fibonacci.py
└── requirements.txt       # Python dependencies
```

## How to Complete Tasks

### Basic Workflow

For each task (e.g., Task 01):

1. **Read the instructions**
   ```bash
   # Open task01_hello.md in your text editor
   ```

2. **Edit the Python file**
   ```bash
   # Edit task01_hello.py
   # Complete the function according to the instructions
   ```

3. **Run your code**
   ```bash
   python task01_hello.py
   ```

4. **Test your code**
   ```bash
   # Run tests for this task
   python -m pytest tests/test_01_hello.py -v
   ```

5. **Commit your changes**
   ```bash
   git add task01_hello.py
   git commit -m "Complete task 01: hello world"
   ```

6. **Push to GitHub**
   ```bash
   git push
   ```

### Testing Your Work

#### Run all tests
```bash
python -m pytest
```

#### Run tests for a specific task
```bash
python -m pytest tests/test_01_hello.py -v
```

#### Run tests including optional problems
```bash
python -m pytest --optional
```

#### Understanding test output

- ✅ **PASSED**: Your code works correctly!
- ❌ **FAILED**: Something is wrong. Read the error message carefully.
- **⊘ SKIPPED**: Test was not run (e.g., optional problems)

## Working on Tasks

### Task Order

We recommend completing tasks in order:

1. **Task 01: Hello World** - Learn basic function and print
2. **Task 02: Iteration** - Learn loops and user input
3. **Task 03: FizzBuzz** - Learn conditionals and logic
4. **Task 04: Fibonacci** - Combine everything

### Optional Problems

Each task has optional (advanced) problems marked as "(optional)".

- These are **challenging** and not required
- Only attempt them if you have completed the basic task
- Great for learning more advanced Python concepts!

## Tips for Success

### 1. Read Error Messages Carefully
Error messages tell you what went wrong. Don't ignore them!

### 2. Test Frequently
Test your code often, not just at the end.

### 3. Use Print Statements for Debugging
```python
print(f"Debug: x = {x}")  # See what values variables have
```

### 4. Commit Often
Make small, frequent commits rather than one big commit.

### 5. Read Python Documentation
- Official Python docs: https://docs.python.org/3/
- Python tutorial: https://docs.python.org/3/tutorial/

### 6. Don't Copy-Paste Solutions
Type the code yourself to learn better.

## Common Issues and Solutions

### "ModuleNotFoundError: No module named 'pytest'"
**Solution**: Install dependencies (see Step 2 above)

### "python: command not found"
**Solution**: Try `python3` instead, or install Python

### Tests are failing but my code looks correct
**Solution**: 
- Read the test output carefully
- Check for typos in function names
- Make sure you're printing/returning the expected format
- Try running your code manually to see the output

### "Permission denied" when pushing to GitHub
**Solution**: Set up GitHub authentication
- Use HTTPS with a personal access token, or
- Use SSH keys
- See: https://docs.github.com/en/authentication

## Getting Help

If you're stuck:

1. **Read the error message carefully**
2. **Check the documentation in this folder**
3. **Look at the test files** to understand what's expected
4. **Search online** for Python concepts you don't understand
5. **Ask your instructor or classmates**

## Next Steps

Ready to start? Great!

1. ✅ Complete the setup steps above
2. ✅ Open `task01_hello.md`
3. ✅ Start coding!

**Good luck!** 🚀

---

## Additional Resources

- [Git Introduction](git_intro.md) - Learn Git basics
- [UV Guide](uv_guide.md) - Learn modern Python project management
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python - Python Basics](https://realpython.com/learning-paths/python-basics/)
