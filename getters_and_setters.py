class Archer:
    def __init__(self, hp):
        self._hp = hp

    def get_hp(self):
        print("Getter called")
        return self._hp

    def set_hp(self, value):
        if value > 200:
            raise ValueError("HP can be 200 at max!")
        print("Setter called")
        self._hp = value

    hp = property(fget=get_hp, fset=set_hp)


archer1 = Archer(100)
archer1._hp = 201
print(archer1.hp)

import time

class Archer:
    def __init__(self, hp, dmg):
        self._hp = hp
        self._dmg = dmg
        self.crit = 1.3
        self._overall_damage = None

    @property
    def dmg(self):
        return self._dmg

    @dmg.setter
    def dmg(self, value):
        self._overall_damage = None
        self._dmg = value

    @property
    def overall_damage(self):
        if self._overall_damage is None:
            print("Compute...")
            time.sleep(3)
            self._overall_damage = self.dmg * self.crit
        else:
            print("Using cache")
        return self._overall_damage

    @overall_damage.setter
    def overall_damage(self, value):
        raise ValueError("Changing overall damage not allowed")


archer1 = Archer(100, 20)
archer1._overall_damage = 35
