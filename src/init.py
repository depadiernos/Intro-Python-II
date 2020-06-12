from player import Player
from room import Room
from item import Item

# Command functions


def is_movement(command):
    message = None
    if command == 'north' or command == 'n':
        message = "n"
    if command == 'east' or command == 'e':
        message = "e"
    if command == 'south' or command == 's':
        message = "s"
    if command == 'west' or command == 'w':
        message = "w"
    if message != None:
        return {"status": True, "message": message}
    return {"status": False, "message": message}

# Get or take command

def is_get(command, obj):
    if command in ['get', 'g', 'take', 't']:
        if obj == None:
            return {"status": True, "message": "Tell me which item."}
        return {"status": True, "message": None}
    return {"status": False, "message": None}

# Drop command

def is_drop(command, obj):
    if obj != None:
        return {"status": False, "message": "What do you want to take?"}
    if command in ['drop', 'd']:
        return {"status": True, "message": None}
    return {"status": False, "message": None}

# Inventory command

# Look command


# Declare all the rooms
outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons")

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")


# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

# Declare items

axe = Item("Axe", "It's a weapon.")
torch = Item("Torch", "Unlit torch.")
book = Item("Book", "It's a journal of someone exploring this region.")
shoe = Item("Shoe", "One shoe. Where is the other?")
box1 = Item("Box 1", "It's a box. Did you think there was treasure in it?")
box2 = Item("Box 2", "It's a box. Did you think there was treasure in it?")
box3 = Item("Box 3", "It's a box. Did you think there was treasure in it?")

# Place items in rooms

outside.items.append(torch)
foyer.items.append(book)
foyer.items.append(axe)
overlook.items.append(box1)
narrow.items.append(box2)
treasure.items.append(box3)
treasure.items.append(axe)

# Declare the player


def player(name):
    return Player(name, outside)
