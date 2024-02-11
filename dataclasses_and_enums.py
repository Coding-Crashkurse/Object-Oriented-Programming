class Bow:
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

bow_a = Bow("great bow", 100, 20)
print(bow_a)

from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Bow:
    name: str
    price: float
    damage: int

bow1 = Bow("zreat bow", 99.99, 20)
bow2 = Bow("great bow", "expensive", 20)

print(bow2)

from pydantic import BaseModel

class Bow(BaseModel):
    name: str
    price: float
    damage: int

bow1 = Bow(name="great bow", price="expensive", damage=20)

print(bow1)

from enum import Enum

class Weapons(Enum):
    S = "Sword"
    B = "Bow"
    A = "Axe"
    SWORD = "Sword"

bow = Weapons("Bow")
print(bow.S is bow.SWORD)

class Armory(BaseModel):
    rooms: int
    weapons: list[Weapons]

armory = Armory(rooms=3, weapons=["Axe", "Sword"])
print(armory.model_dump())