from location import *

from dialogues import creature
from crone import *
from inventory import *



class Game:
    def __init__(self) -> None:
        self.__game_over = False
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
            "Go back to the library entrance": library_rack.go_library_entrance,
            "Go back to the kitchen": enter_library.go_back_kitchen,
            "Move to the desk": library_rack.go_desk,
            "Push the desk": desk_with_body.push_desk,
            "Move to the remnants": library_rack.go_remnants,
            "Take the axe": old_remnants.take_axe,
            "Move to the mirror": old_remnants.go_mirror,
            "Turn the mirror": mirror.turn_mirror,
            "Enter the passageway": mirror.go_passageway,
            "Climb through the hole": passageway.climb_through_hole,
            "Examine the fuse box": service_room.examine_fuse_box,
            "Open the lid": fuse_box_closed.open_fuse_box,
            "Look away": fuse_box_closed.look_away,
            "Switch the button": fuse_box_open.switch_button,
            "Connect the cable": fuse_box_open.connect_cable,
            "Cut off the old cable rubber": inventory.cut_off_rubber,
            "Use the computer": service_room.use_computer,
            "Examine the garbage": service_room.examine_garbage,
            "Enter the library": service_room.enter_library,
            "Enter the service room": library_back.enter_service_room,
            "Open the two-wing door": library_back.open_two_wing_door,

        }
    
    ### Method to start the game with an intr
    def start_game(self) -> None:

        print("==================================================")
        print("--------------WELCOME TO THE GAME-----------------")
        print("==================================================")
        print("""
You open your eyes slowly. Your head is throbbing.
The room is dimly lit, not anything like your memory.
The room is dimly lit, not anything like your memory.
That is lost in a black hole of oblivion.
You get up slowly from the floor. The wood creaks beneath your feet.
You need to find your way out of here.
""")
        separators()
        Location.change_location(start)
        self.main_loop()
    

    ### Method to get a user input
    def get_input(self, clear):
        list_choices = ""
        for key, value in (Location.get_current_location_choices().items()):
            list_choices += (f"{key} {value}, ")
        user_input = input(f"What do you want to do? ({list_choices.rstrip(", ")}) > ").lower()
        clear()
        return user_input
        

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