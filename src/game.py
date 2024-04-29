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
            "Open inventory": inventory.open_inventory,
            "Close inventory": inventory.close_inventory,
            "Explore": start.explore,
            "Go to the window": dark_room.go_window,
            "Open the door": dark_room.open_dark_room_door,
            "Open the wardrobe": dark_room.open_wardrobe,
            "Take the clip": dark_room_window.take_clip,
            "Take the pliers": wardrobe.take_pliers,
            "Craft a picklock": inventory.craft_picklock,
            "Examine the doll": wardrobe.examine_doll,
            "Close the wardrobe": wardrobe.close_wardrobe,
            "Go to the next room": dark_room.go_kitchen,
            "Examine the sink": kitchen.examine_sink,
            "Take the scalpel": kitchen.take_scalpel,
            "Turn away": kitchen.turn_away,
            "Go back to the room": kitchen.go_back_room,
            "Examine the steel door": kitchen.examine_steel_door,
            "Enter the code": kitchen.enter_code,
            "Examine the green door": kitchen.examine_green_door,
            "Talk to the creature": kitchen.talk_to_creature,
            "Enter the room": kitchen.go_library,
            "Hide behind the rack": enter_library.hide_behind_rack,
            "Go back to the kitchen": enter_library.go_back_kitchen,
            "Move to the desk": library_rack.go_desk,
            "Push the desk": desk_with_body.push_desk,
            "Move to the remnants": library_rack.go_remnants
            
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

    
    
    ### Moving away from the doors in the kitchen
    def move_away(self) -> None:
        self.label("You turn back to the kitchen.")
        self.change_location("kitchen")
        print(f"{self.get_current_location_revisit()}")
        separators()
        pass

            
    
    ### Going to the library 
    def go_library(self):
        self.label("The vast room reveals in front of you.")
        self.change_location("library")
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
    

    ### Examine the garbage
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