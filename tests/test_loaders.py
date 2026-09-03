import json
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from src.exceptions import DataLoadError, DataValidationError
from src.loaders import load_data

#! loaders.py testleri  # noqa: EXE005


def test_load_data():
    # * Geçerli bir JSON dosyasını yükleme testi
    path = Path("data/sample.json")
    users, transactions = load_data(path)

    assert len(users) == 5
    assert len(transactions) == 10


# * load_data(path) çalışırken DataLoadError çıkmasını bekliyorum
def test_load_data_file_not_found():
    path = Path("data/bu_dosya_yok.json")

    with pytest.raises(DataLoadError):
        load_data(path)


# * JSON dosyası mevcut ama JSON formatı bozuksa DataLoadError oluşuyor mu -- open() bozuk JSON döndürürse DataLoadError oluşuyor mu
def test_load_data_invalid_json():
    with patch(
        "builtins.open",
        mock_open(read_data="{ invalid json }"),
    ), pytest.raises(DataLoadError):
        load_data(Path("invalid.json"))


# * loader.py içindeki except gerçekten çalışıyor mu
def test_load_data_invalid_structure(tmp_path):
    data = {"transactions": []}

    path = tmp_path / "invalid.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    with pytest.raises(DataValidationError):
        load_data(path)


def test_load_data_with_mock():
    json_data = """
    {
        "users": [
            {
                "id": 1,
                "name": "Ayse",
                "email": "ayse@example.com",
                "is_active": true
            }
        ],
        "transactions": []
    }
    """

    with patch("builtins.open", mock_open(read_data=json_data)):
        users, transactions = load_data(Path("test.json"))

    assert users[0].name == "Ayse"
    assert transactions == []
    # * gerçekten dosya açmıyor, sanki dosyanın içinde bu json varmış gibi davranıyor
