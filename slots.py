class Archer:
    __slots__ = ("hp", "mana")

    def __init__(self, hp, mana):
        self.hp = hp
        self.mana = mana

# class Archer2:
#
#     def __init__(self, hp, mana):
#         self.hp = hp
#         self.mana = mana
#
# archer = Archer(100, 50)
# archer2 = Archer2(100, 50)

from pympler import asizeof

# print(asizeof.asizeof(archer))
# print(asizeof.asizeof(archer2))

class MagicArcher(Archer):
    __slots__ = ("arrows")

    def __init__(self, hp, mana, arrows):
        super().__init__(hp, mana)
        self.arrows = arrows

marcher = MagicArcher(hp=100, mana=50, arrows=10)
print(marcher.hp)
print(marcher.arrows)