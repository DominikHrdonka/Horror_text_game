from location import *

from dialogues import creature
from crone import *
from inventory import *



class Game:
    def __init__(self) -> None:
        self.__game_over = False
    
        self.__inventory = []
        self.__knowledge = []

        self.inventory_choices = {
            "1": "exit"
        }

        self.actions={
            "Explore": start.explore,
            "Go to the window": dark_room.go_window,
            "Open the door": dark_room.open_dark_room_door,
            "Open the wardrobe": dark_room.open_wardrobe,
            "Take the clip": dark_room_window.take_clip
        }

    
    
    ### Method to add knowledge to knowledge list
    def add_knowledge(self, knowledge) -> None:
        self.__knowledge.append(knowledge)



    
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
        Location.change_location(start)
        self.main_loop()
    

    
    ### Opening the inventory
    def open_inventory(self) -> None:
        if self.__inventory:
            self.change_location("inventory")
            self.label("Your inventory contains:")
            for item in self.__inventory:
                print(f"{item.name}")
            separators()
            self.update_invetory_choices()
        else:
            self.label("The inventory is empty.")
            
    ### Method to update inventory choices to craft new items
    def update_invetory_choices(self):
        if pliers in self.__inventory and clip in self.__inventory:
                print(f"You can craft {picklock.name}!!!")
                self.inventory_choices["2"] = "craft a picklock"
                separators()
            
    ### Method to show available inventory choices
    def get_inventory_choices(self):
        self.update_invetory_choices()
        inventory_choices = ""
        for value in self.inventory_choices.values():
            inventory_choices += f"{value}, "
        return inventory_choices.rstrip(", ")
    


    
    ### going to the kitchen
    def go_kitchen(self) -> None:
        self.label("You enter the room!")
        self.change_location("kitchen")
        print(f"{self.get_current_location()}")
        separators()
        pass
    
    ### Taking the scalpel
    def take_scalpel(self) -> None:
        self.label("You took the scalpel!")
        self.add_item("scalpel")
        self.change_location("sink without scalpel")
        print(f"{self.get_current_location()}")
        separators()
        pass

    ##Examining the sink
    def examine_sink(self) -> None:
        self.label("You approach the sink.")
        if "scalpel" not in self.__inventory:    
            self.change_location("sink")
            print(f"{self.get_current_location()}")
            separators()
        else:
            self.change_location("sink without scalpel")
            print(f"{self.get_current_location()}")
            separators()
        pass

    ### Turning away from the sink
    def turn_away_sink(self) -> None:
        self.label("You turn away from the sink.")
        self.change_location("kitchen")
        print(f"{self.get_current_location_revisit()}")
        separators()
        pass


    ### Examining the green door
    def examine_green_door(self) -> None:
        self.label("You approach the green door.")
        self.change_location("keyhole")
        print(f"{self.get_current_location()}")
        separators()
        pass
    
    ### getting back to the dark room
    def go_back_room(self) -> None:
        self.label("You go back to the dark room.")
        self.change_location("dark room")
        print(f"{self.get_current_location_revisit()}")
        separators()
        pass
    
    ### Moving away from the doors in the kitchen
    def move_away(self) -> None:
        self.label("You turn back to the kitchen.")
        self.change_location("kitchen")
        print(f"{self.get_current_location_revisit()}")
        separators()
        pass

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
        if "revisiting creature" not in self.__knowledge:
            self.add_knowledge("revisiting creature")
            play_dialogue("start")
        else:
            if "knowledge_keypad" not in self.__knowledge:
                print(">>Leave me alone!<<")
                separators()
            else:
                play_dialogue("code_answer")
        pass
            

    ### Examining the steel door
    def examine_steel_door(self):
        self.label("You approach the steel door.")
        self.change_location("steel_door")
        self.add_knowledge("knowledge_keypad")
        print(f"{self.get_current_location()}")
        separators()
        pass

    ### Entering the code
    def enter_code(self):
        self.label("The screen is blank, the keys worn out.")
        code = input("Enter the code: ")
        clear()
        if code == "571":
            self.label("The keypad light turns green!")
            self.change_location("steel_door_opened")
            print(f"{self.get_current_location()}")
            separators()
        else:
            print("Invalid code")
            separators()
        pass
    
    ### Going to the library 
    def go_library(self):
        self.label("The vast room reveals in front of you.")
        self.change_location("library")
        print(f"{self.get_current_location()}")
        separators()
        pass

    ### Hiding behin the first rack
    def hide_behind_rack(self):
        self.label("You slip behind the rack on the left.")
        self.change_location("rack_one")
        print(f"{self.get_current_location()}")
        separators()
        pass

    ### Moving back to the steel door
    def go_back_steel_door(self):
        self.label("You are at the entrance again.")
        self.change_location("library")
        print(f"{self.get_current_location_revisit()}")
        separators()
        pass
    
    ### Going back to the kitchen from the library
    def go_back_kitchen(self) -> None:
        self.label("You slip back through the steel door.")
        self.change_location("kitchen")
        print(f"{self.get_current_location()}")
        separators()
        pass

    ### Moving to the stuck axe
    def go_old_remnants(self) -> None:
        if crone.get_position() != "approaching_mirror":    
            if "axe" not in self.__inventory:
                self.label("You sneak up to the old remnants.")
                self.change_location("old_remnants")
                print(f"{self.get_current_location()}")
                separators()
            else:
                self.label("You sneak up to the old remnants.")
                self.change_location("old_remnants_without_axe")
                print(f"{self.get_current_location()}")
                separators()
        else:
            self.label("The crone would see you. You can't go there!")
        pass

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
            self.add_item(axe)
            self.change_location("old_remnants_without_axe")
        pass
        
    def go_desk(self):
        if "desk_pushed" not in self.__knowledge:
            self.label("You approach the bloody desk.")
            self.change_location("desk_with_body")
            print(f"{self.get_current_location()}")
            separators()
        else:
            self.label("The desk has been pushed away.")
            self.change_location("pushed_desk")
            print(f"{self.get_current_location_revisit()}")
            if crone.get_position() == "at_the_desk":
                print("The crone is examining the desk and body, hissing and twitching with rage.")
            separators()
        pass

    def push_desk(self):
        self.label("The desk moves usrpisingly smoothly.")
        print("The wheels squeek and soon the desk hits the rack on the opposite wall.\nFrom the center of the library, there comes a terrible hiss.\nThen heavy steps, and the sound of cloth sweeping on the floor.\nThe crone is on the move! She's gone to inspect the fuss at the opposite side.\n")
        self.change_location("pushed_desk")
        self.add_knowledge("desk_pushed")
        crone.set_position("at_the_desk")
        separators()
        pass

    ### Moving to the mirror
    def go_mirror(self):
        self.label("You approach the mirror.")
        self.change_location("mirror")
        print(f"{self.get_current_location()}")
        separators()
        pass

    ### Turning the mirror
    def turn_mirror(self):
        self.label("You turn the mirror.")
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
        pass

    ### Going to the passageway
    def go_passageway(self)-> None:
        self.label("You enter the passageway.")
        self.change_location("passageway")
        if "revisiting_passgw" not in self.__knowledge:
            print(f"{self.get_current_location()}")
            self.add_knowledge("revisiting_passgw")
            separators()
        else:
            print(f"{self.get_current_location_revisit()}")
            separators()
        pass

    ### Entering the service room
    def climb_through_hole(self)-> None:
        self.label("You climb through the hole.")
        self.change_location("service_room")
        if "revisitting_servicer" not in self.__knowledge:
            print(f"{self.get_current_location()}")
            separators()
            self.add_knowledge("revisitting_servicer")
        else:
            print(f"{self.get_current_location_revisit()}")
            separators()
        pass

    ### Using the computer
    def use_computer(self)-> None:
        print("---------------------------")
        print("You press the power button.\nNothing happens. the machine is long dead.")
        print("---------------------------")
        pass

    ### Method to get a user input
    def get_input(self, clear):
        list_choices = ""
        for key, value in (Location.get_current_location_choices().items()):
            list_choices += (f"{key} {value}, ")
        user_input = input(f"What do you want to do? ({list_choices.rstrip(", ")}) > ").lower()
        clear()
        return user_input
    

    ### Examining the garbage
    def examine_garbage(self)-> None:
        print("-------------------------")
        print("You approach the garbage.\nOld carton boxes, some wires, papershreds... Oh, look, a rusty knife!")
        print("-------------------------")
        print("You took the rusty knife!")
        separators()
        self.add_item("rusty_knife")
        pass

    ###Examining the fuse box
    def examine_fuse_box(self)-> None:
        self.label("You approach the fuse box.")
        self.change_location("fuse_box")
        if "revisiting_fuse" not in self.__knowledge:
            print(f"{self.get_current_location()}")
            separators()
            self.add_knowledge("revisiting_fuse")
        else:
            print(f"{self.get_current_location_revisit()}")
            separators()
        pass
    
    ###Looking away from the fuse box
    def look_away(self)-> None:
        self.label("You look away.")
        self.change_location("service_room")
        print(f"{self.get_current_location_revisit()}")
        separators()
        pass

    ###Switching the button on the fuse box
    def switch_button(self)-> None:
        self.label("You switch the button.")
        print("There is a spark.\nFrom below the door you see light entering the service room.\nAnd with the light, there comes a shriek. The crone's coming here!")
        crone.set_position("approaching_service_room")
        separators()
        pass
    
    def enter_library(self):
        if crone.get_position() == "approaching_service_room":
            self.label("You can't go there now, you'd bump right into the crone!")
        else:
            self.label("You enter the library")
            self.change_location("library_back")
            print(self.get_current_location())
            separators()
        pass

    ### Entering service room from library
    def enter_service_room(self):
        self.label("You enter the service room")
        self.change_location("service_room")
        print(self.get_current_location_revisit())
        separators()
        pass
        

########### MAIN LOOP OF THE GAME # #########
    def main_loop(self) -> None:
        while not self.__game_over:
            user_input = self.get_input(clear)
            
            try:
                self.actions[Location.get_current_location_choices()[user_input]]()
            except:
                print("Invalid choice.")

# Creating instance of Game
game = Game()