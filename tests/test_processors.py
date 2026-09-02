import pytest

from src.models import Transaction, User
from src.processors import TransactionProcessor, UserProcessor


# başka alanlara bağlı olmadan sadece bu fonksiyonu test edebilmek adına test amaçlı bir transaction listesi oluşturduk.
@pytest.fixture
def transactions():  # *transactions = Transaction nesnelerinden oluşan listenin tamamı.
    return [
        Transaction(
            id=1,
            user_id=1,
            amount=100.0,
            category="food",
            currency="USD",
            status="completed",
        ),
        Transaction(  # * transaction ise bu listenin içinden tek bir Transaction.
            id=2,
            user_id=1,
            amount=200.0,
            category="travel",
            currency="TRY",
            status="pending",
        ),
        Transaction(
            id=3,
            user_id=2,
            amount=300.0,
            category="food",
            currency="TRY",
            status="completed",
        ),
    ]


@pytest.fixture
def users():
    return [
        User(id=1, name="Ali", email="ali@example.com", is_active=False),
        User(id=2, name="Ayse", email="ayse@example.com", is_active=True),
        User(id=3, name="Mehmet", email="mehmet@example.com", is_active=True),
    ]


#! processors.py testleri  # noqa: EXE005
def test_filter_by_status(transactions):

    processor = TransactionProcessor(transactions)
    result = processor.filter_by_status(transactions, "completed")
    result = list(result)
    assert [transaction.id for transaction in result] == [
        1,
        3,
    ]  # * result içindeki transaction'ların id'lerini al ve [1,3] ile karşılaştır. Eğer eşleşirse test başarılı demektir.


def test_filter_by_category(transactions):

    processor = TransactionProcessor(transactions)
    result = processor.filter_by_category(transactions, "food")
    result = list(result)
    assert [transaction.id for transaction in result] == [1, 3]


def test_filter_by_amount(transactions):

    processor = TransactionProcessor(transactions)
    result = processor.filter_by_amount(transactions, 100.0)
    result = list(result)
    assert [transaction.id for transaction in result] == [1]


def test_filter_by_currency(transactions):

    processor = TransactionProcessor(transactions)
    result = processor.filter_by_currency(transactions, "USD")
    result = list(result)
    assert [transaction.id for transaction in result] == [1]


def test_filter_by_user_id(transactions):

    processor = TransactionProcessor(transactions)
    result = processor.filter_by_user_id(transactions, 1)
    result = list(result)
    assert [transaction.id for transaction in result] == [
        1,
        2,
    ]  # * result listesindeki her transactionın id değerlerini al ve bunların [1, 2] olduğundan emin ol.


def test_process_t(transactions):

    processor = TransactionProcessor(transactions)

    result = processor.process()
    result = list(result)

    assert [transaction.id for transaction in result] == [1, 2, 3]


def test_process_u(users):

    processor = UserProcessor(users)

    result = processor.process()
    result = list(result)

    assert [user.id for user in result] == [1, 2, 3]


def test_filter_by_name(users):

    processor = UserProcessor(users)

    result = list(processor.filter_by_name(users, "Ayse"))

    assert [user.id for user in result] == [2]


def test_filter_by_email(users):

    processor = UserProcessor(users)

    result = list(processor.filter_by_email(users, "mehmet@example.com"))

    assert [user.id for user in result] == [3]


def test_filter_by_is_active(users):

    processor = UserProcessor(users)

    result = list(processor.filter_by_is_active(users, True))

    assert [user.id for user in result] == [2, 3]


def test_filter_by_id(users):

    processor = UserProcessor(users)

    result = list(processor.filter_by_id(users, 2))

    assert [user.id for user in result] == [2]


# ? pytest --cov=src --> src klasöründeki kodların ne kadarının testler sırasında çalıştırıldığını ölçer

# ? pytest --cov=src --cov-report=term-missing --> buradaki Missing sütunu bize hangi satırların test edilmediğini gösterecek
