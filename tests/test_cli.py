import sys
from unittest.mock import patch

import pytest

from src.exceptions import DataLoadError, DataValidationError
from src.main import main


# * python -m src.main --status completed --> verildiğinde program gerçekten completed transaction'larını yazdırıyor mu?
def test_cli_status(caplog, monkeypatch):
    caplog.set_level("INFO")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "main.py",
            "--status",
            "completed",
        ],  # * komut satırına girilmesi beklenen işlemin sys.argv karşılığı
    )

    main()

    assert "101" in caplog.text


# * birden fazla filtrenin gerçekten zincirlendiğini test edeceğiz
def test_cli_multiple_filters(caplog, monkeypatch):
    caplog.set_level("INFO")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "main.py",
            "--status",
            "completed",
            "--category",
            "food",
            "--user_id",
            "3",
        ],
    )

    main()

    assert "105" in caplog.text
    assert "101" not in caplog.text


def test_cli_without_filters(caplog, monkeypatch):
    caplog.set_level("INFO")

    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py"],
    )

    main()

    assert "101" in caplog.text
    assert "110" in caplog.text


# * mock : Gerçek bir şeyi test sırasında geçici olarak taklit etmek.
def test_main_data_load_error(caplog, monkeypatch):
    caplog.set_level("ERROR")

    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py"],
    )

    with patch(
        "src.main.load_data",
        side_effect=DataLoadError("test hatası"),
    ), pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1  # SystemExit(1) çalıştı mı?
    assert "test hatası" in caplog.text  # logger.error(e) çalıştı mı?


def test_main_data_validation_error(caplog, monkeypatch):
    caplog.set_level("ERROR")

    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py"],
    )

    with patch(
        "src.main.load_data",
        side_effect=DataValidationError("test validation hatası"),
    ), pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1
    assert "test validation hatası" in caplog.text
