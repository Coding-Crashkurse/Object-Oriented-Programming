class Metaclass(type):

    def __call__(self, *args, **kwargs):
        print("__call__")
        return super().__call__(*args, **kwargs)

    @classmethod
    def __prepare__(metacls, name, bases):
        print("__prepare__")
        return {"hp": 100, "mana": 100}

    def __new__(metacls, name, bases, namespace):
        print("__new__")
        print(namespace)
        return super().__new__(metacls, name, bases, namespace)



class SingleTon(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("__call__ in singleton")
        if not cls in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Archer(metaclass=SingleTon):

    def __init__(self, hp):
        self.hp = hp


archer = Archer(100)
archer2 = Archer(200)

print(archer2.hp)
# print(id(archer))
# print(id(archer2))


