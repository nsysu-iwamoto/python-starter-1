# Task 02: Iteration

**Goal:** Learn how to use loops and get user input

---

## Overview

In this task, you'll learn:
- How to use `for` loops
- How to use the `range()` function
- How to get user input with `input()`

---

## Task 02a (Required)

### Instructions

Open `task02_iteration.py` and edit the file to do the following tasks.

The function `show_one_to_ten()` currently shows numbers from 0 to 5 (which is incorrect).

**Fix the function so it prints numbers from 1 to 10.**

### Current Output (Wrong)

```
0
1
2
3
4
5
```

### Expected Output (Correct)

```
1
2
3
4
5
6
7
8
9
10
```

### Hints

<details>
<summary>Click to see hint 1</summary>

The `range()` function has the syntax:

```python
range(start, stop)  # Generates numbers from start to stop-1
```

For example:
- `range(0, 5)` gives: 0, 1, 2, 3, 4
- `range(1, 6)` gives: 1, 2, 3, 4, 5
</details>

<details>
<summary>Click to see hint 2</summary>

To get numbers 1 to 10, you need:

```python
range(1, 11)  # 11 because stop is exclusive (excluded)
```
</details>

### How to Test

```bash
# Run your code
python task02_iteration.py

# Run the test
python -m pytest tests/test_02_iteration.py::test_show_one_to_ten -v
```

---

## Task 02b (Required)

### Instructions

Complete the function `show_one_to_n()` so that it:

1. First asks the user to enter a number `n`
2. Then displays numbers from 1 to `n`

### Example Interaction

```
Enter a number: 5
1
2
3
4
5
```

### Hints

<details>
<summary>Click to see hint 1</summary>

Use the `input()` function to get user input:

```python
user_input = input("Enter a number: ")
```

⚠️ **Important:** `input()` returns a string, so you need to convert it to an integer!

```python
n = int(user_input)
```
</details>

<details>
<summary>Click to see hint 2</summary>

You can combine input and conversion in one line:

```python
n = int(input("Enter a number: "))
```
</details>

---

## Task 02c (Optional)

### Instructions

Add a function `show_one_to_n_ordinal()`, which is the same as `show_one_to_n()` but displays the numbers as ordinal numbers.

Namely, the output should be:

```
Enter a number: 4
1st
2nd
3rd
4th
```

### Hints

<details>
<summary>Click to see hint</summary>

You need to add suffixes based on the number:

**Rules for ordinal numbers:**

1. Numbers ending in 1 → add "st" (1st, 21st, 31st, ...)
2. Numbers ending in 2 → add "nd" (2nd, 22nd, 32nd, ...)
3. Numbers ending in 3 → add "rd" (3rd, 23rd, 33rd, ...)
4. All other numbers → add "th" (4th, 5th, 6th, 7th, 8th, 9th, 10th, ...)

**⚠️ Important exceptions:**

- 11 → 11th (NOT 11st)
- 12 → 12th (NOT 12nd)
- 13 → 13th (NOT 13rd)

**Why?** Numbers 11, 12, 13 are special cases. Even though they end in 1, 2, 3, they use "th".

**Examples:**
- 1 → 1st ✅
- 11 → 11th ✅ (exception!)
- 21 → 21st ✅
- 12 → 12th ✅ (exception!)
- 22 → 22nd ✅

You can use `if-elif-else` statements and the modulo operator `%` to check the last digit.

</details>

---

## Understanding Loops

### The `for` loop syntax

```python
for variable in sequence:
    # code to repeat
```

### The `range()` function

```python
range(stop)          # 0 to stop-1
range(start, stop)   # start to stop-1
range(start, stop, step)  # start to stop-1, incrementing by step
```

Examples:
```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

---

## Common Mistakes

1. **Forgetting to convert input to integer**
   - ❌ `n = input("Enter: ")` then using `n` in `range()`
   - ✅ `n = int(input("Enter: "))`

2. **Wrong range boundaries**
   - ❌ `range(1, 10)` for numbers 1 to 10 (gives 1 to 9)
   - ✅ `range(1, 11)` for numbers 1 to 10

3. **Forgetting the colon** after the `for` statement
   - ❌ `for i in range(10)`
   - ✅ `for i in range(10):`

---

## Need Help?

- Review Python loop syntax
- Test with small numbers first
- Use `print()` to debug
- See the [Getting Started Guide](docs/getting_started.md) for more help
