class Crone:
    def __init__(self) -> None:
        self._position = "center_library"
        self._health = ("##########")
        self._choices = {

        }

    def get_position(self):
        return self._position
    
    def set_position(self, new_position):
        self._position = new_position
        return self._position
    