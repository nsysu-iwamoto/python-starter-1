import pytest
from conftest import assert_has_function, skip_if_no_function

module = __import__("01_hello")


def test_hello_world(capsys):
    assert_has_function(module, "hello_world")
    module.hello_world()
    out, _ = capsys.readouterr()
    assert out == "Hello, World!\n"


def test_hello_world_three_times(capsys):
    skip_if_no_function(module, "hello_world_three_times")
    module.hello_world_three_times()
    out, _ = capsys.readouterr()
    assert out == "Hello, World!" * 3


def test_hello_world_n_timese(capsys):
    skip_if_no_function(module, "hello_world_n_times")
    module.hello_world_n_times(4)
    out, _ = capsys.readouterr()
    assert out == "Hello, World!\nHello, World!\nHello, World!\nHello, World!\n"


@pytest.mark.parametrize("n", range(0, 10))
def test_hello_world_n_times_more(capsys, n):
    skip_if_no_function(module, "hello_world_n_times")
    module.hello_world_n_times(n)
    out, _ = capsys.readouterr()
    assert out == "Hello, World!\n" * n
