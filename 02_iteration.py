# Task 01: Hello, World!


def show_one_to_ten():
    for i in range(6):
        print(i)


def show_one_to_n():
    n = int(input("Enter a number: "))
    print(f"Now I'm going to print one to {n}.")
    # continue your code


if __name__ == "__main__":  # the main part
    show_one_to_ten()
