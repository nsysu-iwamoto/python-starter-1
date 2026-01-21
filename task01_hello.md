# Task 01: Hello World!

**Goal:** Learn how to write and call functions in Python

## Overview

In this task, you'll learn:

- How to define a function
- How to use the `print()` function
- How to run Python programs

## Task 01a (Required)

Open `task01_hello.py` and edit the file to do the following tasks.

Write a program that prints `Hello, World!` to the console.

That is, if you execute `python task01_hello.py` from the command line, the output should be:

```text
Hello, World!
```

### Rules

- You should **only modify inside** the `hello_world()` function
- Do not modify anything outside this function

### Hints

<details>
<summary>Click to see hint 1</summary>

Use the `print()` function to display text:

```python
print("your text here")
```

</details>

<details>
<summary>Click to see hint 2</summary>

Replace the `pass` statement with your code.

`pass` is a placeholder that does nothing.
</details>

## Task 01b (Optional)

Add a function `hello_world_three_times()` that prints `Hello, World!` three times.

Here, try to print them in different manners. For example, you can use:

- "f-string" formatting (e.g., `f"Hello, {name}!"`)
- String concatenation operator (e.g., `"Hello" + ", " + "World!"`)
- Other more advanced ways

You also need to modify "the main part" of the file (the `if __name__ == "__main__":` section).

## Task 01c (Optional)

Now you want to customize how many times it prints.

Add a function `hello_world_n_times()` that:

1. First asks the user how many times it should print `Hello, World!`
2. Then prints it that many times

<details>
<summary>Click to see hint</summary>

You may see `task02_iteration.py` for how to ask for user inputs.

Use the `input()` function and `for` loop.
</details>

### Example Interaction

```text
How many times? 5
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
```

## Common Mistakes

1. **Forgetting the quotes** around the string
   - ❌ `print(Hello, World!)`
   - ✅ `print("Hello, World!")`

2. **Wrong capitalization**
   - ❌ `print("hello, world!")` (lowercase 'h' and 'w')
   - ✅ `print("Hello, World!")` (uppercase 'H' and 'W')

3. **Wrong punctuation**
   - ❌ `print("Hello World")` (missing comma)
   - ✅ `print("Hello, World!")` (has comma and exclamation mark)

## Need Help?

- Make sure you understand what functions are
- Read error messages carefully
- Try running your code to see the output
- See the [Getting Started Guide](docs/getting_started.md) for more help
