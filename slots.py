class Archer:

    __slots__ = ("hp", "mana")

    def __init__(self, hp, mana):
        self.hp = hp
        self.mana = mana

class SuperArcher(Archer):

    __slots__ = ("arrows")

    def __init__(self, hp, mana, arrows):
        super().__init__(hp, mana)
        self.arrows = arrows

sarcher = SuperArcher(100, 50, 20)
print(sarcher.__dict__)