from game import *
from location import *
from items import *

def main() -> None:
    
    # Adding location to the game list of locations
    game.add_location("Start", Start)
    game.add_location("dark room", dark_room)
    game.add_location("wardrobe", wardrobe)
    game.add_location("window", window)
    game.add_location("door", door)
    game.add_location("unlocked door", unlocked_door)
    game.add_location("wardrobe without pliers", wardrobe_without_pliers)
    game.add_location("window without clip", window_without_clip)
    game.add_location("kitchen", kitchen)
    game.add_location("sink", sink)
    game.add_location("sink without scalpel", sink_without_scalpel)
    game.add_location("keyhole", keyhole)
    game.add_location("steel_door", steel_door)
    game.add_location("library", library)
    game.add_location("steel_door_opened", steel_door_opened)
    game.add_location("rack_one", rack_one)
    game.add_location("old_remnants", old_remnants)
    game.add_location("desk_with_body", desk_with_body)
    game.add_location("pushed_desk", pushed_desk)
    game.add_location("old_remnants_without_axe", old_remnants_without_axe)
    game.add_location("mirror", mirror)
    game.add_location("passageway", passageway)
    game.add_location("service_room", service_room)
    game.add_location("fuse_box", fuse_box)
    game.add_location("library_back", library_back)

    # Defining current location
    game.current_location = dark_room

    # Starting the game
    game.start_game()



if __name__ == "__main__":
    main()