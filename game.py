import time
from location import Location
import os

 ### Global method to create separators between descr. and inputs ###
def separators():
    print("-" * 25)

class Game:
    def __init__(self):
        self.game_over = False
        self.current_location = None
        self.locations = {}
        self.inventory = []
          
   

    ### method to add Location instances to the dictionary
    def add_location(self, key, location):
        self.locations[key] = location

    ### method to change current location - loop until correct input
    def change_location(self, key):
        while True:
            if key in self.locations:
                self.current_location = self.locations[key]
                break
    
    ### Method to add items to inventory
    def add_item(self, item):
        self.inventory.append(item)

    
    ### Method to start the game with an intr
    def start_game(self):

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
    def explore(self):
        print("-----------------------")
        print("You decided to explore!")
        print("-----------------------")
        self.change_location("dark room")
        print(f"{self.current_location.description}")
        separators()
    
    ### Quiting the game
    def quit(self):
        self.game_over = True
        return self.game_over
    
    #### trying to open the locked door
    def open_the_locked_door(self):
        print("----------------------------")
        print("You decided to open the door!")
        print("----------------------------")
        print("You press the knob but nothing happens.\nThe door is locked! ")
        self.change_location("door")
        separators()
    
    ### unlocking the door with the key
    def open_door_with_key(self):
        print("-----------------------------------")
        print("You unlocked the door with the key!")
        print("-----------------------------------")
        self.change_location("unlocked door")

    ### opening the wardrobe
    def open_the_wardrobe(self):
        print("---------------------------------")
        print("You decided to open the wardrobe!")
        print("---------------------------------")
        if "key" not in self.inventory:
            self.change_location("wardrobe")
            print(f"{self.current_location.description}")
            separators()
        else:
            self.change_location("wardrobe without key")
            print(f"{self.current_location.description}")
            separators()
    
    ### examining the doll in the wardrobe
    def examine_doll(self):
        print("--------------------------")
        print("You're examining the doll.")
        print("--------------------------")
        print("The doll's empty eyes make you shudder.\nYou carefully take it it in your hands. A memory pops out.\nA dark memory screaming at you from within.\nA flash of a vision – you're in your room. She came for a visit.\nShe stinks from alcohol and for some reason you are scared.\nShe grins at you, her teeth rotten and disgusting...\nYou put the doll back in the wardrobe.")
        separators()

    ### going to the window
    def going_to_window(self):
        print("--------------------------------")
        print("You decided to go to the window!")
        print("--------------------------------")
        self.change_location("window")
        print(f"{self.current_location.description}")
        separators()

    ### closing the wardrobe
    def close_wardrobe(self):
        print("------------------------")
        print("You closed the wardrobe.")
        print("------------------------")
        self.change_location("dark room")

    ### taking the key
    def take_key(self):
        print("-----------------")
        print("You took the key!")
        print("-----------------")
        self.add_item("key")
        self.change_location("wardrobe without key")
    
    ### going to the kitchen
    def go_kitchen(self):
        print("---------------------")
        print("You entered the room!")
        print("---------------------")
        self.change_location("kitchen")
        print(f"{self.current_location.description}")
        separators()
    
    ### Taking the scalpel
    def take_scalpel(self):
        print("---------------------")
        print("You took the scalpel!")
        print("---------------------")
        self.add_item("scalpel")
        self.change_location("sink without scalpel")
        print(f"{self.current_location.description}")
        separators()

    ##Examining the sink
    def examine_sink(self):
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
    def turn_away_sink(self):
        print("------------------------------")
        print("You turned away from the sink.")
        print("------------------------------")
        self.change_location("kitchen")
        print(f"{self.current_location.description_next}")
        separators()


    ### Examining the green door
    def examine_green_door(self):
        print("----------------------------")
        print("You approach the green door.")
        print("----------------------------")
        self.change_location("keyhole")
        print(f"{self.current_location.description}")
        separators()
    
    ### getting back to the dark room
    def go_back_room(self):
        print("-----------------------------")
        print("You go back to the dark room.")
        print("-----------------------------")
        self.change_location("dark room")
        print(f"{self.current_location.description_next}")
        separators()
    
    ### Moving away from the green door
    def move_away(self):
        print("-----------------------------")
        print("You turn back to the kitchen.")
        print("-----------------------------")
        self.change_location("kitchen")
        print(f"{self.current_location.description_next}")
        separators()

 ########Talking to the creature: dialogue########
    dialogue = {
        "start": {
            "lines": ["You take a deep breath.",
                      ">> Hello? Can you hear me?<<",
                      "The rumbling continues...",
                      ">>Hey! Over here!<<",
                      ">>What do you want?<<"
            ],
            "options": {
                "1": (">>Who are you?<<", "answer_one"),
                "2": (">>Where are we?<<", "answer_two")
        }
        },
        "answer_one": {
            "lines": [
                ">>Urgh... WHO I am? More like WHAT I am.<<",
                ">>So much pain...<<",
                ">>So much horror...<<",
                ">>HELP ME!!!<<"
            ],
            "options": {
                "1": (">>Where are we?<<", "answer_two")
            }
        },
        "answer_two": {
            "lines": [
                ">>In hell...<<",
                ">>Is she... Is she still gone?<<"
            ],
            "options": {
                "1": (">>Who is SHE?<<", "answer_three"),
                "2": (">>There's just us. I guess...<<", "answer_four")
            }
        }
    }
    
    
    def talk_to_creature(self):
        
        ### implementing pause between speech lines
        def dialogue_pause():
            time.sleep(2)

        ### Child function of the dialogue - question branches
        def start_dialogue():
            separators()
            print("You take a deep breath.")
            separators()
            print(">> Hello? Can you hear me?<<")
            dialogue_pause()
            print("The rumbling continues...")
            dialogue_pause()
            print(">>Hey! Over here!<<")
            dialogue_pause()
            print(">>What do you want?<<")
            separators()

        ### Question 1 method: Who are you ###
        def question_one():
            dialogue_pause()
            print(">>Urgh... WHO I am? More like WHAT I am.<<")
            dialogue_pause()
            print(">>So much pain...<<")
            dialogue_pause()
            print(">>So much horror...<<")
            dialogue_pause()
            print(">>HELP ME!!!<<")
            separators()
            dialogue_input = input("2. Where are we?")
            if dialogue_input == "2":
                question_two()

        ### Question 2 method: Where are we ###
        def question_two():
            dialogue_pause()
            print(">>In hell...<<")
            dialogue_pause()
            print(">>Is she... Is she still gone?<<")
            separators()

        ### Question three method: Who is she?
        def question_three():
            dialogue_pause()
            print(">>Our Mother? What kind of question is that?\nShe is the one who feeds us.")
            dialogue_pause()
            print(">>Who carresses us.<<")
            dialogue_pause()
            print("Who punishes us...<<")
            dialogue_pause()
            print("*sobbing*")
            dialogue_pause()
            print(">>I don't want her to come back...<<")
            separators()
            dialogue_input = input("2. There's just us. I guess... ")
            if dialogue_input == "2":
                question_four()
        
        ### Question four method: There's only us...  
        def question_four():
            dialogue_pause()
            print(">>Good... that is very good. We must rest.<<")
            dialogue_pause()
            print(">>Before she comes back.<")
            separators()
        
        ### Question five method: How can we get out of here?
        def question_five():
            dialogue_pause()
            print(">>We can't. We're bound to this place.<<")
            dialogue_pause()
            print(">>Forever.<<")
            dialogue_pause()
            print(">>And now... let me rest. I must be strong when she comes back.<<")
            separators()
        
    #### The dialogue itself ###
        start_dialogue()
        dialogue_input = input("Choose number: 1. Who are you?/2. Where are we? ")
        if dialogue_input == "1":
            question_one()
        if dialogue_input == "2":
            question_two()
        dialogue_input = input("Choose number: 1. Who is SHE?/2. There's just us. I guess...<< ")
        if dialogue_input == "1":
            question_three()
        if dialogue_input == "2":
            question_four()
        dialogue_input = input(">>Choose number: 1. How can we get out of here? ")
        if dialogue_input == "1":
            question_five()


########### MAIN LOOP OF THE GAME ################
    def main_loop(self):
        ###Method to clear the terminal after every user input
        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')
        user_input = input(f"What do you want to do? ({self.current_location.choices}) > ").lower()
        clear()

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
            
            elif user_input == "go back to the room":
                user_input == None
                self.go_back_room()
            
            elif user_input == "examine the doll":
                user_input == None
                self.examine_doll()
            
            elif user_input == "examine the sink":
                user_input == None
                self.examine_sink()

            elif user_input == "take the scalpel":
                user_input == None
                self.take_scalpel()
            
            elif user_input == "turn away":
                user_input == None
                self.turn_away_sink()
            
            elif user_input == "examine the green door":
                user_input == None
                self.examine_green_door()
                
            elif user_input == "move away":
                user_input == None
                self.move_away()

            elif user_input == "talk to the creature":
                user_input == None
                self.talk_to_creature()

            elif user_input == "quit":
                user_input == None
                self.quit()
                break

            user_input = input(f"What do you want to do? ({self.current_location.choices}) > ").lower()
            clear()
            

        

