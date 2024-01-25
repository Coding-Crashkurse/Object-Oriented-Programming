class MetaClass(type):
    def __call__(self, *args, **kwargs):
        print("__call__ in MetaClass")
        return super().__call__(*args, **kwargs)

    @classmethod
    def __prepare__(metacls, name, bases):
        print("__prepare__ in MetaClass")
        return {"hp": 100, "mana": 100}

    def __new__(metacls, name, bases, namespace):
        print("__new__ in MetaClass")
        print(namespace)
        return super().__new__(metacls, name, bases, namespace)


class MyMetaClassExample(metaclass=MetaClass):
    def __init__(self):
        print("__init__ in MyMetaClassExample")


print("MyMetaClassExample instances:")
meta_a = MyMetaClassExample()


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("__call__ in Singleton")
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MySingletonExample(metaclass=Singleton):
    def __init__(self):
        print("__init__ in MySingletonExample")


print("\nMySingletonExample instances:")
singleton_a = MySingletonExample()
singleton_b = MySingletonExample()
print(id(singleton_a))
print(id(singleton_b))
