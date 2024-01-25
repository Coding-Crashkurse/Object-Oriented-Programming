# Basisklasse A
class A:
    def action(self):
        return "Aktion von Klasse A"


# Basisklasse B
class B:
    def action(self):
        return "Aktion von Klasse B"


# Klasse C erbt von A und B
class C(A, B):
    def action(self):
        return super().action()


c = C()
print(c.action())


# Basisklasse D
class D:
    def action(self):
        return "Aktion von Klasse D"


# Klasse E erbt von B und D
class E(B, D):
    def action(self):
        return super().action() + ", dann E"


# Klasse F erbt von C und E
class F(C, E):
    def action(self):
        return super().action() + ", dann F"


# Objekt von Klasse F erstellen
f = F()

# Aktion ausführen
print(f.action())  # R


import json


class JsonMixin:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class SuperWalkMixin:
    def walk(self):
        return f"{super().walk()} extrem schnell"


class Archer:
    def __init__(self, hp):
        self.hp = hp

    def walk(self):
        return "Ich laufe..."


class SuperArcher(JsonMixin, SuperWalkMixin, Archer):
    pass


a = SuperArcher(100)
print(a.walk())
print(a.toJSON())
