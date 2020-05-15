from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [
                         Item('sword', 'a steel sword'),
                         Item('axe', 'a steel axe')
                     ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [
                         Item('helmet', 'a steel helmet'),
                         Item('gloves', 'leather gloves')
                     ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [
                         Item('ring', 'a silver ring'),
                         Item('shield', 'a steel shield')
                     ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [
                         Item('necklace', 'a gold necklace'),
                         Item('bracelet', 'a gold bracelet')
                     ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [
                         Item('chest', 'a mysterious treasure chest'),
                         Item('onion', 'an onion')
                     ]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Player 1', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print(player.name)

selection = ""
while selection != "q":
    curr_room = player.current_room
    print(f"Current Room: {curr_room.name}")
    print(f"{curr_room.description}")

    selection = input("Select an action to perform or a direction to move, or \"help\" for a list of commands: ")
    selection_split = selection.split(' ')
    if selection == "n" and curr_room.n_to is not None:
        player.current_room = curr_room.n_to
    elif selection == "s" and curr_room.s_to is not None:
        player.current_room = curr_room.s_to
    elif selection == "e" and curr_room.e_to is not None:
        player.current_room = curr_room.e_to
    elif selection == "w" and curr_room.w_to is not None:
        player.current_room = curr_room.w_to
    elif selection_split[0] == "list" and selection_split[1] == "items" and selection_split[2] == "in":
        if selection_split[3] == "room":
            curr_room.get_items()
        elif selection_split[3] == "bag":
            player.get_items()
    elif selection_split[0] == "take":
        try:
            item = [item for item in curr_room.items if item.name == selection_split[1]][0]
            player.pick_up_item(curr_room, item)
        except:
            print("Item not found in room")
    elif selection_split[0] == "drop":
        try:
            item = [item for item in player.items if item.name == selection_split[1]][0]
            player.drop_item(curr_room, item)
        except:
            print("Item not found in bag")
    elif selection_split[0] == "help":
        print("""You can move in a cardinal direction, eg \"n\", \"s\", \"e\", \"w\".
You can \"list items in bag\".
You can \"list items in room\".
You can \"take item ___\".
You can \"drop item ___\".
"q" to quit.""")
    elif selection != "q":
        print("That movement is not possible.")

print("Thanks for playing!")