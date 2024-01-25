class Archer:
    def __init__(self, hp):
        self.hp = hp

    def walk(self):
        return "Ich laufe..."

    def attack(self):
        return "I shoot an arrow!"


class Knight:
    def __init__(self, hp):
        self.hp = hp

    def walk(self):
        return "I march forward!"

    def attack(self):
        return "I swing my sword!"


class CharacterFactory:
    def create_character(self, type, hp):
        if type == "Archer":
            return Archer(hp)
        elif type == "Knight":
            return Knight(hp)
        else:
            raise ValueError("Unknown character type")


# Usage
factory = CharacterFactory()
archer = factory.create_character("Archer", 100)
knight = factory.create_character("Knight", 150)

# Testing the created characters
print(archer.walk())  # "Ich laufe..."
print(archer.attack())  # "I shoot an arrow!"
print(knight.walk())  # "I march forward!"
print(knight.attack())  # "I swing my sword!"

###############################


class AttackStrategy:
    def execute(self):
        pass


class BowAttack(AttackStrategy):
    def execute(self):
        return "Shoot an arrow"


class CrossbowAttack(AttackStrategy):
    def execute(self):
        return "Shoot a crossbow bolt"


class Archer:
    def __init__(self, hp, strategy):
        self.hp = hp
        self.strategy = strategy

    def attack(self):
        return self.strategy.execute()


# Usage
archer = Archer(100, BowAttack())
print(archer.attack())
archer.strategy = CrossbowAttack()
print(archer.attack())

################################################################


class Observer:
    def update(self, subject):
        pass


class King(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, subject):
        print(
            f"{self.name} received update from {subject.__class__.__name__}: New HP is {subject.hp}"
        )


class Knight:
    def __init__(self, hp):
        self.hp = hp
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_hp(self, hp):
        self.hp = hp
        self.notify()


# Usage
knight = Knight(100)
king_arthur = King("King Arthur")
king_richard = King("King Richard")

knight.attach(king_arthur)
knight.attach(king_richard)

knight.set_hp(90)
