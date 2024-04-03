class Location:
    def __init__(self, name, description, description_next, choices):
        self.name = name
        self.description = description
        self.description_next = description_next
        self.choices = choices

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
    "The wardrobe creaks. Awful smell gets out.\nYou feel sick and have to cover your nose.\nAs the shock passes, you notice something inside.\nA ragged doll with one eye. And there... old pliers!",
    "The wardrobe - a sad reminder of life long gone.",
    "take the pliers, examine the doll, close the wardrobe"
    )
wardrobe_without_pliers = Location(
    "wardrobe without pliers",
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
    "The glass is covered in cobwebs.\nYou try to see through but realize the window is coverd with planks from outside.\nYou can't see anything except that there,\non the windowsill, there is a metal clip.",
    "The window - if only you could see outside...",
    "take the clip, open the door, open the wardrobe"
)

window_without_clip = Location(
    "window without clip",
    "The window - if only you could see outside...",
    None,
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
    "move to the desk, move to the remnants, go back to the steel door, quit"
)

old_remnants = Location(
    "old_remnants",
    "The rusty axe is thrust deep into the remnants of an old rack.\nOn the right, you see your ragged reflexion in a tall mirror.",
    "The axe is still stuck deeú in the wood",
    "take the axe, hide behind the rack, move to the mirror, quit"
)

old_remnants_without_axe = Location(
    "old_remnants_without_axe",
    "The old remnants with a vicious scar where the axe used to be",
    "The old remnants with a vicious scar where the axe used to be",
    "hide behind the rack, move to the mirror, quit"

)

mirror = Location(
    "mirror",
    "The mirror with several cracks distorts your shape\nas if you're a dim comic caricature. Ane perhaps you truly are.\nThis all seems like a nightmare anyway.\nThe mirror could be turned if needed. And there's a narrow passage\nbetween the racks and the right wall. In the dakr, you could sneak through without being seen.",
    "The cracked mirror and the passageway along the right wall.",
    "turn the mirror, enter the passageway, move to the remnants, quit"
)

desk_with_body = Location (
    "desk_with_body",
    "You feel sick. The body is awfully mutilated.\nHow many bodies are there anyway?\nYou notice little wheels at the desk's base. It is mobile.",
    "The mobile desk - could you use it somehow?",
    "push the desk, hide behind the rack, quit"
)

pushed_desk = Location (
    "pushed_desk",
    "The desk colided with the opposite wall.\nYou crouch behind the counter instead.",
    "The desk colided with the opposite wall.\nYou crouch behind the counter instead.",
    "hide behind the rack, quit"
)

passageway = Location(
    "passageway",
    "You squeeze yourself inbetween the racks and the ragged wall.\nIf you're careful enough, you can get to the at the end of the library undetected.\nIn the narrow passageway, everything stinks of mold and.\nAt the end, you can see a dim hole in the wall. Where is it going?",
    "The narrow passageway – an opportunity to get to the other side of the library.",
    "move to the mirror, climb through the hole"
)