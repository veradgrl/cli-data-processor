# JSON dosyasını oku ve içindeki verileri Python nesnelerine dönüştür.

import json  # * JSON dosyasını okumak
from pathlib import Path  # * dosya yolunu yönetmek

from dacite import DaciteError, from_dict  # * dict -> @dataclass dönüşümü

from src.exceptions import DataLoadError, DataValidationError
from src.models import Transaction, User

"""
    JSON dosyasını oku ve içindeki verileri Python nesnelerine dönüştür.
    
    Args:
        path (Path): JSON dosyasının yolu.
        
    Returns:
        tuple[list[User], list[Transaction]]: Kullanıcılar ve işlemler listesi.
"""


def load_data(path: Path) -> tuple[list[User], list[Transaction]]:

    try:
        with open(path, "r", encoding="utf-8") as file:
            dict_data = json.load(
                file
            )  # JSON'u Python verisine çeviriyor ve bunun tipi dict oluyor -  JSON oku

    except (
        FileNotFoundError
    ):  # * teknik hatayı yakalar ve bizim ürettiğimiz daha anlamlı bir hata mesajı verir
        raise DataLoadError(f"Dosya bulunamadı: {path}")

    except (
        json.JSONDecodeError
    ):  # * JSON dosyası bozuksa veya geçersizse yakalar ve anlamlı bir hata mesajı verir
        raise DataLoadError(f"JSON dosyası okunamadı: {path}")

    try:
        users = [
            from_dict(data_class=User, data=user) for user in dict_data["users"]
        ]  # * users değişkeninin tipi artık list[User] olacak şekilde dönüştürüldü.
        transactions = [
            from_dict(data_class=Transaction, data=transaction)
            for transaction in dict_data["transactions"]
        ]  # * transactions → list[Transaction]
    except (
        KeyError,
        DaciteError,
    ) as e:  # users anahtarı yoksa- keyerror, veri yapısı User/Transaction a uymuyorsa -- DaciteError
        raise DataValidationError(f"Veri yapısı geçersiz: {e}") from e

    return (
        users,
        transactions,
    )  # * users ve transactions listelerini döndür -> (list[User], list[Transaction])
