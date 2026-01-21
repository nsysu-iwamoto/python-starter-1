# Task 04: Fibonacci

**Goal:** Combine loops, conditionals, and variables

## Overview

In this task, you'll learn:

- How to use loops with conditional logic
- How to maintain state across loop iterations
- How to implement algorithms

**Note:** In this course, the Fibonacci sequence starts with: **1, 1, 2, 3, 5, 8, ...**

(Some definitions start with 0, 1, but we use 1, 1 for simplicity.)

## Task 04a (Required)

### Instructions

Open `task04_fibonacci.py` and edit the file to do the following tasks.

Complete the function `fibonacci(goal)` so that it displays the Fibonacci sequence but stops just before reaching the `goal`.

For example, `fibonacci(13)` should print:

```console
1
1
2
3
5
8
```

Of course, `fibonacci(9)` should give the same output (stops before reaching 9).

<details>
<summary>Click to see hint 1: Using two variables</summary>

You need to keep track of the last two numbers:

```python
a = 1  # first number
b = 1  # second number

# To get the next number:
next_num = a + b
```

</details>

<details>
<summary>Click to see hint 2: Updating variables</summary>

After calculating the next number, you need to update the variables:

```python
a = b         # shift b to a
b = next_num  # shift next_num to b
```

Or, more elegantly in Python:

```python
a, b = b, a + b
```

</details>

<details>
<summary>Click to see hint 3: Loop structure</summary>

Use a `while` loop that continues as long as the number is less than the goal:

```python
while current_number < goal:
    print(current_number)
    # calculate next number
    # update variables
```

</details>

## Task 04b (Optional, Advanced)

Write a function `fibonacci_to(n)` that displays the Fibonacci sequence up to `n`.

However, if `n` is not in the Fibonacci sequence, the function should not print any numbers, but instead tell the user that the input `n` is not suitable for this function.

### Example Output

For `fibonacci_to(8)`:

```console
1
1
2
3
5
8
```

For `fibonacci_to(10)`:

```console
10 is not in the Fibonacci sequence
```

### Additional Challenge

Does your code work even if the input is extremely large (e.g., `fibonacci_to(10**100)`)?

Think about:

- How long does it take to check?
- Does your code handle large numbers efficiently?

## Common Mistakes

1. **Not initializing variables correctly**
   - Start with `a = 1` and `b = 1`

2. **Wrong loop condition**
   - Use `while current < goal` not `while current <= goal`

3. **Not updating variables properly**
   - Remember to shift values: `a, b = b, a + b`

4. **Printing in wrong order**
   - Print BEFORE updating variables, or adjust your logic

## Understanding While Loops

### `while` loop syntax

```python
while condition:
    # code to repeat while condition is True
```

### Difference from `for` loop

- `for` loop: When you know how many iterations
- `while` loop: When you loop until a condition is met

Example:

```python
# for loop - fixed iterations
for i in range(10):
    print(i)

# while loop - conditional
count = 0
while count < 10:
    print(count)
    count += 1
```

## Need Help?

- Review `while` loops in Python
- Try calculating a few Fibonacci numbers by hand first
- Use `print()` to debug variable values
- Start with small goals like `fibonacci(10)`
- See the [Getting Started Guide](docs/getting_started.md) for more help
