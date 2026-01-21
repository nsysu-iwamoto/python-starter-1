# Task 04: Fibonacci

**Goal:** Combine loops, conditionals, and variables

---

## Overview

In this task, you'll learn:
- How to use loops with conditional logic
- How to maintain state across loop iterations
- How to implement algorithms

**Note:** In this course, the Fibonacci sequence starts with: **1, 1, 2, 3, 5, 8, ...**

(Some definitions start with 0, 1, but we use 1, 1 for simplicity.)

---

## Task 04a (Required)

### Instructions

Open `task04_fibonacci.py` and edit the file to do the following tasks.

Complete the function `fibonacci(goal)` so that it displays the Fibonacci sequence but stops just before reaching the `goal`.

For example, `fibonacci(13)` should print:

```
1
1
2
3
5
8
```

Of course, `fibonacci(9)` should give the same output (stops before reaching 9).

### What is the Fibonacci Sequence?

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones:

```
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

How it works:
- Start with: 1, 1
- Next number: 1 + 1 = 2
- Next number: 1 + 2 = 3
- Next number: 2 + 3 = 5
- Next number: 3 + 5 = 8
- And so on...

### Hints

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

### How to Test

```bash
# Run your code
python task04_fibonacci.py

# Run the test
python -m pytest tests/test_04_fibonacci.py::test_fibonacci -v
```

---

## Task 04b (Optional, Advanced)

### Instructions

Write a function `fibonacci_to(n)` that displays the Fibonacci sequence up to `n`. 

However, if `n` is not in the Fibonacci sequence, the function should not print any numbers, but instead tell the user that the input `n` is not suitable for this function.

### Example Output

For `fibonacci_to(8)`:
```
1
1
2
3
5
8
```

For `fibonacci_to(10)`:
```
10 is not in the Fibonacci sequence
```

### Additional Challenge

Does your code work even if the input is extremely large (e.g., `fibonacci_to(10**100)`)?

Think about:
- How long does it take to check?
- Does your code handle large numbers efficiently?

### Hints

<details>
<summary>Click to see hint 1: Checking if n is in sequence</summary>

Generate the Fibonacci sequence until you either:
1. Find the number `n` (it's in the sequence)
2. Pass the number `n` (it's not in the sequence)

```python
while current < n:
    # generate next number
    
if current == n:
    # n is in sequence, print it
else:
    # n is not in sequence
```
</details>

<details>
<summary>Click to see hint 2: Efficiency for large numbers</summary>

Your algorithm should be efficient. It should only need to:
- Generate numbers up to `n`
- Not store all numbers in memory

This means using a loop with just a few variables, not creating a large list.
</details>

---

## Understanding the Fibonacci Sequence

### Mathematical Definition

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
```

Note: In this task, we start with F(1) = 1, F(2) = 1 for simplicity.

### Applications

The Fibonacci sequence appears in:
- Nature (spiral patterns in shells, flowers)
- Art and architecture
- Computer algorithms
- Financial markets

### First 15 Fibonacci Numbers

```
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610
```

---

## Common Mistakes

1. **Not initializing variables correctly**
   - Start with `a = 1` and `b = 1`

2. **Wrong loop condition**
   - Use `while current < goal` not `while current <= goal`

3. **Not updating variables properly**
   - Remember to shift values: `a, b = b, a + b`

4. **Printing in wrong order**
   - Print BEFORE updating variables, or adjust your logic

---

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

---

## Need Help?

- Review `while` loops in Python
- Try calculating a few Fibonacci numbers by hand first
- Use `print()` to debug variable values
- Start with small goals like `fibonacci(10)`
- See the [Getting Started Guide](docs/getting_started.md) for more help

---

## Fun Fact

The Fibonacci sequence is named after Leonardo Fibonacci, an Italian mathematician from the 13th century, but it was known in Indian mathematics even earlier!
