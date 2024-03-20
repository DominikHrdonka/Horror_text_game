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
        self.main_loop()
    
    def explore(self):
        print("You decided to explore!")
        print(f"{self.current_location.description}") 
        
    def main_loop(self):
        while not self.game_over:
            user_input = input("What do you want to do? (explore, quit) > ")
            if user_input == "explore":
                self.explore()
            if user_input == "quit":
                self.game_over = True

