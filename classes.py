class Archer:

    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self.__arrows = arrows

    def walk(self):
        print(f'Ich bin {self} und laufe')

    def shoot(self):
        if self.__arrows > 0:
            self.__arrows -= 1
            print(f"Bogenschütze hat geschossen, noch {self.__arrows} Pfeile übrig")
        else:
            print("Bogenschütze hat keinen Pfeil mehr")

    @classmethod
    def from_data(cls, hp, mana, arrows):
        return cls(hp, mana, arrows)

    @staticmethod
    def static():
        print("Ich bin eine Staticmethod")

archer1 = Archer.from_data(100, 5, 0)
archer1.shoot()

Archer(100, 5, 0)
archer = Archer
archer.static()




