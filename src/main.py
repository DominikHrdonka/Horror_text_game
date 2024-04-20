from game import *
from location import *
from items import *

def main() -> None:
    

    # Defining current location
    game.current_location = dark_room

    # Starting the game
    game.start_game()



if __name__ == "__main__":
    main()