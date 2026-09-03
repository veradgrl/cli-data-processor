from dataclasses import dataclass

# pytonda verinin nasıl temsil edileceği belirlendi


@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool


@dataclass
class Transaction:
    id: int
    user_id: int
    amount: float
    category: str
    currency: str
    status: str
