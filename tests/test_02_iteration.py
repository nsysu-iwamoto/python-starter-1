import io
import re

import pytest
from conftest import assert_has_function, optional, remove_trailing, skip_if_no_function

import task02_iteration as task

one_to_10_expected = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n".strip()
one_to_4_expected = "1\n2\n3\n4\n".strip()
one_to_5_ordinal_expected = """
1st
2nd
3rd
4th
5th
""".strip()


def test_show_one_to_ten(capsys):
    assert_has_function(task, "show_one_to_ten")
    task.show_one_to_ten()
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual == one_to_10_expected


def test_show_one_to_n(capsys, monkeypatch):
    assert_has_function(task, "show_one_to_n")
    monkeypatch.setattr("sys.stdin", io.StringIO("4"))
    task.show_one_to_n()
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual.endswith(one_to_4_expected), "incorrect output for input 4"


@pytest.mark.parametrize("n", [1, 10, 200, 999])
def test_show_one_to_n_more(capsys, monkeypatch, n):
    assert_has_function(task, "show_one_to_n")
    monkeypatch.setattr("sys.stdin", io.StringIO(f"{n}"))
    task.show_one_to_n()
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual.endswith(str(n)), f"output should end with {n} if input is {n}"
    for i in range(3, n - 1):
        assert f"{i}\n{i + 1}" in actual


@optional
def test_show_one_to_n_ordinal_5(capsys, monkeypatch):
    skip_if_no_function(task, "show_one_to_n_ordinal")
    monkeypatch.setattr("sys.stdin", io.StringIO("5"))
    task.show_one_to_n_ordinal()  # ty: ignore[unresolved-attribute]
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual.endswith("5th"), "output should end with '5th' if input is 5."
    assert one_to_5_ordinal_expected in actual


@optional
def test_show_one_to_n_ordinal_1(capsys, monkeypatch):
    skip_if_no_function(task, "show_one_to_n_ordinal")
    monkeypatch.setattr("sys.stdin", io.StringIO("1"))
    task.show_one_to_n_ordinal()  # ty: ignore[unresolved-attribute]
    out, _ = capsys.readouterr()
    actual = remove_trailing(out)
    assert actual.endswith("1st"), "output should end with '1st' if input is 1."
    assert "2nd" not in actual


@optional
def test_show_one_to_n_ordinal_more(capsys, monkeypatch):
    for n in [5, 20, 100, 200]:
        skip_if_no_function(task, "show_one_to_n_ordinal")
        monkeypatch.setattr("sys.stdin", io.StringIO(f"{n}"))
        task.show_one_to_n_ordinal()  # ty: ignore[unresolved-attribute]
        out, _ = capsys.readouterr()
        actual = remove_trailing(out)

        # check number part first by replacing a-z with x
        num = re.sub(r"[a-zA-Z]", "x", out)
        num = re.sub(r"\s+$", "", num, flags=re.M)
        assert num.endswith(f"{n}xx"), f"output should end with {n}xx for input {n}"
        num_expected = ("\n".join(f"{i + 1}xx" for i in range(n))).strip()
        assert num_expected in num, f"output should have 1 to {n}"

        for line in actual.splitlines():
            line = line.strip()
            if m := re.match(r"(\d+)(\w+)", line):
                number, suffix = int(m[1]), m[2]
                if number % 100 in [11, 12, 13]:
                    assert suffix == "th", f"ordinal for {number} is {number}th"
                elif number % 10 == 1:
                    assert suffix == "st", f"ordinal for {number} is {number}st"
                elif number % 10 == 2:
                    assert suffix == "nd", f"ordinal for {number} is {number}nd"
                elif number % 10 == 3:
                    assert suffix == "rd", f"ordinal for {number} is {number}rd"
                else:
                    assert suffix == "th", f"ordinal for {number} is {number}th"
