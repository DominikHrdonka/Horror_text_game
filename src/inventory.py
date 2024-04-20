class Inventory:
    def __init__(self):
        self.__inventory = inventory
    
    ### Method to add items to inventory
    def add_item(self, item) -> None:
        self.__inventory.append(item)
    
    ### Removing items from inventory
    def remove_item(self, item):
        self.__inventory.remove(item)


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

inventory = Inventory()          
### Items instances
key = Items("key")
pliers = Items("pliers")
clip = Items("clip")
picklock = Items("picklock")

### Weapons instances
scalpel = Weapons("scalpel", 4)
axe = Weapons("axe", 7)
rusty_knife = Weapons("rusty_knife", 3)