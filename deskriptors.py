
class Deskriptor:

    def __init__(self, value):
        self._value = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0 or value > self._value:
            raise ValueError(f"Property {self.name} erlaubt nur werte zwischen 0 und {self._value}")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Lifes:
    def __get__(self, instance, owner):
        return 3


class Archer:
    hp = Deskriptor(120)
    mana = Deskriptor(50)
    lifes = Lifes()

    def __init__(self, hp, mana, lifes):
        self.hp = hp
        self.mana = mana
        self.lifes = lifes

archer = Archer(100, 50, 5)


print(archer.lifes)


