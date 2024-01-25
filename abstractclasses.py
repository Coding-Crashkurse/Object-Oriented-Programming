from abc import ABC, abstractmethod

class AbstractArcher(ABC):

    @property
    @abstractmethod
    def hp(self):
        pass

    @abstractmethod
    def walk(self):
        pass

class Archer(AbstractArcher):

    def walk(self):
       super().walk()

    def __init__(self, hp):
        self._hp = hp

    @property
    def hp(self):
        return self._hp

archer = Archer(100)

archer.walk()