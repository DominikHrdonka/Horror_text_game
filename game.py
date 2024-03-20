from location import Location
class Game:
    def __init__(self):
        self.game_over = False
        self.current_location = None
        self.locations = {}

    ### method to add Location instances to the dictionary
    def add_location(self, key, location):
        self.locations[key] = location

    ### method to change current location
    def change_location(self, key):
        while True:
            if key in self.locations:
                self.current_location = self.locations[key]
                break
            else:
                print("You can't go there")
                ### make a loop to repeat when wrong output
            
    def start_game(self):
        print("You open your eyes slowly. Your head is throbbing.")
        print("The room is dimly lit, not anything like your memory.")
        print("That is lost in a black hole of oblivion.")
        print("You get up slowly from the floor. The wood creaks beneath your feet.")
        print("You need to find your way out of here.")
        user_input = input(f"What do you want to do? (explore, quit) > ")
        self.main_loop(user_input)
    
    def explore(self):
        print("You decided to explore!")
        print("-----------------------")
        print(f"{self.current_location.description}")
    
    #### opening the door
    def open_the_door(self):
        print("You decided to open the door!")
        print("----------------------------")
        print("You press the knob but nothing happens.\nThe door is locked! ")
        self.change_location("door")

    ### opening the wardrobe
    def open_the_wardrobe(self):
        print("You decided to open the wardrobe!")
        print("---------------------------------")
        self.change_location("wardrobe")
        print(f"{self.current_location.description}")
    
    ### going to the window
    def going_to_window(self):
        print("You decided to go to the window!")
        print("--------------------------------")
        self.change_location("window")
        print(f"{self.current_location.description}")

    ### closing the wardrobe
    def close_wardrobe(self):
        print("You decided to close the wardrobe.")
        print("------------------------")
        self.change_location("dark room")
        print(f"{self.current_location.description}")


        

    def main_loop(self, user_input):
        while not self.game_over:
            if user_input == "explore":
                self.explore()

            elif user_input == "open the door":
                user_input = None
                self.open_the_door()
                
            elif user_input == "open the wardrobe":
                user_input = None
                self.open_the_wardrobe()
            
            elif user_input == "go to the window":
                user_input == None
                self.going_to_window()

            elif user_input == "close the wardrobe":
                user_input == None
                self.close_wardrobe()


            elif user_input == "quit":
                self.game_over = True
            user_input = input(f"What do you want to do? ({self.current_location.choices}) > ")
            

        

