# class A:
#     def sayhi2(self):
#         print("Hello from A")
#
# class B(A):
#     def sayhi2(self):
#         print("Hello from B")
#
# class C(A):
#     def sayhi2(self):
#         print("Hello from C")
#
# class D(C, B):
#     pass
#
# d = D()
# d.sayhi()

import json

class Archer:
    def __init__(self, hp):
        self.hp = hp

    def walk(self):
        return "I am walking"

class JsonMixin:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class SuperWalkMixin:
    def walk(self):
        return f"{super().walk()} extemely fast!"

class SuperArcher(JsonMixin, SuperWalkMixin, Archer):
    pass

a = SuperArcher(100)
print(a.walk())
print(a.toJSON())