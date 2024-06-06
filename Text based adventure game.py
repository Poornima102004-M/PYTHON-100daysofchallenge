import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def display_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print("Inventory:", self.inventory)

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

def main():
    # Create rooms
    living_room = Room("Living Room", "A cozy room with a fireplace.")
    kitchen = Room("Kitchen", "A spacious kitchen with modern appliances.")
    bedroom = Room("Bedroom", "A comfortable bedroom with a large bed.")

    # Connect rooms
    living_room.add_exit("east", kitchen)
    kitchen.add_exit("west", living_room)
    kitchen.add_exit("north", bedroom)
    bedroom.add_exit("south", kitchen)

    # Start the game
    print("Welcome to the Text Adventure Game!")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    current_room = living_room

    while True:
        print("\n" + "-"*20)
        print("Current Location:", current_room.name)
        print(current_room.description)
        player.display_status()

        # Check for exits
        if len(current_room.exits) == 0:
            print("You've reached the end of the game!")
            break

        # Ask for player's action
        action = input("Choose your next move (e.g., go east): ").lower().split()
        if len(action) != 2 or action[0] != "go" or action[1] not in current_room.exits:
            print("Invalid action!")
            continue

        # Move to the next room
        direction = action[1]
        current_room = current_room.exits[direction]

        # Simulate some time passing
        time.sleep(1)

if __name__ == "__main__":
    main()
