import time
import os
from inventory import *

### Global method to create separators between descr. and inputs ###
def separators() -> None:
    print("-" * 25)

### Global method to clear the terminal after every user input
def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


class Location:
    __current_location = None

    def __init__(self, name, choices, description=None, description_revisit=None):
        self.name = name
        self.description = description
        self.description_revisit = description_revisit
        self.choices = choices
        

    
    
    ### Method to add label to actions
    def label(self, give_label):
        separator_count = "-" * len(give_label)
        print(separator_count)
        print(f"{give_label}")
        print(separator_count)
    
    ### getting the current location
    @classmethod
    def get_current_location_choices(cls):
        return cls.__current_location.choices

    ### getting current location
    @classmethod
    def get_current_location_description(cls):
        return cls.__current_location.description
    
    ### getting curr. loc. when revisiting
    @classmethod
    def get_current_location_revisit(cls):
        return cls.__current_location.description_revisit

    ### method to change current location - loop until correct input
    @classmethod
    def change_location(cls, location) -> None:
        cls.__current_location = location
        

class Start(Location):
    def __init__(self, name, choices, description=None, description_revisit=None):
        super().__init__(name, choices, description, description_revisit)
    
    ### Exploring at the beginning of the game
    def explore(self) -> None:
        self.label("You decided to explore!")
        Location.change_location(dark_room)
        print(f"{Location.get_current_location_description()}")
        separators()


class DarkRoom(Location):
    def __init__(self, name, choices, description=None, description_revisit=None):
        super().__init__(name, choices, description, description_revisit)
    
    #### trying to open the locked door
    def open_dark_room_door(self) -> None:
        if picklock not in Inventory.get_inventory():
            self.label("You press the door handle!")
            print("But nothing happens.\nThe door is locked! ")
            Location.change_location(dark_room)
            separators()
        else:
            self.label("You unlocked the door with the picklock!")
            Location.change_location(dark_room_door_unlocked)

    ### opening the wardrobe
    def open_wardrobe(self) -> None:
        self.label("You opened the wardrobe!")
        if pliers not in Inventory.get_inventory():
            Location.change_location(wardrobe)
            print(f"{Location.get_current_location_description()}")
            separators()
        else:
            Location.change_location(wardrobe_without_pliers)
            print(f"{Location.get_current_location_description()}")
            separators()
    
    ### going to the window
    def go_window(self) -> None:
        self.label("You approach the window.")
        if clip not in Inventory.get_inventory():
            Location.change_location(dark_room_window)
            print(f"{Location.get_current_location_description()}")
            separators()
        else:
            Location.change_location(dark_room_window_without_clip)
            print(f"{Location.get_current_location_description()}")
            separators()
    
    def craft_picklock(self):
        print(f"You combined the {clip.name} and {pliers.name} and crafted a {picklock.name}!")
        Inventory.remove_item(clip)
        Inventory.add_item(picklock)
        separators()
    
    ### going to the kitchen
    def go_kitchen(self) -> None:
        self.label("You enter the room!")
        Location.change_location(kitchen)
        print(f"{Location.get_current_location_description()}")
        separators()

class DarkRoomWardrobe(Location):
    def __init__(self, name, choices, description=None, description_revisit=None):
        super().__init__(name, choices, description, description_revisit)
    
    ### examining the doll in the wardrobe
    def examine_doll(self) -> None:
        self.label("You pick up the doll.")
        print("The doll's empty eyes make you shudder.\nYou carefully take it it in your hands. A memory pops out.\nA dark memory screaming at you from within.\nA flash of a vision – you're in your room. She came for a visit.\nShe stinks from alcohol and for some reason you are scared.\nShe grins at you, her teeth rotten and disgusting...\nYou put the doll back in the wardrobe.")
        separators()

    ### closing the wardrobe
    def close_wardrobe(self) -> None:
        self.label("You closed the wardrobe.")
        Location.change_location(dark_room)
        print(f"{Location.get_current_location_revisit()}")
        separators()
    
    ### taking the pliers
    def take_pliers(self) -> None:
        self.label("You took the pliers!")
        Inventory.add_item(pliers)
        Location.change_location(wardrobe_without_pliers)
        if clip in Inventory.get_inventory():
            dark_room.craft_picklock()

class DarkRoomWindow(DarkRoom):
    def __init__(self, name, choices, description=None, description_revisit=None):
        super().__init__(name, choices, description, description_revisit)
    
    ###Taking the clip
    def take_clip(self):
        self.label("You took the clip!")
        Inventory.add_item(clip)
        Location.change_location(dark_room_window_without_clip)
        if pliers in Inventory.get_inventory():
            dark_room.craft_picklock()

class Kitchen(Location):
    def __init__(self, name, choices, description=None, description_revisit=None):
        super().__init__(name, choices, description, description_revisit)

    ##Examining the sink
    def examine_sink(self) -> None:
        self.label("You approach the sink.")
        if scalpel not in Inventory.get_inventory():    
            Location.change_location(sink)
            print(f"{Location.get_current_location_description()}")
            separators()
        else:
            Location.change_location(sink_without_scalpel)
            print(f"{Location.get_current_location_description()}")
            separators()
    
    ### Taking the scalpel
    def take_scalpel(self) -> None:
        self.label("You took the scalpel!")
        Inventory.add_item(scalpel)
        Location.change_location(sink_without_scalpel)
        print(f"{Location.get_current_location_description()}")
        separators()
    
    ### Turning away from the sink
    def turn_away(self) -> None:
        self.label("You turn away from the sink.")
        Location.change_location(kitchen)
        print(f"{Location.get_current_location_revisit()}")
        separators()

"""
INSTANCES OF LOCATION CLASSES
"""
start = Start(name="Start", choices={"1": "Explore"})

dark_room = DarkRoom(
    name="Dark room",
    description="As your eyes get used to the dark,\nyou start to distinguish a dark frame set on the opposite wall.\nA door! Next to it there's a black shadow of a wardrobe lurking,\nsitting quietly. The walls are empty, except for black mold. The air heavy with dust.\nOne window set in a wall like a dead painting.",
    description_revisit="The same old dark room. Mold on the walls, wet stink. Is that fear?",
    choices={
        "1": "Go to the window",
        "2": "Open the door",
        "3": "Open the wardrobe"
    }
    )



dark_room_door_unlocked = DarkRoom(
    name="Unlocked door",
    description="The door - the only way out of here?",
    choices={
        "1": "Go to the next room",
        "2": "Go to the window",
        "3": "Open the wardrobe"
    }


)

wardrobe = DarkRoomWardrobe(
    name="wardrobe",
    description="The wardrobe creaks. Awful smell gets out.\nYou feel sick and have to cover your nose.\nAs the shock passes, you notice something inside.\nA ragged doll with one eye. And there... old pliers!",
    description_revisit="The wardrobe - a sad reminder of life long gone.",
    choices={
        "1": "Take the pliers",
        "2": "Examine the doll",
        "3": "Close the wardrobe"
    }
    )
wardrobe_without_pliers = DarkRoomWardrobe(
    name="wardrobe without pliers",
    description="The wardrobe - a sad reminder of life long gone.",
    choices={
        "1": "Examine the doll",
        "2": "Close the wardrobe"
    }
)

dark_room_window = DarkRoomWindow(
    name="Window",
    description="The glass is covered in cobwebs.\nYou try to see through but realize the window is coverd with planks from outside.\nYou can't see anything except that there,\non the windowsill, there is a metal clip.",
    description_revisit="The window - if only could you see outside...",
    choices={
        "1": "Take the clip",
        "2": "Open the door",
        "3": "Open the wardrobe"
    }
)

dark_room_window_without_clip = DarkRoomWindow(
    name="Window without clip",
    description="The window - if only you could see outside...",
    choices={
        "1": "Open the door",
        "2": "Open the wardrobe"
    }
)



kitchen = Kitchen(
    name="Kitchen",
    description="You are in a kitchen. The smell is even worse here.\nAnd you can see why. There is something in the sink.\nAll covered in blood that's also dripping on the floor.\nThe tiles of the kitchen are old and worn just as a green door on the left.\nYou can hear some rumbling behind it.",
    description_revisit="Kitchen - with a bloody sink and a green door.",
    choices={
        "1": "Examine the sink",
        "2": "Go back to the room",
        "3": "Examine the green door",
        "4": "Examine the steel door"
    }
)

sink = Location(
    name="Sink",
    description="The fur is painted by blackish red blood.\nYou lean over the dead animal, trying to make out what it is.\n Probably a rackoon, by the sad sight of it. And rather massacred one.\nWho did this? And why?\nYou notice a rusty scalpel in the sink.",
    description_revisit="The bloody sink - it makes no sense.",
    choices={
        "1": "Take the scalpel",
        "2": "Turn away"
    }

)
sink_without_scalpel = Kitchen(
    name="sink without scalpel",
    description="The bloody sink - it makes no sense",
    choices={
        "1": "Turn away"
    }
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
    "Is that a library? The huge room spreads in front of you like a giant vault.\nThe dimness is pierced through shimmering light that's coming from above.\nA roof window! Way out of reach though.\nSomething catches your eye. As you lower your gaze, your heart skips a beat.\nBetween the racks of old books you see steel desks. And on them... Sheer madness!\nAn old crone is hunched over one of the bodies all over the place, her back turned to you.\nThere is a horriffic muttering coming from her. She hasn't noticed you yet.\nRight behind her on the other side of the room, there is a two-winged door.\n Is it your way out?",
    "Library - books, bodies and sheer madness. Could you get through the big door?",
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

service_room = Location(
    "service_room",
    "You find yourself in an old service room. There is a rusty fuse box on the wall.\nSome garbage in the corner. A dusted computer. Door, most likely leading to the library.",
    "The old service room – not much left but something could be useful.",
    "enter the passageway, examine the fuse box, use the computer, examine the garbage, enter the library"
)

fuse_box = Location(
    "fuse_box",
    "The old fuse box is covered with cobwebs. There's a silent buzz coming out from it.\nCould it be still functional?",
    "The old fuse box – still working",
    "switch the button, look away"
)

library_back = Location(
    "library_back",
    "You are in the front of the library. The two-wing door stand just right before you.\nThat's the only way out. The crone is far enough.\nDon't hesitate!",
    "Front of the library – so close to the main entrance!",
    "open the big door, enter the service room"
)