# Task 02: Iteration


def show_one_to_ten():
    """Print numbers from 1 to 10, one per line.
    
    Currently this prints 0 to 5. Fix it to print 1 to 10.
    """
    for i in range(6):
        print(i)


def show_one_to_n():
    """Ask user for a number n, then print numbers from 1 to n.
    
    First, ask the user to enter a number.
    Then, print all numbers from 1 to n (inclusive), one per line.
    """
    n = int(input("Enter a number: "))
    print(f"Now I'm going to print one to {n}.")
    # TODO: Add your code here to print numbers from 1 to n


if __name__ == "__main__":  # Main execution block
    show_one_to_ten()
