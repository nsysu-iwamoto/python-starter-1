import io
from conftest import assert_has_function, skip_if_no_function, remove_trailing

module = __import__("01_hello")

hw = "Hello, World!"
expected_hello_world_1 = "Hello, World!\n".strip()
expected_hello_world_2 = """
Hello, World!
Hello, World!
""".strip()
expected_hello_world_3 = """
Hello, World!
Hello, World!
Hello, World!
""".strip()
expected_hello_world_4 = """
Hello, World!
Hello, World!
Hello, World!
Hello, World!
""".strip()
expected_hello_world_5 = """
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
""".strip()


def test_hello_world(capsys):
    assert_has_function(module, "hello_world")
    module.hello_world()
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual == expected_hello_world_1


def test_hello_world_three_times(capsys):
    skip_if_no_function(module, "hello_world_three_times")
    module.hello_world_three_times()
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual.endswith(hw), f"output should end with '{hw}'"
    assert actual.count(hw) == 3, f"output should have three '{hw}'"
    assert actual.endswith(expected_hello_world_3)


def test_hello_world_n_times(capsys, monkeypatch):
    skip_if_no_function(module, "hello_world_n_times")
    monkeypatch.setattr("sys.stdin", io.StringIO("4"))
    module.hello_world_n_times()
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual.endswith(hw), f"output should end with '{hw}'"
    assert actual.count(hw) == 4, f"output should have four '{hw}' when input 4"
    assert actual.endswith(expected_hello_world_4)


def test_hello_world_n_times_more(capsys, monkeypatch):
    for n in [10, 50, 200]:
        skip_if_no_function(module, "hello_world_n_times")
        monkeypatch.setattr("sys.stdin", io.StringIO(f"{n}"))
        module.hello_world_n_times()
        out, _ = capsys.readouterr()
        actual = remove_trailing(out)
        assert actual.endswith(hw), f"output should end with '{hw}'"
        assert actual.count(hw) == n, f"output should have {n} '{hw}' when input {n}"
        expected = (expected_hello_world_1 * n).strip()
        assert actual.endswith(expected)
