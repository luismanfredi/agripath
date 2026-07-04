from datetime import UTC, datetime

import pytest
from pytest import CaptureFixture, MonkeyPatch

import src.menu as menu_mod
from src.menu import menu


@pytest.fixture(autouse=True)
def reset_products() -> None:
    menu_mod.products.clear()


def test_menu_product(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    inputs = iter(["1", "Test Id", "TEST", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    menu()
    captured = capsys.readouterr()
    assert "Product saved successfully!" in captured.out


def test_menu_event(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    inputs = iter(
        ["1", "Test Id", "TEST", "2", "1", "1", "test description", "TEST", "4"]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    menu()
    captured = capsys.readouterr()
    assert "Event added successfully!" in captured.out


def test_menu_show_products_events(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    inputs = iter(
        ["1", "Test Id", "TEST", "2", "1", "1", "test description", "TEST", "3", "4"]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    menu()
    registry_time = f"{datetime.now(UTC):%Y/%m/%d %H:%M:%S}"
    captured = capsys.readouterr()
    result = f'TEST - Test Id\n[{registry_time}] test description, registered by "TEST"'
    assert result in captured.out
