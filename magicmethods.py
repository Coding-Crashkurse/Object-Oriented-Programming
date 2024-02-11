import uuid

class Archer:

    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self.arrows = arrows
        self._id = uuid.uuid4()

    def __str__(self):
        return f"Archer with {self.hp} hp and {self.mana} mana and {self.arrows} arrows"

    def __repr__(self):
        return f"Archer({self.hp}, {self.mana}, {self.arrows})"

    def __add__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        new_hp = self.hp + other.hp
        new_mana = self.mana + other.mana
        new_arrows = self.arrows + other.arrows
        return Archer(new_hp, new_mana, new_arrows)

    def __eq__(self, other):
        if not isinstance(other, Archer):
            return False
        return self.hp == other.hp and self.mana == other.mana

    def __gt__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.hp > other.hp

    def __hash__(self):
        return hash(self._id)

    # def __lt__(self, other):
    #     if not isinstance(other, Archer):
    #         return NotImplemented
    #     return self.hp == other.hp

# archer1 = Archer(100, 100, 6)
# archer2 = Archer(100, 100, 5)
# # print(archer1 < archer2)
# archer1.mana = 200
# print(hash(archer1))
# archer1.mana = 100
# print(hash(archer1))


# new_dict = {archer1: "test"}

class Company:
    def __init__(self, size):
        self.size = size
        self.archers = []

    def add_archer(self, archer):
        if not isinstance(archer, Archer):
            raise TypeError("Only Archers allowed")
        if len(self.archers) > self.size:
            raise ValueError("Company already full")
        self.archers.append(archer)

    def __add__(self, other):
        if not isinstance(other, Archer):
            raise TypeError("Only adding Archers allowed")
        self.add_archer(other)
        return self

    def __iter__(self):
        return iter(self.archers)


archer2 = Archer(100, 100, 5)
company = Company(5)
newcompany = company + archer2 + archer2 + archer2

for archer in newcompany:
    print(archer)
