import pytest
import io
from conftest import assert_has_function, skip_if_no_function
import re

module = __import__("02_iteration")


def test_show_one_to_ten(capsys):
    assert_has_function(module, "show_one_to_ten")
    module.show_one_to_ten()
    out, _ = capsys.readouterr()
    assert out == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"


def test_show_one_to_n(capsys, monkeypatch):
    assert_has_function(module, "show_one_to_n")
    monkeypatch.setattr("sys.stdin", io.StringIO("4"))
    module.show_one_to_n()
    out, _ = capsys.readouterr()
    assert out.endswith("\n1\n2\n3\n4\n"), "For input 4, output must end with 4."
    assert "5" not in out, "For input 4, output must not contain 5"


@pytest.mark.parametrize("n", range(1, 10))
def test_show_one_to_n_more(capsys, monkeypatch, n):
    assert_has_function(module, "show_one_to_n")
    monkeypatch.setattr("sys.stdin", io.StringIO(f"{n}"))
    module.show_one_to_n()
    out, _ = capsys.readouterr()
    expected = "\n".join(str(i) for i in range(1, n + 1))
    assert "\n" + expected + "\n" in out


def test_show_one_to_n_ordinal_5(capsys, monkeypatch):
    skip_if_no_function(module, "show_one_to_n_ordinal")
    monkeypatch.setattr("sys.stdin", io.StringIO("5"))
    module.show_one_to_n_ordinal()
    out, _ = capsys.readouterr()
    assert "\n1st\n2nd\n3rd\n4th\n5th\n" in out, "Incorrect for input 5"
    assert out.endswith("5th"), "Output must end with 5th if input is 5"


@pytest.mark.parametrize("n", [1, 5, 13, 100, 200])
def test_show_one_to_n_ordinal_more(capsys, monkeypatch, n):
    skip_if_no_function(module, "show_one_to_n_ordinal")
    monkeypatch.setattr("sys.stdin", io.StringIO(f"{n}"))
    module.show_one_to_n_ordinal()
    out, _ = capsys.readouterr()

    number_part = re.sub(r"[a-z]", "", out)
    number_part_expected = "\n".join(str(i) for i in range(1, n + 1))
    assert number_part.endswith(number_part_expected)

    # TODO: implement ordinals assertions
