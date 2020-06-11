from room import Room
from player import Player

# Declare all the rooms


outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons")

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow =   Room("Narrow Passage", """The narrow passage bends here from west
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

def mud():
    directions = ['n', 'e', 's', 'w']
    name = input("What's your name? ")
    player = Player(name, outside)

    print(f'Hi {name}!\nYou can move around by typing (n)orth, (e)ast, (s)outh, (w)est. Or type (q) to exit')

    while True:
        direction = input('Which way? ').lower().strip()
        if direction == 'q':
            print('Good bye!')
            break

        if direction in directions:
            try:
                success = player.move_to(direction)
                if success == True:
                    print(f'You moved to {player.current_location.name}.')
                elif success == False:
                    print(f"You can't go there!")
            except ValueError:
                print("There's no room there.")
                continue



if __name__ == '__main__':
    mud()
