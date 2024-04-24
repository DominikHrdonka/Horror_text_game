class Inventory:
    __inventory = []
    
    ### Method to add items to inventory
    @classmethod
    def add_item(cls, item) -> None:
        cls.__inventory.append(item)
    
    ### Removing items from inventory
    @classmethod
    def remove_item(cls, item):
        cls.__inventory.remove(item)

    ### Show what is is inventory
    @classmethod
    def get_inventory(cls):
        return cls.__inventory


class Items(Inventory):
    def __init__(self, name) -> None:
        self.name = name


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
scalpel = Weapons("scalpel", 4)
axe = Weapons("axe", 7)
rusty_knife = Weapons("rusty_knife", 3)