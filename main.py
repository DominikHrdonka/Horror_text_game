from game import Game
from location import Location
from items import Items
def main():
    
    # Creating instances of Game
    game = Game()

    # Creating instances of Location
    dark_room = Location(
        "dark room",
        "As your eyes get used to the dark,\nyou start to distinguish a dark fram set on the opposite wall.\nA door! Next it there's a black shadow of a wardrobe lurking,\nsitting quietly. The walls are empty. The air heavy with dust.\nOne window set in a wall like a dead paiting",
        "go to the window, open the door, open the wardrobe"
        )

    wardrobe = Location(
        "wardrobe",
        "The wardrobe creaks. Awful smell gets out.\nYou feel sick and have to cover your nose.\nAs the shock passes, you notice something inside.\nA ragged doll with one eye. And there... a key!",
        "take the key, take the doll, close the wardrobe"
        )
    door = Location(
        "door",
        "Old wooden door. You wonder what's on the other side.",
        "open the door, go to the window, open the wardrobe"

    )
    window = Location(
        "window",
        "The glass is covered in cobwebs.\nYou try to see through but realize the window is coverd with planks from outside.\nYou can't see anything.",
        "open the door, open the wardrobe"
    )

    # Creating instances of Items
    key = Items("key")


    # Adding location to the game list of locations
    game.add_location("dark room", dark_room)
    game.add_location("wardrobe", wardrobe)
    game.add_location("window", window)
    game.add_location("door", door)

    # Defining current location
    game.current_location = dark_room

    # Actual game progress
    game.start_game()



if __name__ == "__main__":
    main()