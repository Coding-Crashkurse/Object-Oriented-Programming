# class Bogen:
#     def __init__(self, name, preis, schaden):
#         self.name = name
#         self.preis = preis
#         self.schaden = schaden
#
# bogen_a = Bogen("Toller Bogen", 500, 90)

from dataclasses import dataclass

# @dataclass
# class Bogen:
#     name: str
#     preis: float
#     schaden: int = 100
#
# @dataclass
# class MagicBogen(Bogen):
#     mcg_dmg: int = 200
#
# bogen1 = Bogen("Standard Bogen", 500, 90)
# bogen2 = MagicBogen("Standard Bogen", 500, "fehler")
#
# print(bogen2)

from pydantic import BaseModel
#
# class Bogen(BaseModel):
#     name: str
#     preis: float
#     schaden: int = 100
#
# Bogen(name="testbogen", preis=500, schaden="fehler")


from enum import Enum, unique

class Waffen(Enum):
    S = "Schwert"
    B = "Bogen"
    A = "Axt"


from pydantic import BaseModel

class Waffenkammer(BaseModel):
    zimmer: int
    waffen: list[Waffen]

kammer = Waffenkammer(zimmer=3, waffen=["Schwerter", "Axt"])


class Auto:
    def __init__(self, farbe, ps):
        self.farbe = farbe
        self.ps = ps

    def gas_geben(self):
        print("Brumm brumm")

rotes_auto = Auto(farbe="rot", ps=200)
blaues_auto = Auto(farbe="blau", ps=200)
gruenes_auto = Auto(farbe="gruen", ps=200)