from abc import ABC, abstractmethod
from collections.abc import Callable, Iterable, Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseProcessor(ABC, Generic[T]):

    @abstractmethod
    def process(self) -> Iterator[T]:
        pass

    def filter_by(
        self, items: Iterable[T], predicate: Callable[[T], bool]
    ) -> Iterator[T]:
        for item in items:
            if predicate(item):
                yield item

    # * filter_by fonksiyonu, T tipindeki elemanlardan oluşan, üzerinde dolaşabileceğim bir veri kaynağı(items) ve T alan ve bool döndüren bir fonksiyon (Callable) alır.
    """
    items = filtreleyeceğimiz liste
    predicate = elemanın koşulu sağlayıp sağlamadığını kontrol eden fonksiyon

    items = users
    predicate = lambda user: user.is_active
    --users listesindeki her user için is_active değerini kontrol et.
        
        """
