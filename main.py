from game import Game
from location import Location
from items import Items
def main() -> None:
    
    # Creating instances of Game
    game = Game()

    # Creating instances of Location
    
    start = Location(
        "start",
        "",
        "",
        "explore, quit"
    )
    
    dark_room = Location(
        "dark room",
        "As your eyes get used to the dark,\nyou start to distinguish a dark frame set on the opposite wall.\nA door! Next to it there's a black shadow of a wardrobe lurking,\nsitting quietly. The walls are empty, except for black mold. The air heavy with dust.\nOne window set in a wall like a dead painting.",
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
        "Kitchen - with a bloody sink and a green door.",
        "examine the sink, go back to the room, examine the green door, examine the steel door"
    )
    
    sink = Location(
        "sink",
        "The fur is painted by blackish red blood.\nYou lean over the dead animal, trying to make out what it is.\n Probably a rackoon, by the sad sight of it. And rather massacred one.\nWho did this? And why?\nYou notice a rusty scalpel in the sink.",
        "The bloody sink - it makes no sense.",
        "take the scalpel, turn away"

    )
    sink_without_scalpel = Location(
        "sink without scalpel",
        "The bloody sink - it makes no sense",
        None,
        "turn away"
    )

    keyhole = Location(
        "keyhole",
        "The rumbling is definitely coming from the other side!\nYou can feel your heart pounding loudly in your chest. Too loudly.\nYou crouch down and slowly move your eye to the keyhole.\nThe keyhole is small but you can see the creature on the other side.\nIts chest is heaving up and down. Whatever it is, it is in pain.",
        "The keyhole – window to another world.",
        "talk to the creature, move away"
    )

    steel_door = Location(
        "steel_door",
        "The heavy door wouldn't budge even if you had a hammer.\nYou notice a keypad on the side though.\nIf you knew the right code, you might escape!",
        "The steel door and a keypad. What is the code?",
        "enter the code, move away"
    )
    steel_door_opened = Location(
        "steel_door_opened",
        "You feel a whif of old air enter from the other side.",
        "The steel door is opened",
        "enter the room, move away"
    )

    library = Location(
        "library",
        "Is that a library? The huge room spreads in front of you like a giant vault.\nThe dimness is pierced through shimmering light that's coming from above.\nA roof window! Way out of reach though.\nSomething catches your eye. As you lower your gaze, your heart skips a beat.\nBetween the racks of old books you see steel desks. And on them... Sheer madness!\nAn old crone is hunched over one of the bodies all over the place, her back turned to you.\nThere is a horriffic muttering coming from her. She hasn't noticed you yet.",
        "Library - books, bodies and sheer madness.",
        "hide behind the rack, go back to the kitchen, quit"
    )

    rack_one = Location(
        "rack_one",
        "The high shadow conceals your body. You hardly breath.\nAfter a while, you dare steal a careful peek. The crone in ragged dress,\nhands covered in blood, wild hair hanging along her skinny skull.\nThe body beneath her touch twitching. And the giant knife in her hand...\nOn the left, hidden from the sight of the crone, you notice a desk with another body.\nOn the right, a few meters away from the crone, there is an axe stuck in the rack.",
        "You crouch behind the rack. Breath stuck in your throat.",
        "move to the desk, move to the axe, go back to the steel door, quit"
    )

    stuck_axe = Location(
        "stuck_axe",
        "The rusty axe is thrust deep into the remnants of an old rack.",
        "The rusty axe is thrust deep into the remnants of an old rack.",
        "take the axe, hide behind the rack"
    )

    # Adding location to the game list of locations
    game.add_location("start", start)
    game.add_location("dark room", dark_room)
    game.add_location("wardrobe", wardrobe)
    game.add_location("window", window)
    game.add_location("door", door)
    game.add_location("unlocked door", unlocked_door)
    game.add_location("wardrobe without key", wardrobe_without_key)
    game.add_location("kitchen", kitchen)
    game.add_location("sink", sink)
    game.add_location("sink without scalpel", sink_without_scalpel)
    game.add_location("keyhole", keyhole)
    game.add_location("steel_door", steel_door)
    game.add_location("library", library)
    game.add_location("steel_door_opened", steel_door_opened)
    game.add_location("rack_one", rack_one)
    game.add_location("stuck_axe", stuck_axe)

    # Defining current location
    game.current_location = dark_room

    # Starting the game
    game.start_game()



if __name__ == "__main__":
    main()