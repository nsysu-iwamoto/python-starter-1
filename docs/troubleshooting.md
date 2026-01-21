# Troubleshooting Guide

Common problems and their solutions.

---

## Running Python Code

### Problem: `python: command not found`

**Solution**: Try `python3` instead:

```bash
python3 task01_hello.py
python3 -m pytest
```

Or install Python from [python.org](https://www.python.org/downloads/).

---

### Problem: "My code runs but prints nothing"

**Cause**: You might be using `pass` or forgot to add `print()`.

**Solution**: 

1. Check that you removed the `pass` statement
2. Make sure you added `print()` statements
3. Example:

   ```python
   # ❌ Wrong - does nothing
   def hello_world():
       pass
   
   # ✅ Correct - prints message
   def hello_world():
       print("Hello, World!")
   ```

---

### Problem: "My output has extra spaces or blank lines"

**Cause**: You might be printing extra newlines or spaces.

**Solution**: 

- Use `print(value)` not `print(value + "\n")`
- Don't add extra `print()` statements with no arguments

```python
# ❌ Wrong - adds extra blank line
print("Hello")
print()
print("World")

# ✅ Correct - one item per line
print("Hello")
print("World")
```

---

## Testing Issues

### Problem: `ModuleNotFoundError: No module named 'pytest'`

**Solution**: Install pytest:

```bash
pip install pytest pytest-timeout
# or
pip3 install pytest pytest-timeout
```

---

### Problem: "Tests are failing but my code looks correct"

**Steps to debug**:

1. **Run your code manually** to see what it prints:

   ```bash
   python task01_hello.py
   ```

2. **Check the error message carefully** - it tells you what's wrong:

   ```
   AssertionError: assert 'hello, world!' == 'Hello, World!'
                        ^ lowercase 'h'         ^ uppercase 'H'
   ```

3. **Common issues**:
   - Wrong capitalization: `hello` vs `Hello`
   - Missing punctuation: `Hello World` vs `Hello, World!`
   - Extra/missing spaces
   - Extra blank lines in output

---

### Problem: "Test says function not found"

**Error message**: `AssertionError: Function hello_world not implemented.`

**Cause**: Function name is wrong or function doesn't exist.

**Solution**:

1. Check spelling: `hello_world` not `helloworld` or `hello_World`
2. Make sure function is defined: `def hello_world():`
3. Check indentation - function must start at left edge

```python
# ❌ Wrong - indented
    def hello_world():
        print("Hello")

# ✅ Correct - no indentation
def hello_world():
    print("Hello")
```

---

## Code Errors

### Problem: `SyntaxError: invalid syntax`

**Common causes**:

1. **Missing colon** after `if`, `for`, `def`:

   ```python
   # ❌ Wrong
   def hello_world()
       print("Hello")
   
   # ✅ Correct
   def hello_world():
       print("Hello")
   ```

2. **Wrong quotes**:

   ```python
   # ❌ Wrong - unmatched quotes
   print("Hello, World!')
   
   # ✅ Correct - matching quotes
   print("Hello, World!")
   ```

3. **Missing parentheses**:

   ```python
   # ❌ Wrong
   print "Hello"
   
   # ✅ Correct
   print("Hello")
   ```

---

### Problem: `IndentationError`

**Cause**: Python uses spaces/tabs to show code structure.

**Solution**: Use 4 spaces for each level of indentation.

```python
# ❌ Wrong - no indentation
def hello_world():
print("Hello")

# ✅ Correct - 4 spaces
def hello_world():
    print("Hello")

# ❌ Wrong - inconsistent
def fibonacci(n):
    a = 1
  b = 1  # Only 2 spaces - ERROR!

# ✅ Correct - consistent 4 spaces
def fibonacci(n):
    a = 1
    b = 1
```

**Tip**: Most editors can convert Tab key to 4 spaces automatically.

---

### Problem: `NameError: name 'x' is not defined`

**Cause**: Using a variable before defining it.

**Solution**: Define the variable first:

```python
# ❌ Wrong
print(x)  # x doesn't exist yet!

# ✅ Correct
x = 5
print(x)
```

---

### Problem: `TypeError: can only concatenate str (not "int") to str`

**Cause**: Mixing strings and numbers in wrong way.

**Solution**: 

1. **Use f-strings** (recommended):

   ```python
   n = 5
   print(f"The number is {n}")
   ```

2. **Convert number to string**:

   ```python
   n = 5
   print("The number is " + str(n))
   ```

---

### Problem: Input doesn't work / `TypeError: 'str' object is not callable`

**Cause 1**: Forgot to convert `input()` to integer:

```python
# ❌ Wrong - input is a string
n = input("Enter number: ")
for i in range(n):  # ERROR! range needs int, not str

# ✅ Correct - convert to int
n = int(input("Enter number: "))
for i in range(n):
```

**Cause 2**: You named a variable `input`:

```python
# ❌ Wrong - 'input' is now a variable, not a function
input = "some value"
n = input("Enter number:")  # ERROR!

# ✅ Correct - use different variable name
user_input = "some value"
n = input("Enter number:")
```

---

## Git Issues

### Problem: `Permission denied` when pushing

**Solution**: Set up GitHub authentication:

- Use a personal access token (recommended for HTTPS)
- Or use SSH keys

See: [GitHub Authentication Guide](https://docs.github.com/en/authentication)

---

### Problem: `git push` does nothing / says "Everything up-to-date"

**Cause**: You forgot to commit your changes.

**Solution**: Always commit before pushing:

```bash
git add .
git commit -m "Your message here"
git push
```

---

### Problem: "I want to undo my changes"

**To undo changes to a file** (before commit):

```bash
git checkout -- task01_hello.py
```

⚠️ **Warning**: This permanently deletes your changes!

**To undo last commit** (keep the changes in your files):

```bash
git reset HEAD~1
```

---

## Output Formatting Issues

### Problem: "My numbers print on one line, not separate lines"

**Cause**: Using wrong separator.

```python
# ❌ Wrong - prints on one line
for i in range(5):
    print(i, end=" ")  # Prints: 0 1 2 3 4

# ✅ Correct - prints on separate lines  
for i in range(5):
    print(i)  # Prints each number on new line
```

---

### Problem: "My range() is wrong"

**Remember**: `range(start, stop)` goes from `start` to `stop - 1` (not including `stop`).

```python
# To print 1 to 10:
for i in range(1, 11):  # 11, not 10!
    print(i)

# Common mistakes:
range(1, 10)   # Gives 1-9 (missing 10)
range(10)      # Gives 0-9 (starts at 0)
range(1, 11)   # ✅ Correct: 1-10
```

---

## Still Having Problems?

1. **Read the error message** - Python tells you what's wrong and where!
2. **Check the line number** in the error message
3. **Compare with examples** in the task instructions
4. **Test with simple values** first (like `n=3`) before large values
5. **Use print() to debug**:

   ```python
   print(f"Debug: n = {n}")
   print(f"Debug: i = {i}")
   ```

6. **Ask for help**:
   - Your instructor
   - Classmates
   - Python documentation
   - Online Python communities

---

## Debugging Tips

### Add temporary print statements:

```python
def fizzbuzz(n):
    for i in range(1, n+1):
        print(f"Debug: checking {i}")  # Temporary debug line
        if i % 15 == 0:
            print("FizzBuzz")
        # ... rest of code
```

Remember to **remove debug prints** before submitting!

### Test with small numbers:

```python
# Instead of testing with 100
fizzbuzz(5)  # Easier to check if correct
```

### Run one test at a time:

```bash
# Instead of running all tests
python -m pytest tests/test_01_hello.py::test_hello_world -v
```

---

## Common Mistakes Summary

| Mistake | Correct |
|---------|---------|
| `print "Hello"` | `print("Hello")` |
| `if x > 5` (no colon) | `if x > 5:` |
| `range(1, 10)` for 1-10 | `range(1, 11)` |
| Comparing with `=` | Use `==` for comparison |
| `n = input()` for number | `n = int(input())` |
| Inconsistent indentation | Use 4 spaces everywhere |

---

Remember: **Everyone makes mistakes!** Programming is about finding and fixing them. You're doing great! 🚀
