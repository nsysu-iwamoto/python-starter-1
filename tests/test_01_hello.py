from conftest import assert_has_function, optional, remove_trailing, skip_if_no_function

import task01_hello as task

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
    assert_has_function(task, "hello_world")
    task.hello_world()
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual == expected_hello_world_1


@optional
def test_hello_world_three_times(capsys):
    skip_if_no_function(task, "hello_world_three_times")
    task.hello_world_three_times()  # ty: ignore[unresolved-attribute]
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual.endswith(hw), f"output should end with '{hw}'"
    assert actual.count(hw) == 3, f"output should have three '{hw}'"
    assert actual.endswith(expected_hello_world_3)


@optional
def test_hello_world_n_times(capsys, monkeypatch):
    skip_if_no_function(task, "hello_world_n_times")

    def fake_input(n):
        # absorb stdout before input
        _ = capsys.readouterr()
        return n

    monkeypatch.setattr("builtins.input", lambda s: fake_input(4))
    task.hello_world_n_times()  # ty: ignore[unresolved-attribute]
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual.endswith(hw), f"output should end with '{hw}'"
    assert actual.count(hw) == 4, f"output should have four '{hw}' when input 4"
    assert actual.endswith(expected_hello_world_4)


@optional
def test_hello_world_n_times_more(capsys, monkeypatch):
    skip_if_no_function(task, "hello_world_n_times")

    def fake_input(n):
        # absorb stdout before input
        _ = capsys.readouterr()
        return n

    for n in [10, 50, 200]:
        monkeypatch.setattr("builtins.input", lambda s: fake_input(n))
        task.hello_world_n_times()  # ty: ignore[unresolved-attribute]
        out, _ = capsys.readouterr()
        actual = remove_trailing(out)
        assert actual.endswith(hw), f"output should end with '{hw}'"
        assert actual.count(hw) == n, f"output should have {n} '{hw}' when input {n}"
        expected = "\n".join(expected_hello_world_1 for i in range(n)).strip()
        assert actual.endswith(expected)
