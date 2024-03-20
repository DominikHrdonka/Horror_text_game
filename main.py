from game import Game
from location import Location
def main():
    
    # Creating instances
    game = Game()
    dark_room = Location(
        "Dark Room",
        "As your eyes get used to the dark,\nyou start to distinguish a dark fram set on the opposite wall.\nA door! Next it there's a black shadow of a wardrobe lurking,\nsitting quietly. The walls are empty. The air heavy with dust.\nOne window set in a wall like a dead paiting",
        "go to the window, open the door, open the wardrobe"
        )

    wardrobe = Location(
        "wardrobe",
        "The wardrobe creaks. Awful smell gets out.\nYou feel sick and have to cover your nose.\nAs the shock passes, you notice something inside.\nA ragged doll with one eye. And there... a key!",
        "take the key, take the doll"
        )
    window = Location(
        "window",
        "The glass is covered in cobwebs.\nYou try to see through but realize the window is coverd with planks from outside.\nYou can't see anything.",
        "open the door, open the wardrobe"
    )


    # Adding location to the game list of locations
    game.add_location("dark room", dark_room)
    game.add_location("wardrobe", wardrobe)
    game.add_location("window", window)

    # Defining current location
    game.current_location = dark_room

    # Actual game progress
    game.start_game()



if __name__ == "__main__":
    main()