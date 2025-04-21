from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Storage(ABC, Generic[T]):
    @abstractmethod
    def save(self, entity: T):
        """Сохранение сущности в хранилище"""
        pass

    @abstractmethod
    def load(self) -> list[T] | None:
        """Получение списка сущностей из хранилища"""
        pass
