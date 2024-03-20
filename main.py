from game import Game
from location import Location

def main():
    
    # Creating instances
    game = Game()
    dark_room = Location(name = "Dark Room", description = "As your eyes get used to the dark,\nyou start to distinguish a dark fram set on the opposite wall.\nA door! Next it there's a black shadow of a wardrobe lurking,\nsitting quietly. The walls are empty. The air heavy with dust.", choices = "open the door, open the wardrobe")

    # Defining current location
    game.current_location = dark_room
    # Actual game progress
    game.start_game()



if __name__ == "__main__":
    main()