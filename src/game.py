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
            "Move to the remnants": library_rack.go_remnants,
            "Take the axe": old_remnants.take_axe,
            "Move to the mirror": old_remnants.go_mirror,
            "Turn the mirror": mirror.turn_mirror,
            "Enter the passageway": mirror.go_passageway,
            "Climb through the hole": passageway.climb_through_hole
            
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
                print("--------------")
                print("Invalid choice")
                print("--------------")

# Creating instance of Game
game = Game()