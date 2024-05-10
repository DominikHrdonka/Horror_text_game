import time
import os
from inventory import *
from dialogues import creature
from crone import *

### Global method to create separators between descr. and inputs ###
def separators() -> None:
    print("-" * 25)

### Global method to clear the terminal after every user input
def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


class Location:
    """
    parent class of all Location subclasses.
    
    class variables: 
    - current location: to keep track of current location
    - last location: to keep track of last current location when interacting
    with invenotry
    - knowledge: simple list of information, that allows further interactions.
    e.g. when discovering some locations or items.

    """
    __current_location = None
    __last_location = None
    __knowledge = []

    def __init__(self, name, choices, description=None, description_revisit=None):
        self.name = name
        self.description = description
        self.description_revisit = description_revisit
        self.choices = choices
    
    ### add label to actions
    def label(self, give_label):
        separator_count = "-" * len(give_label)
        print(separator_count)
        print(f"{give_label}")
        print(separator_count)
    
    ### get current location choices for getting input
    @classmethod
    def get_current_location_choices(cls):
        return cls.__current_location.choices
    
    ### get current location variable for invenotry interactions
    @classmethod
    def get_current_location_varibale(cls):
        return cls.__current_location

    ### get current location description
    @classmethod
    def get_current_location_description(cls):
        return cls.__current_location.description
    
    ### get current location revisit description
    @classmethod
    def get_current_location_revisit(cls):
        return cls.__current_location.description_revisit

    ###change current location
    @classmethod
    def change_location(cls, location) -> None:
        cls.__current_location = location

    ### get last location for inventory interactions
    @classmethod
    def get_last_location(cls):
        return cls.__last_location
    
    ### set last location for inventory interactions
    @classmethod
    def set_last_location(cls, location):
        cls.__last_location = location

    ### add knowledge to the list
    @classmethod
    def add_knowledge(cls, knowledge):
        cls.__knowledge.append(knowledge)

    ### get list of knowledge
    @classmethod
    def get_knowledge(cls):
        return cls.__knowledge

class BrowsingInventory(Location):
    def __init__(self, name, choices, description=None, description_revisit=None):
        super().__init__(name, choices, description, description_revisit)
    
    ### Opening the inventory
    def open_inventory(self) -> None:
        Location.set_last_location(Location.get_current_location_varibale())
        Location.change_location(inventory)
        if Inventory.get_inventory():
            Location.change_location(inventory)
            self.label("Your inventory contains:")
            for item in Inventory.get_inventory():
                print(f"{item.name}")
            separators()
            self.update_invetory_choices()
        else:
            self.label("The inventory is empty.")

    ### Closing the inventory
    def close_inventory(self):
        Location.change_location(Location.get_last_location())
        print(f"{Location.get_current_location_description()}")
        separators()

            
    ### Method to update inventory choices to craft new items
    def update_invetory_choices(self):
        if pliers in Inventory.get_inventory() and clip in Inventory.get_inventory():
            print(f"You can craft {picklock.name}!!!")
            self.choices["2"] = "Craft a picklock"
            separators()
        if old_cable in Inventory.get_inventory() and scalpel in Inventory.get_inventory():
            self.choices["2"] = "Cut off the old cable rubber"

    
    def craft_picklock(self):
        print(f"You combined the {clip.name} and {pliers.name} and crafted a {picklock.name}!")
        Inventory.remove_item(clip)
        Inventory.add_item(picklock)
        del self.choices["2"]
        separators()
    
    def cut_off_rubber(self):
        self.label(f"You used the {scalpel.name} to cut the old rubber off the {old_cable.name}!")
        print("You expose a few tiny wires. Luckily they are rust-free.")
        Inventory.remove_item(old_cable)
        Inventory.add_item(cable)
        del self.choices["2"]
        fuse_box_open.choices["3"] = "Connect the cable"
        separators()
            
    ### Method to show available inventory choices
    def get_inventory_choices(self):
        self.update_invetory_choices()
        inventory_choices = ""
        for value in self.inventory_choices.values():
            inventory_choices += f"{value}, "
        return inventory_choices.rstrip(", ")
        

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
        Location.change_location(wardrobe)
        if pliers not in Inventory.get_inventory():
            print(f"{Location.get_current_location_description()}")
            separators()
        else:
            print(f"{Location.get_current_location_revisit()}")
            separators()
    
    ### going to the window
    def go_window(self) -> None:
        self.label("You approach the window.")
        if clip not in Inventory.get_inventory() and picklock not in Inventory.get_inventory():
            Location.change_location(dark_room_window)
            print(f"{Location.get_current_location_description()}")
            separators()
        else:
            Location.change_location(dark_room_window_without_clip)
            print(f"{Location.get_current_location_description()}")
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
        del wardrobe.choices["3"]

class DarkRoomWindow(DarkRoom):
    def __init__(self, name, choices, description=None, description_revisit=None):
        super().__init__(name, choices, description, description_revisit)
    
    ###Taking the clip
    def take_clip(self):
        self.label("You took the clip!")
        Inventory.add_item(clip)
        Location.change_location(dark_room_window_without_clip)
        

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
    
     ### getting back to the dark room
    def go_back_room(self) -> None:
        self.label("You go back to the dark room.")
        Location.change_location(dark_room_door_unlocked)
        print(f"{Location.get_current_location_description()}")
        separators()
    
    ### Examining the steel door
    def examine_steel_door(self):
        self.label("You approach the steel door.")
        Location.change_location(steel_door)
        Location.add_knowledge("keypad discovered")
        print(f"{Location.get_current_location_description()}")
        separators()
    
     ### Entering the code
    def enter_code(self):
        self.label("The screen is blank, the keys worn out.")
        code = input("Enter the code: ")
        clear()
        if code == "571":
            self.label("The keypad light turns green!")
            Location.change_location(steel_door_opened)
            print(f"{Location.get_current_location_description()}")
            separators()
        else:
            print("Invalid code")
            separators()
    
    ### Examining the green door
    def examine_green_door(self) -> None:
        self.label("You approach the green door.")
        Location.change_location(keyhole)
        print(f"{Location.get_current_location_description()}")
        separators()
    
    ########Talking to the creature: dialogue########
    def talk_to_creature(self) -> None:

        def dialogue_pause() -> None:
            time.sleep(2)

        def play_dialogue(dialogue_key) -> None:
            dialogue = creature[dialogue_key]
            for line in dialogue["lines"]:
                print(line)
                dialogue_pause()
            while True:
                try:
                    if "options" in dialogue:
                        print("------------------")
                        for option_key, (option_text, _) in dialogue["options"].items():
                            print(f"{option_key}. {option_text}")
                        print("------------------")
                        choice = input("Choose an option: ")
                    else:
                        False

                    if choice in dialogue["options"]:
                        next_dialogue_key = dialogue["options"].get(choice)[1]
                        play_dialogue(next_dialogue_key)
                    else:
                        raise ValueError("Invalid dialogue choice")
                
                except ValueError as e:
                    print("--------------")
                    print(f"{e}")
                    print("--------------")     
                
        if "revisiting creature" not in Location.get_knowledge():
            Location.add_knowledge("revisiting creature")
            play_dialogue("start")
        else:
            if "keypad discovered" not in Location.get_knowledge():
                print(">>Leave me alone!<<")
                separators()
            else:
                play_dialogue("code_answer")

    ### Going to the library 
    def go_library(self):
        self.label("The vast room reveals in front of you.")
        Location.change_location(enter_library)
        print(f"{Location.get_current_location_description()}")
        separators()

class Library(Location):
    def __init__(self, name, choices, description=None, description_revisit=None):
        super().__init__(name, choices, description, description_revisit)
    

    ### Hiding behin the first rack
    def hide_behind_rack(self):
        self.label("You slip behind the rack on the left.")
        Location.change_location(library_rack)
        print(f"{Location.get_current_location_description()}")
        separators()
    
    ### Going back to the kitchen from the library
    def go_back_kitchen(self) -> None:
        self.label("You slip back through the steel door.")
        Location.change_location(kitchen)
        print(f"{Location.get_current_location_revisit()}")
        separators()

    ### go to the desk in library
    def go_desk(self):
        if "desk pushed" not in Location.get_knowledge():
            self.label("You approach the bloody desk.")
            Location.change_location(desk_with_body)
            print(f"{Location.get_current_location_description()}")
            separators()
        else:
            self.label("The desk has been pushed away.")
            Location.change_location(pushed_desk)
            print(f"{Location.get_current_location_revisit()}")
            if crone.get_position() == "at the desk":
                print("The crone is examining the desk and body, hissing and twitching with rage.")
            separators()

    ### Push desk in library to distract crone
    def push_desk(self):
        self.label("The desk moves usrpisingly smoothly.")
        print("The wheels squeek and soon the desk hits the rack on the opposite wall.\nFrom the center of the library, there comes a terrible hiss.\nThen heavy steps, and the sound of cloth sweeping on the floor.\nThe crone is on the move! She's gone to inspect the fuss at the opposite side.\n")
        Location.change_location(pushed_desk)
        Location.add_knowledge("desk pushed")
        crone.set_position("at the desk")
        separators()
    
    ### Moving to the stuck axe
    def go_remnants(self) -> None:
        if crone.get_position() != "approaching_mirror":    
            if axe not in Inventory.get_inventory():
                self.label("You sneak up to the old remnants.")
                Location.change_location(old_remnants)
                print(f"{Location.get_current_location_description()}")
                separators()
            else:
                self.label("You sneak up to the old remnants.")
                Location.change_location(old_remnants_without_axe)
                print(f"{Location.get_current_location_description()}")
                separators()
        else:
            self.label("The crone would see you. You can't go there!")
    
    ### Take axe
    def take_axe(self) -> None:
        if crone.get_position() == "center_library":
            print("-----------------------------------")
            print("Removing the axe will make a noise.\nYou don't dare trying when the crone is so close.\nPerhaps you could lure her away?")
            print("-----------------------------------")
        else:
            self.label("You grab the axe handle.")
            print("\nYour muscles tense up as you pull.\nFinally, as the wood creaks, you successfully remove the axe.")
            Inventory.add_item(axe)
            Location.change_location(old_remnants_without_axe)
            separators()
    
    def go_mirror(self):
        self.label("You approach the mirror.")
        Location.change_location(mirror)
        print(f"{Location.get_current_location_description()}")
        separators()

    ### Turning the mirror
    def turn_mirror(self):
        self.label("You turn the mirror.")
        if crone.get_position() != "approaching_mirror":
            if crone.get_position() == "center_library" or crone.get_position()== "approaching_service_room":
                print("""
As the cracked glass catches the dim sunlight coming from the roof window
reflection gets thrown at the center of the library.
The light falls right on the crone.
There is a furious roar, inhuman and ears-piercing.
You manage to slip behind the rack next to the mirror right in time.
The steps are approaching, the hissing grows."
""")
                separators()
                crone.set_position("approaching_mirror")
            else:
                print("""
As the cracked glass catches the dim sunlight coming from the roof window
reflection gets thrown at the center of the library.
Nothing happens. Well, you don't even know what you expected.
""")
                separators()
        else:
            print("The mirror is already turned and the crone is coming to you! Get lost!")
            separators()
    
    ### Enter the passageway
    def go_passageway(self)-> None:
        self.label("You enter the passageway.")
        Location.change_location(passageway)
        if "revisiting_passgw" not in Location.get_knowledge():
            print(f"{Location.get_current_location_description()}")
            Location.add_knowledge("revisiting_passgw")
            separators()
        else:
            print(f"{Location.get_current_location_revisit()}")
            separators()
    
    ### Entering the service room
    def climb_through_hole(self)-> None:
        self.label("You climb through the hole.")
        Location.change_location(service_room)
        if "revisitting_servicer" not in Location.get_knowledge():
            print(f"{Location.get_current_location_description()}")
            separators()
            Location.add_knowledge("revisitting_servicer")
        else:
            print(f"{Location.get_current_location_revisit()}")
            separators()
    
    def enter_service_room(self):
        self.label("You enter the service room")
        Location.change_location(service_room)
        print(f"{Location.get_current_location_revisit()}")

     ### Open main door from library
    def open_two_wing_door(self):
        self.label("You lean on the heavy door.")
        Location.change_location(corridor_behind_library)
        Location.get_current_location_description()
        separators()

class ServiceRoom(Location):
    def __init__(self, name, choices, description=None, description_revisit=None):
        super().__init__(name, choices, description, description_revisit)
    
        ###Examine the fuse box
    def examine_fuse_box(self)-> None:
        if "fuse_box_is_open" not in Location.get_knowledge():
            self.label("You approach the fuse box.")
            Location.change_location(fuse_box_closed)
            if "revisiting_fuse" not in Location.get_knowledge():
                print(f"{Location.get_current_location_description()}")
                separators()
                Location.add_knowledge("revisiting_fuse")
            else:
                print(f"{Location.get_current_location_revisit()}")
                separators()
        else:
            fuse_box_closed.open_fuse_box()
    
    ###Look away from the fuse box
    def look_away(self)-> None:
        self.label("You look away.")
        Location.change_location(service_room)
        print(f"{Location.get_current_location_revisit()}")
        separators()

    
    ### Open closed fuse box
    def open_fuse_box(self):
        if "fuse_box_is_open" not in Location.get_knowledge():
            if axe in Inventory.get_inventory():
                self.label("You thrust the axe in the lid gap.")
                Location.change_location(fuse_box_open)
                print(f"{Location.get_current_location_description()}")
                Location.add_knowledge("fuse_box_is_open")
                separators()
            else:
                self.label("You try to open the lid.")
                print("\nIt won't budge. You need to find some tool.\n")
                separators()
        else:
            self.label("You open the lid.")
            Location.change_location(fuse_box_open)
            #Condition to show a new choice if crafted cable in Inventory
            print(f"{Location.get_current_location_revisit()}")
            separators()
    
    ### Switch fuse box button
    def switch_button(self)-> None:
        self.label("You switch the button.")
        if "button_functional" in Location.get_knowledge():

            print("""
There is a spark.
From below the door you see light entering the service room.
And with the light, there comes a shriek. The crone's coming here!
""")
            crone.set_position("approaching_service_room")
            separators()
        else:
            print("\nNothing happens. The switch is dead. A cable is missing\n")
            separators()

    ### Connect crafted cable to fuse box
    def connect_cable(self):
        self.label("You connected the cable!")
        print("\nThe little light in the fuse box flickers green and stays on.\n")
        Location.add_knowledge("button_functional")
        del self.choices["3"]
        separators()

    
    ### Use the computer
    def use_computer(self)-> None:
        self.label("You press the power button.")
        print("\nNothing happens. the machine is long dead.\n")
        separators()

    ### Examine the garbage
    def examine_garbage(self)-> None:
        self.label("You approach the garbage.")
        print(
            """
Old carton boxes, some wires, papershreds...
Oh, look, a rusty knife and old piece of cable!
That could come in handy. You take both.
"""
)
        separators()
        Inventory.add_item(rusty_knife)
        Inventory.add_item(old_cable)
    
    ### Enter library from service room
    def enter_library(self):
        if crone.get_position() == "approaching_service_room":
            self.label("You can't go there now, you'd bump right into the crone!")
        elif crone.get_position() == "at_the_desk":
            self.label("You slowly open the door but close it immediately.")
            print("""
The crone standing at the desk would see you right away.
You need to lure her off.
""")
        else:
            self.label("You enter the library")
            Location.change_location(library_back)
            print(Location.get_current_location_description())
            separators()
    
    
class CorridorChase(Location):
    def __init__(self, name, choices, description=None, description_revisit=None):
        super().__init__(name, choices, description, description_revisit)
    
    def run_in_corridor(self):
        Location.change_location(wardrobe_in_corridor)
        Location.get_current_location_description()
        separators()

"""
INSTANCES OF LOCATION CLASSES
"""

inventory = BrowsingInventory(
    name="Inventory",
    choices={
        "1": "Close inventory"
    }
)

start = Start(
    name="Start",
    choices={
        "1": "Explore"
    }
)

dark_room = DarkRoom(
    name="Dark room",
    description="""
As your eyes get used to the dark,
you start to distinguish a dark frame set on the opposite wall.
A door! Next to it there's a black shadow of a wardrobe lurking, sitting quietly.
The walls are empty, except for black mold. The air heavy with dust.
One window set in a wall like a dead painting.
""",
    description_revisit="""
The same old dark room. Mold on the walls, wet stink. Is that fear?
""",
    choices={
        "1": "Go to the window",
        "2": "Open the door",
        "3": "Open the wardrobe",
        "i": "Open inventory"
    }
    )



dark_room_door_unlocked = DarkRoom(
    name="Unlocked door",
    description="""
The door - the only way out of here?
""",
    choices={
        "1": "Go to the next room",
        "2": "Go to the window",
        "3": "Open the wardrobe",
        "i": "Open inventory"
    }


)

wardrobe = DarkRoomWardrobe(
    name="wardrobe",
    description=
"""
The wardrobe creaks. Awful smell gets out.
You feel sick and have to cover your nose.
As the shock passes, you notice something inside.
A ragged doll with one eye. And there... old pliers!
""",
    description_revisit="\nThe wardrobe - a sad reminder of life long gone.\n",
    choices={
        "1": "Examine the doll",
        "2": "Close the wardrobe",
        "3": "Take the pliers",
        "i": "Open inventory"
    }
    )


dark_room_window = DarkRoomWindow(
    name="Window",
    description="""
The glass is covered in cobwebs.
You try to see through but realize the window
is coverd with planks from outside.
You can't see anything except that there,
on the windowsill, there is a metal clip.
""",
    description_revisit="""
The window - if only could you see outside...
    """,
    choices={
        "1": "Take the clip",
        "2": "Open the door",
        "3": "Open the wardrobe",
        "i": "Open inventory"
    }
)

dark_room_window_without_clip = DarkRoomWindow(
    name="Window without clip",
    description="""
The window - if only you could see outside...
""",
    choices={
        "1": "Open the door",
        "2": "Open the wardrobe",
        "i": "Open inventory"
    }
)


kitchen = Kitchen(
    name="Kitchen",
    description="""
You are in a kitchen. The smell is even worse here.
And you can see why. There is something in the sink.
All covered in blood that's also dripping on the floor.
The tiles of the kitchen are old and worn just as a green door on the left.
You can hear some rumbling behind it.
""",
    description_revisit="""
Kitchen - with a bloody sink and a green door.
""",
    choices={
        "1": "Examine the sink",
        "2": "Go back to the room",
        "3": "Examine the green door",
        "4": "Examine the steel door",
        "i": "Open inventory"
    }
)

sink = Location(
    name="Sink",
    description="""
The fur is painted by blackish red blood.
You lean over the dead animal, trying to make out what it is.
Probably a rackoon, by the sad sight of it. And rather massacred one.
Who did this? And why?
You notice a rusty scalpel in the sink.
""",
    description_revisit="""
The bloody sink - it makes no sense.
""",
    choices={
        "1": "Take the scalpel",
        "2": "Turn away",
        "i": "Open inventory"
    }

)
sink_without_scalpel = Kitchen(
    name="sink without scalpel",
    description="""
The bloody sink - it makes no sense
""",
    choices={
        "1": "Turn away",
        "i": "Open inventory"
    }
)

keyhole = Kitchen(
    name="keyhole",
    description="""
The rumbling is definitely coming from the other side!
You can feel your heart pounding loudly in your chest. Too loudly.
You crouch down and slowly move your eye to the keyhole.
The keyhole is small but you can see the creature on the other side.
Its chest is heaving up and down. Whatever it is, it is in pain.
""",
    description_revisit="""
The keyhole – window to another world.
""",
    choices={
        "1": "Talk to the creature",
        "2": "Turn away",
        "i": "Open inventory"
    }
)

steel_door = Kitchen(
    name="steel_door",
    description="""
The heavy door wouldn't budge even if you had a hammer.
You notice a keypad on the side though.
If you knew the right code, you might escape!
""",
    description_revisit="""
The steel door and a keypad. What is the code?
""",
    choices={
        "1": "Enter the code",
        "2": "Turn away",
        "i": "Open inventory"
    }
)
steel_door_opened = Kitchen(
    name="steel_door_opened",
    description="""
You feel a whif of old air enter from the other side.
""",
    description_revisit="""
The steel door is opened
""",
    choices={
        "1": "Enter the room",
        "2": "Turn away",
        "i": "Open inventory"
    }
)

enter_library = Library(
    name="library",
    description="""
Is that a library?
The huge room spreads in front of you like a giant vault.
The dimness is pierced through shimmering light that's coming from above.
A roof window! Way out of reach though.
Something catches your eye. As you lower your gaze, your heart skips a beat.
Between the racks of old books you see steel desks.
And on them... Sheer madness! An old crone is hunched over one of the bodies
all over the place, her back turned to you.
There is a horriffic muttering coming from her. She hasn't noticed you yet.
Right behind her on the other side of the room, there is a two-winged door.
Is it your way out?
""",
    description_revisit="""
Library - books, bodies and sheer madness.
Could you get through the big door?
""",
    choices={
        "1": "Hide behind the rack",
        "2": "Go back to the kitchen",
        "i": "Open inventory"
    }
)

library_rack = Library(
    name="Library rack",
    description="""
The high shadow conceals your body. You hardly breath.
After a while, you dare steal a careful peek. The crone in ragged dress,
hands covered in blood, wild hair hanging along her skinny skull.
The body beneath her touch twitching. And the giant knife in her hand...
On the left, hidden from the sight of the crone, you notice a desk with another body.
On the right, a few meters away from the crone, there is an axe stuck in the rack.
""",
    description_revisit="""
You crouch behind the rack. Breath stuck in your throat.
""",
    choices={
        "1": "Move to the desk",
        "2": "Move to the remnants",
        "3": "Go back to the steel door",
        "i": "Open inventory"
    }
)

old_remnants = Library(
    name="Old remnants",
    description="""
The rusty axe is thrust deep into the remnants of an old rack.
On the right, you see your ragged reflexion in a tall mirror.
""",
    description_revisit="""
The axe is still stuck deep in the wood
""",
    choices={
        "1": "Take the axe",
        "2": "Hide behind the rack",
        "3": "Move to the mirror",
        "i": "Open inventory"
    }
)

old_remnants_without_axe = Library(
    name="old_remnants_without_axe",
    description="""
The old remnants with a vicious scar where the axe used to be
""",
    choices={
        "1": "Hide behind the rack",
        "2": "Move to the mirror",
        "i": "Open inventory"
    }

)

mirror = Library(
    name="mirror",
    description="""
The mirror with several cracks distorts your shape
as if you're a dim comic caricature. Ane perhaps you truly are.
This all seems like a nightmare anyway. The mirror could be turned if needed.
And there's a narrow passage between the racks and the right wall.
In the dakr, you could sneak through without being seen.
""",
    description_revisit="""
The cracked mirror and the passageway along the right wall.
""",
    choices={
        "1": "Move to the remnants",
        "2": "Turn the mirror",
        "2": "Enter the passageway",
        "i": "Open inventory"
    }
)

desk_with_body = Library (
    name="Desk with body",
    description="""
You feel sick. The body is awfully mutilated.
How many bodies are there anyway?
You notice little wheels at the desk's base. It is mobile.
""",
    description_revisit="""
The mobile desk - could you use it somehow?
""",
    choices={
        "1": "Push the desk",
        "2": "Hide behind the rack",
        "i": "Open inventory"
    }
)

pushed_desk = Library (
    name="Pushed desk",
    description=
"""
The desk colided with the opposite wall.
You crouch behind the counter instead.
""",
    description_revisit=
"""
The desk colided with the opposite wall.
You crouch behind the counter instead.
""",
    choices={
        "1": "Hide behind the rack",
        "i": "Open inventory"
    }
)

passageway = Library(
    name="passageway",
    description=
"""
You squeeze yourself inbetween the racks and the ragged wall.
If you're careful enough, you can get to the at the end of the library undetected.
In the narrow passageway, everything stinks of mold and.
At the end, you can see a dim hole in the wall. Where is it going?
""",
    description_revisit=
"""
The narrow passageway.
An opportunity to get to the other side of the library.
""",
    choices={
        "1": "Move to the mirror",
        "2" : "Climb through the hole"
    }
)

service_room = ServiceRoom(
    name="service_room",
    description="""
You find yourself in an old service room.
There is a rusty fuse box on the wall.
Some garbage in the corner. A dusted computer.
Door, most likely leading to the library.
""",
    description_revisit="""
The old service room – not much left but something could be useful.
""",
    choices={
        "1": "Enter the passageway",
        "2": "Examine the fuse box",
        "3": "Use the computer",
        "4": "Examine the garbage",
        "5": "Enter the library",
        "i": "Open inventory"
    }
)

fuse_box_closed = ServiceRoom(
    name="fuse_box_closed",
    description="""
The old fuse box is covered with cobwebs.
There's a silent buzz coming out from it.
Could it be still functional? Anyway, the rusty lid is stuck.
    """,
    description_revisit="""
The old fuse box – still working but closed.
""",
    choices={
        "1": "Open the lid",
        "2": "Look away",
        "i": "Open inventory"
    }
)

fuse_box_open = ServiceRoom(
    name="fuse_box_open",
    description= """
You pry the lid open. A rusty squeak shoots out in the room.
You blow off layers of dust from the control panel.
The little lightbulb is dead. Next to it, an old button.
""",
    description_revisit="""
The old fuse box – still working, lid open.
""",
    choices={
        "1": "Switch the button",
        "2": "Look away",
        "i": "Open inventory"
    }
)



library_back = Library(
    name="library_back",
    description="""
You are in the front of the library.
The two-wing door stand just right before you.
That's the only way out. The crone is far enough. Don't hesitate!
""",
    description_revisit="""
Front of the library – so close to the main entrance!
""",
    choices={
        "1": "Open the two-wing door",
        "2": "Enter the service room",
        "i": "Open inventory"
    }
)

corridor_behind_library = Location(
    name="corridor",
    description=
"""
You can feel it move a little bit. It's not enough though.
You gather all your strength and push harder. The door squeaks.
From behind you, you can hear a furious hiss.
Even harder you lean on the door, the gap slowly growing.
Heavy steps approaching, inhuman squeel tearing your ears.
>>For God's sake, come on!<<
Just as you feel the ominous presence at your back, you manage to push through.
You fall hard on the floor in a long dim corridor.
There is only one option now...
RUN!!!
""",
    choices={
        "1": "Run",
    }
)

wardrobe_in_corridor = CorridorChase(
    name="wardrobe_in_corridor",
    description="""
    You scramble up on your feet, stumbling forward you miss a serious blow.
    The crone roars in an undead scream. You run down the dim corridor,
    not knowing where it leads. In front of you, you distinguish an ominous shape.
    An old wardrobe leaning across the corridor. You can stop now!
    """,
    choices={
        "1": "Climb over the wardrobe",
        "2": "Climb under the wardrobe"
    }
)
