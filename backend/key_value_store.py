from abc import ABC, abstractmethod
from typing import Optional

from typing import Generic, TypeVar

K = TypeVar('K')
V = TypeVar('V')

class KeyValueStore(ABC, Generic[K, V]):
    @abstractmethod
    def get(self, key: K) -> Optional[V]:
        pass

    @abstractmethod
    def set(self, key: K, value: V):
        pass

    @abstractmethod
    def remove(self, key: K) -> bool:
        pass

class RAMOnlyKVStore(Generic[K, V], KeyValueStore[K, V]):
    def __init__(self):
        self.__dct = dict[K, V]()

    def get(self, key: K) -> Optional[V]:
        return self.__dct.get(key)
    
    def set(self, key: K, value: V):
        self.__dct[key] = value

    def remove(self, key: K):
        if key in self.__dct:
            self.__dct.pop(key)
            return True
        return False
    