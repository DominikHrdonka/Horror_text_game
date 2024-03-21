from game import Game
from location import Location
from items import Items
def main():
    
    # Creating instances of Game
    game = Game()

    # Creating instances of Location
    dark_room = Location(
        "dark room",
        "As your eyes get used to the dark,\nyou start to distinguish a dark frame set on the opposite wall.\nA door! Next to it there's a black shadow of a wardrobe lurking,\nsitting quietly. The walls are empty. The air heavy with dust.\nOne window set in a wall like a dead painting.",
        "The same old dark room. Mold on the walls, wet stink. Is that fear?",
        "go to the window, open the door, open the wardrobe"
        )

    wardrobe = Location(
        "wardrobe",
        "The wardrobe creaks. Awful smell gets out.\nYou feel sick and have to cover your nose.\nAs the shock passes, you notice something inside.\nA ragged doll with one eye. And there... a key!",
        "The wardrobe - a sad reminder of life long gone.",
        "take the key, examine the doll, close the wardrobe"
        )
    wardrobe_without_key = Location(
        "wardrobe without key",
        "The wardrobe - a sad reminder of life long gone.",
        "The wardrobe - a sad reminder of life long gone.",
        "examine the doll, close the wardrobe"
    )
    door = Location(
        "door",
        "Old wooden door. You wonder what's on the other side.",
        "The door - the only way out of here?",
        "open the door, go to the window, open the wardrobe"

    )
    unlocked_door = Location(
        "unlocked door",
        "The door - the only way out of here?",
        "The door - the only way out of here?",
        "go to the next room, go to the window, open the wardrobe"
    )
    window = Location(
        "window",
        "The glass is covered in cobwebs.\nYou try to see through but realize the window is coverd with planks from outside.\nYou can't see anything.",
        "The window - if only you could see outside...",
        "open the door, open the wardrobe"
    )

    kitchen = Location(
        "kitchen",
        "You are in a kitchen. The smell is even worse here.\nAnd you can see why. There is something in the sink.\nAll covered in blood that's also dripping on the floor.\nThe tiles of the kitchen are old and worn just as a green door on the left.\nYou can hear some rumbling behind it.",
        "Kitchen - with a massacred raccoon in the sink.",
        "examine the sink, go back to the room, examine the green door"
    )
    
    sink = Location(
        "sink",
        "The fur is painted by blackish red blood.\nYou lean over the dead animal, trying to make out what it is.\n Probably a rackoon, by the sad sight of it. And rather massacred one.\nWho did this? And why?\nYou notice a rusty scalpel in the sink.",
        "The bloody sink - it makes no sense.",
        "take the scalpel, turn away"

    )

    kitchen_without_scalpel = Location(
        "kitchen without scalpel",
        "The scalpel will come in handy.\nNow, what about the green door? It seems to be opened",
        "The scalpel will come in handy.\nNow, what about the green door? It seems to be opened",
        "open the green door, go back to the room"

    )
    keyhole = Location(
        "keyhole",
        "The rumbling is definitely coming from the other side!\nYou can feel your heart pounding loudly in your chest. Too loudly.\nYou crouch down and slowly move your eye to the keyhole.\nThe keyhole is small but you can see the creature on the other side.\nIts chest is heaving up and down. Whatever it is, it is in pain.",
        "The keyhole – window to another world.",
        "talk to the creature, move away"
    )

    # Creating instances of Items
    key = Items("key")


    # Adding location to the game list of locations
    game.add_location("dark room", dark_room)
    game.add_location("wardrobe", wardrobe)
    game.add_location("window", window)
    game.add_location("door", door)
    game.add_location("unlocked door", unlocked_door)
    game.add_location("wardrobe without key", wardrobe_without_key)
    game.add_location("kitchen", kitchen)
    game.add_location("sink", sink)
    game.add_location("kitchen without scalpel", kitchen_without_scalpel)

    # Defining current location
    game.current_location = dark_room

    # Actual game progress
    game.start_game()



if __name__ == "__main__":
    main()