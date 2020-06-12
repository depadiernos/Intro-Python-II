import init

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
    player = init.player(name)

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
