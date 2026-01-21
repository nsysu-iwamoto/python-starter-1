# Task 02: Iteration


def show_one_to_ten():
    for i in range(6):
        print(i)


def show_one_to_n():
    n = int(input("Enter a number: "))
    print(f"Now I'm going to print one to {n}.")
    # TODO: Add your code here to print numbers from 1 to n


if __name__ == "__main__":  # Main execution block
    show_one_to_ten()
