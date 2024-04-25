class Crone:
    def __init__(self) -> None:
        self.__position = "center_library"
        self.__health = ("[##########]")
        self.__choices = {
            "1": "center_library",
            "2": "at_the_desk",
            "3": "approaching_mirror",
            "4": "approaching_service_room"
        }

    def get_position(self):
        return self.__position
    
    def set_position(self, new_position):
        self.__position = new_position
        return self.__position
    
crone = Crone()