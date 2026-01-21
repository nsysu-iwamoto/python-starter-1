# Task 03: FizzBuzz


def fizzbuzz(n):
    """Print FizzBuzz sequence from 1 to n.
    
    For each number from 1 to n:
    - Print "Fizz" if divisible by 3
    - Print "Buzz" if divisible by 5
    - Print "FizzBuzz" if divisible by both 3 and 5
    - Print the number otherwise
    """
    print(f"FizzBuzz from 1 to {n}:")
    # TODO: Add your code here to implement FizzBuzz logic


if __name__ == "__main__":  # Main execution block
    n = int(input("Enter a number: "))
    fizzbuzz(n)
