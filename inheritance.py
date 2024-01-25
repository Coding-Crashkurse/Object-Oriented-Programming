class BasePlayer:

    def __init__(self, hp):
        self.hp = hp

    def walk(self):
        print("Ich laufe...")


class Archer(BasePlayer):

    def __init__(self, hp, arrows):
        super().__init__(hp=hp)
        self.arrows = arrows


class Wizard(BasePlayer):
    pass

archer = Archer(100, 10)
wizard = Wizard(15)

archer.walk()
wizard.walk()
x = {"bla": 123}
x["bla"] = 122

class NoUpdateDictionary(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError("Key existiert bereits")
        super().__setitem__(key, value)

x = NoUpdateDictionary()
x["key"] = 123
x["key"] = 125
print(x)