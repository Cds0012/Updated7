# TextBasedGame.Py
# Cassandra Smith


def show_instructions():
    """Displays the game instruction."""
    print("Escape From Crystal Caverns")
    print("Collect 6 items to win the game, or die in collasping caverns")
    print("Move commands: go South, go North, go East, go West")
    print("Add to inventory: get 'item name'")
    print("To quit the game, type 'quit'")


def show_status(current_room, inventory):
    """Displays the player's current status."""
    print(f"You are in the (current_room)")
    print("inventory", inventory)
    if "item" in rooms[current_room] and rooms[current_room]["item"]:
        print("You see a {rooms[current_room]['item']}")


def get_new_state(direction, current_room):
    """Updates the player's state based on the direction input"""
    if direction in rooms[current_room]:
        return rooms[current_room][direction]  # Move to the new room
    else:
        return current_room  # Stay in the current room


def main():
    """Main game loop."""
    global rooms  # Needed to modify the rooms dictionary within the function

    rooms = {
        "Entrance": {
            "North": "Crystal Lake",
            "East": "Shifting Sands",
            "item": None
        },
        "Crystal Lake": {
            "South": "Whispering Walls",
            "North": "Entrance",
            "item": "Climbing Gear"
        },
        "Whispering Walls": {
            "North": "Crystal Lake",
            "East": "Obsidian Maze",
            "item": "Gemstone Compass"
        },
        "Shifting Sands": {
            "South": "Obsidian Maze",
            "West": "Entrance",
            "item": "Collapsing Caverns"
        },
        "Obsidian Maze": {
            "North": "Shifting Sands",
            "East": "Giant Geode",
            "West": "Whispering Walls",
            "item": "Crystal Key"
        },
        "Giant Geode": {
            "South": "Emerald Grotto",
            "West": "Obsidian Maze",
            "item": "Lantern"
        },
        "Emerald Grotto": {
            "North": "Giant Geode",
            "South": "Exit",
            "item": "Ancient Tablet"
        },
        "Exit": {
            "item": None
        }
    }

    current_room = "Entrance"
    inventory = []
    items_to_collect = 6
    show_instructions()

    while True:
        show_status(current_room, inventory)

        command = input("\nEnter your move").strip().lower()

        if command == "quit":
            print("Thanks for playing!")
            break

        if command.startswith("go"):
            direction = command.split(" ")[1].capitalize()
            current_room = get_new_state(direction, current_room)

        elif command.startswith("get"):
            item_name = command.split(" ")[1].capitalize()
            if "item" in rooms[current_room] and rooms[current_room]["item"] == item:
                inventory.append(item)
                rooms[current_room]["item"] = None  # Remove item from room
                print(f"You picked up the {item}")
            else:
                print("That item is not here!")

        else:
            print("Invalid command!")

        if len(inventory) >= items_needed_to_win:
            print("\nCongratulations! You have collected all items and Won the Game.")
            break
        elif current_room == "Shifting Sands Room":
            print("\nYou Died in the Collapsing Caverns! Game over.")
            break


if __name__ == "__main__":
    main()





