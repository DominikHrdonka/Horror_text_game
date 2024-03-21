from location import Location
class Game:
    def __init__(self):
        self.game_over = False
        self.current_location = None
        self.locations = {}
        self.inventory = []

    ### method to add Location instances to the dictionary
    def add_location(self, key, location):
        self.locations[key] = location

    ### method to change current location
    def change_location(self, key):
        while True:
            if key in self.locations:
                self.current_location = self.locations[key]
                break
                ### make a loop to repeat when wrong output
    
    ### Method to add items to inventory
    def add_item(self, item):
        self.inventory.append(item)
            
    def start_game(self):
        print("==================================================")
        print("You open your eyes slowly. Your head is throbbing.")
        print("The room is dimly lit, not anything like your memory.")
        print("That is lost in a black hole of oblivion.")
        print("You get up slowly from the floor. The wood creaks beneath your feet.")
        print("You need to find your way out of here.")
        print("--------------------------")
        user_input = input(f"What do you want to do? (explore, quit) > ")
        self.main_loop(user_input)
    
    def explore(self):
        print("-----------------------")
        print("You decided to explore!")
        print("-----------------------")
        print(f"{self.current_location.description}")
        print("--------------------------")
    
    #### trying to open the lockeddoor
    def open_the_locked_door(self):
        print("----------------------------")
        print("You decided to open the door!")
        print("----------------------------")
        print("You press the knob but nothing happens.\nThe door is locked! ")
        self.change_location("door")
        print("--------------------------")
    
    def open_door_with_key(self):
        print("-----------------------------------")
        print("You unlocked the door with the key!")
        print("-----------------------------------")
        self.change_location("unlocked door")
        print("--------------------------")

    ### opening the wardrobe
    def open_the_wardrobe(self):
        print("---------------------------------")
        print("You decided to open the wardrobe!")
        print("---------------------------------")
        self.change_location("wardrobe")
        print(f"{self.current_location.description}")
        print("--------------------------")
    
    def examine_doll(self):
        print("--------------------------")
        print("You're examining the doll.")
        print("--------------------------")
        print("The doll's empty eyes make you shudder.\nYou carefully take it it in your hands. A memory pops out.\nA dark memory screaming at you from within.\nA flash of a vision – you're in your room. She came for a visit.\nShe stinks from alcohol and for some reason you are scared.\nShe grins at you, her teeth rotten and disgusting...\nYou put the doll back in the wardrobe.")
        print("--------------------------")
    ### going to the window
    def going_to_window(self):
        print("--------------------------------")
        print("You decided to go to the window!")
        print("--------------------------------")
        self.change_location("window")
        print(f"{self.current_location.description}")
        print("--------------------------")

    ### closing the wardrobe
    def close_wardrobe(self):
        print("------------------------")
        print("You decided to close the wardrobe.")
        print("------------------------")
        self.change_location("dark room")
        print(f"{self.current_location.description_next}")
        print("--------------------------")

    ### taking the key
    def take_key(self):
        print("-----------------")
        print("You took the key!")
        print("-----------------")
        self.add_item("key")
        self.change_location("wardrobe without key")
        print("--------------------------")
    
    ### going to the kitchen
    def go_kitchen(self):
        print("---------------------")
        print("You entered the room!")
        print("---------------------")
        self.change_location("kitchen")
        print(f"{self.current_location.description}")
        print("--------------------------")
    
    def take_scalpel(self):
        print("---------------------")
        print("You took the scalpel!")
        print("---------------------")
        self.add_item("scalpel")
        self.change_location("kitchen without scalpel")
        print(f"{self.current_location.description}")
        print("--------------------------")

    def examine_sink(self):
        print("--------------------------------")
        print("You decided to examine the sink!")
        print("--------------------------------")
        self.change_location("sink")
        print(f"{self.current_location.description}")
        print("--------------------------")

    def examine_green_door(self):
        print("----------------------------")
        print("You approach the green door.")
        print("----------------------------")
        self.change_location("sink")
        print(f"{self.current_location.description}")
        print("--------------------------")

    def talk_to_creature(self):
        

    ### MAIN LOOP OF THE GAME
    def main_loop(self, user_input):
        while not self.game_over:
            if user_input == "explore":
                self.explore()

            elif user_input == "open the door":
                if "key" in self.inventory:
                    self.open_door_with_key()
                else:
                    self.open_the_locked_door()
                user_input == None

            elif user_input == "go to the next room":
                user_input == None
                self.go_kitchen()
                
            elif user_input == "open the wardrobe":
                user_input = None
                self.open_the_wardrobe()
            
            elif user_input == "go to the window":
                user_input == None
                self.going_to_window()

            elif user_input == "take the key":
                user_input == None
                self.take_key()

            elif user_input == "close the wardrobe":
                user_input == None
                self.close_wardrobe()
            
            elif user_input == "examine the doll":
                user_input == None
                self.examine_doll()
            
            elif user_input == "examine the sink":
                user_input == None
                self.examine_sink()

            elif user_input == "take the scalpel":
                user_input == None
                self.take_scalpel()
            
            elif user_input == "examine the green door":
                user_input == None
                self.examine_green_door()

            elif user_input == "quit":
                self.game_over = True
            user_input = input(f"What do you want to do? ({self.current_location.choices}) > ")
            

        

