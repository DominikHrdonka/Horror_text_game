class Items:
    def __init__(self, name) -> None:
        self.name = name

    def __add__(self, other):
        if self.name == "pliers" and other.name == "clip":
            return picklock("picklock")



class Weapons(Items):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power
            
### Items instances
key = Items("key")
pliers = Items("pliers")
clip = Items("clip")
picklock = Items("picklock")

### Weapons instances
scalpel = Weapons("scalpel", 2)
axe = Weapons("axe", 7)