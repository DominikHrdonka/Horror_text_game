class Location:
    def __init__(self, name, description, choices = "explore, quit"):
        self.name = name
        self.description = description
        self.choices = choices