import pytest
import random
from conftest import assert_has_function, skip_if_no_function, remove_trailing
import sys

module = __import__("04_fibonacci")

fibonacci_before_13_expected = """
1
1
2
3
5
8
""".strip()
fibonacci_before_9_expected = """
1
1
2
3
5
8
""".strip()
fibonacci_before_5_expected = """
1
1
2
3
""".strip()
fibonacci_before_2_expected = """
1
1
""".strip()

fibonacci_million = [
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
    10946,
    17711,
    28657,
    46368,
    75025,
    121393,
    196418,
    317811,
    514229,
    832040,
]
fibonacci_before_million_expected = "\n".join(str(i) for i in fibonacci_million)


@pytest.mark.parametrize(
    "n, expected",
    [
        (13, fibonacci_before_13_expected),
        (9, fibonacci_before_9_expected),
        (5, fibonacci_before_5_expected),
        (2, fibonacci_before_2_expected),
    ],
)
def test_fibonacci_n(capsys, n, expected):
    assert_has_function(module, "fibonacci")
    module.fibonacci(n)
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual == expected


def test_fibonacci_million(capsys):
    assert_has_function(module, "fibonacci")
    module.fibonacci(1000000)
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual == fibonacci_before_million_expected


def test_fibonacci_to(capsys):
    skip_if_no_function(module, "fibonacci_to")
    for i in fibonacci_million:  # existing case
        if i == 1:
            continue
        module.fibonacci_to(i)
        out, _ = capsys.readouterr()
        actual = remove_trailing(out)
        expected = "\n".join(str(j) for j in fibonacci_million if j <= i)
        assert actual == expected, f"invalid output for {i}"
    for _ in range(10):  # test 10 random number
        i = 1
        while i in fibonacci_million:
            i = random.randint(4, 1000000)
        module.fibonacci_to(i)
        out, _ = capsys.readouterr()
        actual = remove_trailing(out)
        assert "1\n1\n2" not in actual, f"should not output fibonacci if input is {i}"


@pytest.mark.timeout(1)
def test_fibonacci_to_extreme(capsys):
    skip_if_no_function(module, "fibonacci_to")
    sys.set_int_max_str_digits(10000)
    s = 1
    for i in range(2, 1000):
        s = s * i
        n = 5 * s * s  # must not be in fibonacci
        module.fibonacci_to(n)
        out, _ = capsys.readouterr()
        actual = remove_trailing(out)
        assert "1\n1\n2" not in actual, f"should not output fibonacci if input is {i}"
