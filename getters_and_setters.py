# class Archer:
#
#     def __init__(self, hp):
#         self._hp = hp
#
#     def get_hp(self):
#         return self._hp
#
#     def set_hp(self, value):
#         self._hp = value
#
#     hp = property(fget=get_hp, fset=set_hp)

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
            print("Berechnung wird durchgeführt")
            self._overall_damage = self.dmg * self.crit
        return self._overall_damage


archer = Archer(100, 50)
print(archer.overall_damage)
archer.dmg = 500
print(archer.overall_damage)
print(archer.overall_damage)
