# Task 03: FizzBuzz

**Goal:** Learn how to use conditional statements (if-elif-else)

## Overview

In this task, you'll learn:

- How to use `if`, `elif`, and `else` statements
- How to check if a number is divisible by another
- How to combine multiple conditions

## Task 03a (Required)

Open `task03_fizzbuzz.py` and edit the file to do the following tasks.

Complete the FizzBuzz code. The function `fizzbuzz(n)` should print numbers from 1 to `n`, but:

- For multiples of 3, print `Fizz` instead of the number
- For multiples of 5, print `Buzz` instead of the number
- For multiples of both 3 and 5 (i.e., multiples of 15), print `FizzBuzz`
- Otherwise, print the number

### Example Output

For `fizzbuzz(15)`:

```text
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

## Task 03b (Optional, Advanced)

### Instructions

A Japanese comedian "Nabeatsu of the world" is famous for his "Nabeatsu FizzBuzz".

He says numbers from 1 to `n`, but he **says the number foolishly** only when:

- The number is a multiple of 3 (3, 6, 9, ...), OR
- The number contains the digit 3 (3, 13, 23, 30, 31, 32, 33, ...)

Implement `nabeatsu(n)` that behaves like Nabeatsu, where you need to think how a computer can display a number "foolishly".

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

### Hint

There can be some [videos on YouTube](https://www.youtube.com/results?search_query=%EF%BC%93%E3%81%AE%E5%80%8D%E6%95%B0%E3%80%80%E3%82%A2%E3%83%9B%E3%81%AB%E3%81%AA%E3%82%8B):

- [https://www.youtube.com/watch?v=_dxG-CtXfCI](https://www.youtube.com/watch?v=_dxG-CtXfCI)
- [https://www.youtube.com/shorts/xUp_K2SfIvw](https://www.youtube.com/shorts/xUp_K2SfIvw)

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

## Common Mistakes

1. **Wrong order of conditions**
   - If you check `i % 3 == 0` before `i % 15 == 0`, you'll never get "FizzBuzz"!

2. **Using `=` instead of `==`**
   - ❌ `if i % 3 = 0:` (assignment)
   - ✅ `if i % 3 == 0:` (comparison)

3. **Forgetting the colon** after conditions
   - ❌ `if i % 3 == 0`
   - ✅ `if i % 3 == 0:`

## Fun Fact

FizzBuzz is a classic programming interview question!

It tests your understanding of:

- Loops
- Conditionals
- Modulo operator
- Basic problem-solving

## Need Help?

- Review conditional statements in Python
- Test with small numbers (e.g., `fizzbuzz(15)`)
- Use `print()` to debug which condition is being triggered
- See the [Getting Started Guide](docs/getting_started.md) for more help
