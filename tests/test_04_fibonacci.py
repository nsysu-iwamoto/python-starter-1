import pytest
from conftest import assert_has_function, skip_if_no_function
import re

module = __import__("04_fibonacci")


def test_fibonacci_13(capsys):
    assert_has_function(module, "fibonacci")
    module.fibonacci(13)
    out, _ = capsys.readouterr()
    expected = "1\n1\n2\n3\n5\n8\n"
    assert out == expected


def test_fibonacci_8(capsys):
    assert_has_function(module, "fibonacci")
    module.fibonacci(8)
    out, _ = capsys.readouterr()
    expected = "1\n1\n2\n3\n5\n"
    assert out == expected


def test_fibonacci_3(capsys):
    assert_has_function(module, "fibonacci")
    module.fibonacci(3)
    out, _ = capsys.readouterr()
    expected = "1\n1\n2\n"
    assert out == expected


def test_fibonacci_1(capsys):
    assert_has_function(module, "fibonacci")
    module.fibonacci(1)
    out, _ = capsys.readouterr()
    expected = ""
    assert out == expected
