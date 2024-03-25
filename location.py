class Location:
    def __init__(self, name, description, description_next, choices = "explore, quit") -> None:
        self.name = name
        self.description = description
        self.description_next = description_next
        self.choices = choices