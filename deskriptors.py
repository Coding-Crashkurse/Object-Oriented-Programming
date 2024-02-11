class Deskriptor:

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError("Value has to be between 0 and 100")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Lifes:
    def __get__(self, instance, owner):
        return 3

    def __set__(self, instance, value):
        pass

class Archer:
    hp = Deskriptor
    mana = Deskriptor
    lifes = Lifes()

    def __init__(self, hp, mana, lifes):
        self.hp = hp
        self.mana = mana
        self.lifes = lifes

archer1 = Archer(100, 30, 6)
print(archer1.lifes)

