import pytest
from pytest import MonkeyPatch

from agripath.utils.prompt import ask_int, choose_index


@pytest.mark.parametrize(
    "num_str, num",
    [
        ("1", 1),
        ("0", 0),
        ("5", 5),
        ("15", 15),
    ],
)
def test_nums_ask_int(num_str: str, num: int) -> None:
    assert ask_int(num_str) == num


@pytest.mark.parametrize(
    "invalid_input, expected_value",
    [
        ("1.4", None),
        ("10a", None),
        ("test", None),
        ("error", None),
    ],
)
def test_ask_int_value_error(invalid_input: str, expected_value: None) -> None:
    assert ask_int(invalid_input) == expected_value


def test_choose_index_first_item(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "1")

    result = choose_index(["A", "B", "C"], "escolha: ")

    assert result == 0


def test_choose_index_cancel(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "0")
    assert choose_index(["A", "B", "C"], "escolha: ") is None


def test_choose_index_non_numeric(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "test")
    assert choose_index(["A", "B", "C"], "escolha: ") is None


def test_choose_index_out_of_range(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "1000")
    assert choose_index(["A", "B", "C"], "escolha: ") is None
