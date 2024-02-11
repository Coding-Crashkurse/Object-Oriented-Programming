class Archer:

    species = "human"

    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self.arrows = arrows

    def shoot(self):
        if self.arrows > 0:
            self.arrows -= 1
            print(f"Archer shot. {self.arrows} left!")
        else:
            print("Archer can not shoot. No arrows left")

    @classmethod
    def from_string(cls, data_string):
        hp, mana, arrows =  map(int, data_string.split("-"))
        return cls(hp, mana, arrows)

    @staticmethod
    def static():
        print("I am static!")

archer1 = Archer(100, 100, 3)

archer2 = Archer.from_string("100-100-5")
Archer.static()

