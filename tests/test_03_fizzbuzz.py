import pytest
from conftest import assert_has_function, skip_if_no_function
import re

module = __import__("03_fizzbuzz")


def test_fizzbuzz_2(capsys):
    assert_has_function(module, "fizzbuzz")
    module.fizzbuzz(2)
    out, _ = capsys.readouterr()
    out = re.sub(r"^Fizz.*:\s*$\n", "", out, flags=re.I | re.M)
    expected = "1\n2\n"
    assert out == expected


def test_fizzbuzz_3(capsys):
    assert_has_function(module, "fizzbuzz")
    module.fizzbuzz(3)
    out, _ = capsys.readouterr()
    out = re.sub(r"^Fizz.*:\s*$\n", "", out, flags=re.I | re.M)
    expected = "1\n2\nFizz\n"
    assert out == expected


def test_fizzbuzz_7(capsys):
    assert_has_function(module, "fizzbuzz")
    module.fizzbuzz(7)
    out, _ = capsys.readouterr()
    out = re.sub(r"^Fizz.*:\s*$\n", "", out, flags=re.I | re.M)
    expected = "1\n2\nFizz\n4\nBuzz\nFizz\n7\n"
    assert out == expected


# TODO: implement more tests
