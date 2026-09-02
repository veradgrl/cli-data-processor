from collections.abc import Iterable, Iterator

from src.base import BaseProcessor
from src.models import Transaction, User


class TransactionProcessor(BaseProcessor[Transaction]):
    def __init__(self, transactions: Iterable[Transaction]):
        self.transactions = transactions

    def process(self) -> Iterator[Transaction]:
        yield from self.transactions

    def filter_by_category(
        self, transactions: Iterable[Transaction], category: str
    ) -> Iterator[Transaction]:
        yield from self.filter_by(
            transactions, lambda transaction: transaction.category == category
        )

    def filter_by_status(
        self, transactions: Iterable[Transaction], status: str
    ) -> Iterator[
        Transaction
    ]:  # * "transactions isimli parametre, üzerinde dolaşabileceğim (for kullanabileceğim) Transaction verilerinden oluşuyor-- üzerinde çalışılacak veri"
        # * Bana hangi transaction akışını verirsen onu filtrele.
        yield from self.filter_by(
            transactions, lambda transaction: transaction.status == status
        )

    def filter_by_user_id(
        self, transactions: Iterable[Transaction], user_id: int
    ) -> Iterator[Transaction]:
        yield from self.filter_by(
            transactions, lambda transaction: transaction.user_id == user_id
        )

    def filter_by_amount(
        self, transactions: Iterable[Transaction], amount: float
    ) -> Iterator[Transaction]:
        yield from self.filter_by(
            transactions, lambda transaction: transaction.amount == amount
        )

    def filter_by_currency(
        self, transactions: Iterable[Transaction], currency: str
    ) -> Iterator[Transaction]:
        yield from self.filter_by(
            transactions, lambda transaction: transaction.currency == currency
        )


class UserProcessor(BaseProcessor[User]):
    def __init__(self, users: Iterable[User]):
        self.users = users

    def process(self) -> Iterator[User]:
        yield from self.users

    def filter_by_name(self, users: Iterable[User], name: str) -> Iterator[User]:
        yield from self.filter_by(users, lambda user: user.name == name)

    def filter_by_email(self, users: Iterable[User], email: str) -> Iterator[User]:
        yield from self.filter_by(users, lambda user: user.email == email)

    def filter_by_is_active(
        self, users: Iterable[User], is_active: bool
    ) -> Iterator[User]:
        yield from self.filter_by(users, lambda user: user.is_active == is_active)

    def filter_by_id(self, users: Iterable[User], user_id: int) -> Iterator[User]:
        yield from self.filter_by(users, lambda user: user.id == user_id)
