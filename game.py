import time
from location import Location
import os
from dialogues import creature
from crone import Crone
from items import *

crone = Crone()

 ### Global method to create separators between descr. and inputs ###
def separators() -> None:
    print("-" * 25)

### Global method to clear the terminal after every user input
def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

class Game:
    def __init__(self) -> None:
        self.game_over = False
        self.current_location = None
        self.locations = {}
        self.inventory = []
        self.knowledge = []
        self.inventory_choices = {
            "1": "exit"
        }
          
    #### Dictionary of all the choices and their methods ####
        self.choices = {            
                "explore": self.explore,
                "quit": self.quit,
                "open inventory": self.open_inventory,
                "open the wardrobe": self.open_the_wardrobe,
                "take the pliers": self.take_pliers,
                "examine the doll": self.examine_doll,
                "close the wardrobe": self.close_wardrobe,
                "go to the window": self.going_to_window,
                "take the clip": self.take_clip,
                "open the door": {"not have": self.open_the_locked_door, "have":self.open_door_with_picklock},
                "go to the next room": self.go_kitchen,
                "examine the sink": self.examine_sink,
                "go back to the room": self.go_back_room,
                "examine the green door": self.examine_green_door,
                "talk to the creature": self.talk_to_creature,
                "examine the steel door": self.examine_steel_door,
                "take the scalpel": self.take_scalpel,
                "turn away": self.turn_away_sink,
                "move away": self.move_away,
                "enter the code": self.enter_code,
                "enter the room": self.go_library,
                "hide behind the rack": self.hide_behind_rack,
                "go back to the kitchen": self.go_back_kitchen,
                "go back to the steel door": self.go_back_steel_door,
                "move to the remnants": self.go_old_remnants,
                "take the axe": self.take_axe,
                "move to the desk": self.go_desk,
                "push the desk": self.push_desk,
                "move to the mirror": self.go_mirror,
                "turn the mirror": self.turn_mirror
            }

    ### method to add Location instances to the dictionary
    def add_location(self, key, location) -> None:
        self.locations[key] = location

    ### method to change current location - loop until correct input
    def change_location(self, key) -> None:
        while True:
            if key in self.locations:
                self.current_location = self.locations[key]
                break
    
    ### Method to add items to inventory
    def add_item(self, item) -> None:
        self.inventory.append(item)
    
    ### Method to add knowledge to knowledge list
    def add_knowledge(self, knowledge) -> None:
        self.knowledge.append(knowledge)

    
    ### Method to start the game with an intr
    def start_game(self) -> None:

        print("==================================================")
        print("--------------WELCOME TO THE GAME-----------------")
        print("==================================================")
        print("You open your eyes slowly. Your head is throbbing.")
        print("The room is dimly lit, not anything like your memory.")
        print("That is lost in a black hole of oblivion.")
        print("You get up slowly from the floor. The wood creaks beneath your feet.")
        print("You need to find your way out of here.")
        separators()
        self.change_location("start")
        self.main_loop()
    
    ### Exploring at the beginning of the game
    def explore(self) -> None:
        print("-----------------------")
        print("You decided to explore!")
        print("-----------------------")
        self.change_location("dark room")
        print(f"{self.current_location.description}")
        separators()
    
    ### Quiting the game
    def quit(self) -> bool:
        self.game_over = True
        return self.game_over
    
    ### Opening the inventory
    def open_inventory(self) -> None:
        if self.inventory:
            self.change_location("inventory")
            print("-----------------------")
            print("Your invenory contains:")
            print("-----------------------")
            for item in self.inventory:
                print(f"{item.name}")
            separators()
            self.update_invetory_choices()
        else:
            print("-----------------------")
            print("The inventory is empty.")
            print("-----------------------")
    
    ### Method to update inventory choices to craft new items
    def update_invetory_choices(self):
        if pliers in self.inventory and clip in self.inventory:
                print(f"You can craft {picklock.name}!!!")
                self.inventory_choices["2"] = "craft a picklock"
                separators()

    
    ### Method to show available inventory choices
    def get_inventory_choices(self):
        inventory_choices = ""
        for value in self.inventory_choices.values():
            inventory_choices += f"{value}, "
        return inventory_choices.rstrip(", ")
    
    #### trying to open the locked door
    def open_the_locked_door(self) -> None:
        print("----------------------------")
        print("You decided to open the door!")
        print("----------------------------")
        print("You press the knob but nothing happens.\nThe door is locked! ")
        self.change_location("door")
        separators()
    
    ### unlocking the door with the key
    def open_door_with_picklock(self) -> None:
        print("----------------------------------------")
        print("You unlocked the door with the picklock!")
        print("----------------------------------------")
        self.change_location("unlocked door")

    ### opening the wardrobe
    def open_the_wardrobe(self) -> None:
        print("---------------------------------")
        print("You decided to open the wardrobe!")
        print("---------------------------------")
        if pliers not in self.inventory:
            self.change_location("wardrobe")
            print(f"{self.current_location.description}")
            separators()
        else:
            self.change_location("wardrobe without pliers")
            print(f"{self.current_location.description}")
            separators()
    
    ### examining the doll in the wardrobe
    def examine_doll(self) -> None:
        print("--------------------------")
        print("You're examining the doll.")
        print("--------------------------")
        print("The doll's empty eyes make you shudder.\nYou carefully take it it in your hands. A memory pops out.\nA dark memory screaming at you from within.\nA flash of a vision – you're in your room. She came for a visit.\nShe stinks from alcohol and for some reason you are scared.\nShe grins at you, her teeth rotten and disgusting...\nYou put the doll back in the wardrobe.")
        separators()

    ### going to the window
    def going_to_window(self) -> None:
        print("--------------------------------")
        print("You approach the window!")
        print("--------------------------------")
        if clip not in self.inventory:
            self.change_location("window")
            print(f"{self.current_location.description}")
            separators()
        else:
            self.change_location("window without clip")
            print(f"{self.current_location.description}")
            separators()

    ### closing the wardrobe
    def close_wardrobe(self) -> None:
        print("------------------------")
        print("You closed the wardrobe.")
        print("------------------------")
        self.change_location("dark room")

    ### taking the pliers
    def take_pliers(self) -> None:
        print("-----------------")
        print("You took the pliers!")
        print("-----------------")
        self.add_item(pliers)
        self.choices["open the door"].pop("not have")
        self.change_location("wardrobe without pliers")
    
    ###Taking the clip
    def take_clip(self):
        print("-----------------")
        print("You took the clip!")
        print("-----------------")
        self.add_item(clip)
        self.change_location("window without clip")
    
    ### going to the kitchen
    def go_kitchen(self) -> None:
        print("---------------------")
        print("You entered the room!")
        print("---------------------")
        self.change_location("kitchen")
        print(f"{self.current_location.description}")
        separators()
    
    ### Taking the scalpel
    def take_scalpel(self) -> None:
        print("---------------------")
        print("You took the scalpel!")
        print("---------------------")
        self.add_item("scalpel")
        self.change_location("sink without scalpel")
        print(f"{self.current_location.description}")
        separators()

    ##Examining the sink
    def examine_sink(self) -> None:
        print("--------------------------------")
        print("You decided to examine the sink!")
        print("--------------------------------")
        if "scalpel" not in self.inventory:    
            self.change_location("sink")
            print(f"{self.current_location.description}")
            separators()
        else:
            self.change_location("sink without scalpel")
            print(f"{self.current_location.description}")
            separators()

    ### Turning away from the sink
    def turn_away_sink(self) -> None:
        print("------------------------------")
        print("You turned away from the sink.")
        print("------------------------------")
        self.change_location("kitchen")
        print(f"{self.current_location.description_next}")
        separators()


    ### Examining the green door
    def examine_green_door(self) -> None:
        print("----------------------------")
        print("You approach the green door.")
        print("----------------------------")
        self.change_location("keyhole")
        print(f"{self.current_location.description}")
        separators()
    
    ### getting back to the dark room
    def go_back_room(self) -> None:
        print("-----------------------------")
        print("You go back to the dark room.")
        print("-----------------------------")
        self.change_location("dark room")
        print(f"{self.current_location.description_next}")
        separators()
    
    ### Moving away from the doors in the kitchen
    def move_away(self) -> None:
        print("-----------------------------")
        print("You turn back to the kitchen.")
        print("-----------------------------")
        self.change_location("kitchen")
        print(f"{self.current_location.description_next}")
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
                        for option_key, (option_text, _) in dialogue["options"].items():
                            print(f"{option_key}. {option_text}")
                        choice = input("Choose an option: ")
                    if choice in dialogue["options"]:
                        next_dialogue_key = dialogue["options"].get(choice)[1]
                        play_dialogue(next_dialogue_key)
                    else:
                        raise ValueError("Invalid choice")

                except ValueError as e:
                    print("--------------")
                    print(f"{e}")
                    print("--------------")
                
        if "knowledge_keypad" not in self.knowledge:
            play_dialogue("start")
        else:
            play_dialogue("code_answer")

    ### Examining the steel door
    def examine_steel_door(self):
        print("-----------------------------")
        print("You approach the steel door.")
        print("-----------------------------")
        self.change_location("steel_door")
        self.add_knowledge("knowledge_keypad")
        print(f"{self.current_location.description}")
        separators()

    ### Entering the code
    def enter_code(self):
        print("---------------------------------------")
        print("The screen is blank, the keys worn out.")
        print("---------------------------------------")
        code = input("Enter the code: ")
        clear()
        if code == "111":
            print("-----------------------------")
            print("The keypad light turns green!")
            print("-----------------------------")
            self.change_location("steel_door_opened")
            print(f"{self.current_location.description}")
            separators()
        else:
            print("Invalid code")
            separators()
    
    ### Going to the library 
    def go_library(self):
        print("--------------------------------------")
        print("The vast room reveals in front of you.")
        print("--------------------------------------")
        self.change_location("library")
        print(f"{self.current_location.description}")
        separators()

    ### Hiding behin the first rack
    def hide_behind_rack(self):
        print("-------------------------------------")
        print("You slip behind the rack on the left.")
        print("-------------------------------------")
        self.change_location("rack_one")
        print(f"{self.current_location.description}")
        separators()

    ### Moving back to the steel door
    def go_back_steel_door(self):
        print("---------------------------")
        print("You are at the entrance again.")
        print("---------------------------")
        self.change_location("library")
        print(f"{self.current_location.description_next}")
        separators()
    
    ### Going back to the kitchen from the library
    def go_back_kitchen(self) -> None:
        print("-------------------------------------")
        print("You slip back through the steel door.")
        print("-------------------------------------")
        self.change_location("kitchen")
        print(f"{self.current_location.description}")
        separators()

    ### Moving to the stuck axe
    def go_old_remnants(self) -> None:
        if crone.get_position() != "approaching_mirror":    
            if "axe" not in self.inventory:
                print("---------------------------------")
                print("You sneak up to the old remnants.")
                print("---------------------------------")
                self.change_location("old_remnants")
                print(f"{self.current_location.description}")
                separators()
            else:
                print("---------------------------------")
                print("You sneak up to the old remnants.")
                print("---------------------------------")
                self.change_location("old_remnants_without_axe")
                print(f"{self.current_location.description}")
                separators()
        else:
            print("The crone would see you. You can't go there!")
            separators()

    ### Taking the axe
    def take_axe(self) -> None:
        if crone.get_position() == "center_library":
            print("-----------------------------------")
            print("Removing the axe will make a noise.\nYou don't dare trying when the crone is so close.\nPerhaps you could lure her away?")
            print("-----------------------------------")
        else:
            print("-----------------------------------")
            print("Your muscles tense up as you pull.\nFinally, as the wood creaks, you successfully remove the axe.")
            print("-----------------------------------")
            self.inventory.append("axe")
            self.change_location("old_remnants_without_axe")
        
    def go_desk(self):
        if "desk_pushed" not in self.knowledge:
            print("-----------------------------")
            print("You approach the bloody desk.")
            print("-----------------------------")
            self.change_location("desk_with_body")
            print(f"{self.current_location.description}")
            separators()
        else:
            print("-----------------------------")
            print("The desk has been pushed away.")
            print("-----------------------------")
            self.change_location("pushed_desk")
            print(f"{self.current_location.description_next}")
            if crone.get_position() == "at_the_desk":
                print("The crone is examining the desk and body, hissing and twitching with rage.")
            separators()

    def push_desk(self):
        print("------------------------------------")
        print("The desk moves usrpisingly smoothly.")
        print("------------------------------------")
        print("The wheels squeek and soon the desk hits the rack on the opposite wall.\nFrom the center of the library, there comes a terrible hiss.\nThen heavy steps, and the sound of cloth sweeping on the floor.\nThe crone is on the move! She's gone to inspect the fuss at the opposite side.\n")
        self.change_location("pushed_desk")
        self.knowledge.append("desk_pushed")
        crone.set_position("at_the_desk")
        separators()

    ### Moving to the mirror
    def go_mirror(self):
        print("------------------------")
        print("You approach the mirror.")
        print("------------------------")
        self.change_location("mirror")
        print(f"{self.current_location.description}")
        separators()

    ### Turning the mirror
    def turn_mirror(self):
        print("--------------------")
        print("You turn the mirror.")
        print("--------------------")
        if crone.get_position() != "approaching_mirror":
            if crone.get_position() == "center_library":
                print("As the cracked glass catches the dim sunlight coming from the roof window\nreflection gets thrown at the center of the library.")
                print("The light falls right on the crone. There is a furious roar, inhuman and ears-piercing.\nYou manage to slip behind the rack next to the mirror right in time.\nThe steps are approaching, the hissing grows.")
                separators()
                crone.set_position("approaching_mirror")
            else:
                print("As the cracked glass catches the dim sunlight coming from the roof window\nreflection gets thrown at the center of the library.")
                print("Nothing happens. Well, you don't even know what you expected.")
                separators()
        else:
            print("The mirror is already turned and the crone is coming to you!")
            separators()

    ### Method to get a user input
    def get_input(self, clear):
        user_input = input(f"What do you want to do? ({self.current_location.choices}) > ").lower()
        clear()
        return user_input


########### MAIN LOOP OF THE GAME # #########
    def main_loop(self) -> None:        
        user_input = self.get_input(clear)
        while not self.game_over:
            try:
                if isinstance(self.choices[user_input], dict):
                    try: 
                        self.choices[user_input]["not have"]()
                        user_input = self.get_input(clear)
                    except: ##Here we'll need to switch the
                            ##booleans after picking up
                            ##the items:
                        self.choices[user_input]["have"]()
                        user_input = self.get_input(clear)
                else:
                    self.choices[user_input]()
                    user_input = self.get_input(clear)
            except:
                print("---------------")
                print("Invalid choice.")
                print("---------------")
                user_input = self.get_input(clear)