from location import Location
class Game:
    def __init__(self):
        self.game_over = False
        self.current_location = None
            
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
        
    ### opening the wardrobe
    def open_the_wardrobe(self):
        print("You decided to open the wardrobe!")
        print("---------------------------------")
        print("The wardrobe creaks. Awful smell gets out.\nYou feel sick and have to cover your nose.\nAs the shock passes, you notice something inside.\nA ragged doll with one eye. And there... a key!")
        

        
    def main_loop(self, user_input):
        while not self.game_over:
            if user_input == "explore":
                user_input = None
                self.explore()

            elif user_input == "open the door":
                user_input = None
                self.open_the_door()
                
            elif user_input == "open the wardrobe":
                user_input = None
                self.open_the_wardrobe()
                ### change locatio to get new choices

            elif user_input == "quit":
                self.game_over = True
            user_input = input(f"What do you want to do? ({self.current_location.choices}) > ")

