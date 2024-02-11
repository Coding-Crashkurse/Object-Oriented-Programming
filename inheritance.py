class Player:

    def __init__(self, hp):
        self.hp = hp

    def walk(self):
        print("I am walking")


class Wizard(Player):

    def walk(self):
        print("I am floating...")

class Archer(Player):

    def __init__(self, hp, arrows):
        super().__init__(hp=hp)
        self.arrows = arrows

    def shoot(self):
        self.arrows -= 1
        print(f"Archer shoots.. {self.arrows} arrows left!")

# wizard = Wizard(50)
# wizard.walk()

# archer = Archer(100, 5)
# archer.shoot()
# archer.shoot()

# x = {"test": 123}
# print(x)
# x["test"] = 200
# print(x)

class NoUpdateDictionary(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError("Key already present")
        super().__setitem__(key, value)

y = NoUpdateDictionary()
y["key"] = 123
y["key"] = 200
print(y)