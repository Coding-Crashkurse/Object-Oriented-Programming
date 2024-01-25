class Archer:

    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self.arrows = arrows

    def __str__(self):
        return f"Archer mit {self.hp} HP und {self.mana} MANA mit {self.arrows} Pfeilen"

    def __repr__(self):
        return f"Archer({self.hp}, {self.mana}, {self.arrows})"

    def __eq__(self, other):
        if not isinstance(other, Archer):
            return False
        return self.hp == other.hp and self.mana == other.mana

    def __gt__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.hp > other.hp

    def __ge__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.hp >= other.hp

    def __hash__(self):
        return hash((self.hp, self.mana, self.arrows))

archer1 = Archer(100, 50, 10)
archer2 = Archer(2100, 50, 90)

print(hash(archer1))

archers = {archer1: "Happy", archer2: "Depressed"}

class Company:
    def __init__(self, size):
        self.archers = []
        self.size = size
        self.index = 0

    def add_archer(self, archer):
        if not isinstance(archer, Archer):
            raise TypeError("Nur Archer in Company erlaubt")
        if len(self.archers) >= self.size:
            raise ValueError("Company bereits voll")
        self.archers.append(archer)

    def __add__(self, other):
        if not isinstance(other, Archer):
            raise TypeError("Nur Archer addieren erlaubt")
        new_company = Company(self.size)
        for archer in self.archers:
            new_company.add_archer(archer)
        new_company.add_archer(other)
        return new_company

    def __radd__(self, other):
        if not isinstance(other, Archer):
            raise TypeError("Nur Archer addieren erlaubt")
        return self + other

    def __iter__(self):
        return iter(self.archers)

    def __next__(self):
        if self.index > len(self.archers):
            raise StopIteration
        new_archer = next(self)
        self.index += 1
        return new_archer

x = 5 + 3

company = Company(3)
company = company + archer1
company = archer1 + company
print(company.archers)

for soldier in company:
    print(soldier)