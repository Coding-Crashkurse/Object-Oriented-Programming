from abc import ABC, abstractmethod

class AbstractArcher(ABC):

    @abstractmethod
    def walk(self):
        print("I walk...")

    @property
    @abstractmethod
    def hp(self):
        pass

class Archer(AbstractArcher):

    def __init__(self, hp):
        self._hp = hp

    def walk(self):
        super().walk()

    @property
    def hp(self):
        return self._hp


archer = Archer(100)
archer.walk()