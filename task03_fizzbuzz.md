# Task 03: FizzBuzz

**Goal:** Learn how to use conditional statements (if-elif-else)

---

## Overview

In this task, you'll learn:
- How to use `if`, `elif`, and `else` statements
- How to check if a number is divisible by another
- How to combine multiple conditions

---

## Task 03a (Required)

### Instructions

Open `task03_fizzbuzz.py` and edit the file to do the following tasks.

Complete the FizzBuzz code. The function `fizzbuzz(n)` should print numbers from 1 to `n`, but:

- For multiples of 3, print `Fizz` instead of the number
- For multiples of 5, print `Buzz` instead of the number
- For multiples of both 3 and 5 (i.e., multiples of 15), print `FizzBuzz`
- Otherwise, print the number

### Example Output

For `fizzbuzz(15)`:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

### Understanding the Problem

Let's break it down:

| Number | Divisible by 3? | Divisible by 5? | Output |
|--------|----------------|-----------------|---------|
| 1      | No             | No              | 1       |
| 2      | No             | No              | 2       |
| 3      | Yes            | No              | Fizz    |
| 4      | No             | No              | 4       |
| 5      | No             | Yes             | Buzz    |
| 6      | Yes            | No              | Fizz    |
| ...    | ...            | ...             | ...     |
| 15     | Yes            | Yes             | FizzBuzz|

### Hints

<details>
<summary>Click to see hint 1: Checking divisibility</summary>

Use the modulo operator `%` to check if a number is divisible:

```python
if i % 3 == 0:  # i is divisible by 3
    # do something
```

The modulo operator returns the remainder of division.
- `6 % 3 == 0` (6 divided by 3 has remainder 0)
- `7 % 3 == 1` (7 divided by 3 has remainder 1)
</details>

<details>
<summary>Click to see hint 2: Order of conditions</summary>

⚠️ **Important:** Check for multiples of 15 BEFORE checking for multiples of 3 or 5!

```python
if i % 15 == 0:
    print("FizzBuzz")
elif i % 3 == 0:
    print("Fizz")
elif i % 5 == 0:
    print("Buzz")
else:
    print(i)
```

Why? Because 15 is divisible by both 3 and 5!
</details>

<details>
<summary>Click to see hint 3: Alternative approach</summary>

You can also use `and` to check both conditions:

```python
if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
```

This is equivalent to checking `i % 15 == 0`.
</details>

### How to Test

```bash
# Run your code
python task03_fizzbuzz.py

# Run the test
python -m pytest tests/test_03_fizzbuzz.py::test_fizzbuzz -v
```

---

## Task 03b (Optional, Advanced)

### Instructions

A Japanese comedian "Nabeatsu of the world" is famous for his "Nabeatsu FizzBuzz".

He says numbers from 1 to `n`, but he **says the number foolishly** only when:

- The number is a multiple of 3 (3, 6, 9, ...), OR
- The number contains the digit 3 (3, 13, 23, 30, 31, 32, 33, ...)

Implement `nabeatsu(n)` that behaves like Nabeatsu, where you need to think how a computer can display a number "foolishly".

### Example Output

For `nabeatsu(35)`:

```
1
2
3!     ← multiple of 3 AND contains 3
4
5
6!     ← multiple of 3
7
8
9!     ← multiple of 3
10
11
12!    ← multiple of 3
13!    ← contains 3
14
15!    ← multiple of 3
...
30!    ← multiple of 3 AND contains 3
31!    ← contains 3
32!    ← contains 3
33!    ← multiple of 3 AND contains 3
34!    ← contains 3
35!    ← contains 3
```

### Hints

<details>
<summary>Click to see hint 1: Checking if digit contains 3</summary>

Convert the number to a string and check if '3' is in it:

```python
if '3' in str(i):
    # contains the digit 3
```
</details>

<details>
<summary>Click to see hint 2: Combining conditions</summary>

Use the `or` operator to check either condition:

```python
if i % 3 == 0 or '3' in str(i):
    print(f"{i}!")  # foolish display
else:
    print(i)
```
</details>

<details>
<summary>Click to see hint 3: Creative foolish display</summary>

You can be creative! Ideas:
- Add exclamation marks: `"3!"`
- Repeat the number: `"3333"`
- Add emoji: `"3 🤪"`
- Convert to full-width: `"３"`
- Any other way to make it look "foolish"!
</details>

---

## Understanding Conditional Statements

### Basic `if-else` syntax

```python
if condition:
    # code if condition is True
else:
    # code if condition is False
```

### `if-elif-else` for multiple conditions

```python
if condition1:
    # code if condition1 is True
elif condition2:
    # code if condition2 is True
elif condition3:
    # code if condition3 is True
else:
    # code if all conditions are False
```

### Logical operators

- `and`: Both conditions must be True
- `or`: At least one condition must be True
- `not`: Negates the condition

---

## Common Mistakes

1. **Wrong order of conditions**
   - If you check `i % 3 == 0` before `i % 15 == 0`, you'll never get "FizzBuzz"!

2. **Using `=` instead of `==`**
   - ❌ `if i % 3 = 0:` (assignment)
   - ✅ `if i % 3 == 0:` (comparison)

3. **Forgetting the colon** after conditions
   - ❌ `if i % 3 == 0`
   - ✅ `if i % 3 == 0:`

---

## Fun Fact

FizzBuzz is a classic programming interview question!

It tests your understanding of:
- Loops
- Conditionals
- Modulo operator
- Basic problem-solving

---

## Need Help?

- Review conditional statements in Python
- Test with small numbers (e.g., `fizzbuzz(15)`)
- Use `print()` to debug which condition is being triggered
- See the [Getting Started Guide](docs/getting_started.md) for more help
