class Items:
    def __init__(self, name) -> None:
        self.name = name

    def __add__(self, other):
        pass

class Weapons(Items):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power
            

key = Items("key")
scalpel = Weapons("scalpel", 2)
axe = Weapons("axe", 7)