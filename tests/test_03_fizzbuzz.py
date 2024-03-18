from conftest import (
    assert_has_function,
    optional,
    remove_trailing,
    skip_if_no_function,
    strip_all_lines,
)

import task03_fizzbuzz as task

fizzbuzz_3_expected = """
1
2
Fizz
""".strip()
fizzbuzz_7_expected = """
1
2
Fizz
4
Buzz
Fizz
7
""".strip()


def test_fizzbuzz_3(capsys):
    assert_has_function(task, "fizzbuzz")
    task.fizzbuzz(3)
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual.endswith(fizzbuzz_3_expected), "incorrect output for input 3"


def test_fizzbuzz_7(capsys):
    assert_has_function(task, "fizzbuzz")
    task.fizzbuzz(7)
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual.endswith(fizzbuzz_7_expected), "incorrect output for input 7"


def test_fizzbuzz_n_more(capsys):
    assert_has_function(task, "fizzbuzz")
    for n in [10, 20, 100, 2000]:
        task.fizzbuzz(n)
        out, _ = capsys.readouterr()
        lines = strip_all_lines(out)
        start = -999
        for i, line in enumerate(lines):
            if line == "Fizz":
                start = i - 3
                break
        assert start > -999, f"no line containing 'Fizz' even when input {n}?"
        for i, line in enumerate(lines):
            if i <= start:
                pass
            elif (i - start) % 15 == 0:
                assert line == "FizzBuzz", f"{i - start} -> FizzBuzz"
            elif (i - start) % 5 == 0:
                assert line == "Buzz", f"{i - start} -> Buzz"
            elif (i - start) % 3 == 0:
                assert line == "Fizz", f"{i - start} -> Fizz"
            else:
                assert line == f"{i - start}", f"{i - start} is wrong?"


@optional
def test_nabeatsu_4(capsys):
    skip_if_no_function(task, "nabeatsu")
    task.nabeatsu(4)
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert "1\n2\n" in actual, "Nabeatsu says 1 and 2 in a normal way"
    assert actual.endswith("4"), "Nabeatsu says 4 normally and stop if input is 4"
    assert "\n3\n" not in actual, "Nabeatsu says 3 in a foolish way"


@optional
def test_nabeatsu_16(capsys):
    skip_if_no_function(task, "nabeatsu")
    task.nabeatsu(16)
    out, _ = capsys.readouterr()
    lines = strip_all_lines(out)
    for i in [3, 6, 9, 12, 15, 13]:
        assert i not in lines, f"Nabeatsu says {i} in a foolish way"
    for i in [1, 2, 4, 5, 7, 8, 10, 11, 14, 16]:
        assert f"{i}" in lines, f"Nabeatsu says {i} in a normal way"


@optional
def test_nabeatsu_more(capsys):
    skip_if_no_function(task, "nabeatsu")
    for n in [20, 100, 4000]:
        task.nabeatsu(n)
        out, _ = capsys.readouterr()
        lines = strip_all_lines(out)
        start = -999
        for i, line in enumerate(lines):
            if line == "1":
                start = i - 1
                break
        assert start > -999, f"no line of '1' even when input {n}?"
        for i, line in enumerate(lines):
            if i <= start:
                pass
            elif "3" in str(i - start) or (i - start) % 3 == 0:
                pass
            else:
                assert line == f"{i - start}", f"{i - start} should be normal?"
