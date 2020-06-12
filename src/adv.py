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
    name = input("What's your name? ")
    player = init.player(name)

    print(f'''
    Hi {name}!
    Commands:
    Type "(n)orth", "(e)ast", "(s)outh", "(w)est" to move.
    Type "get" or "(t)ake" and name of item to pick it up.
    Type "(d)rop" and name of item to drop it.
    Type "(i)nventory" to check what you are carrying.
    Type "(l)ook" to check room for items.
    Type "(q)uit" to exit''')

    while True:
        command = input('What do you want to do? ').lower().split(' ')
        verb = command[0]
        obj = None
        if len(command) > 1:
            obj = command[1]

        # Quit command
        if verb == 'quit' or verb == 'q':
            print('Good bye!')
            break

        # Go command
        is_movement = init.is_movement(verb)
        if is_movement['status'] == True:
            try:
                success = player.move_to(is_movement['message'])
                if success == True:
                    print(f'You moved to {player.current_location.name}.')
                elif success == False:
                    print(f"You can't go there!")
            except ValueError:
                print("Something went wrong!")
                continue
        is_get = init.is_get(verb, obj)
        if is_get['status'] == True:
            try:
                if is_get['message'] != None:
                    print(is_get['message'])
                else:
                    if is_get == True:
                        item = [
                            item for item in player.items if item.name == obj]
                        success = player.take(item)
                        if success == True:
                            print(f"You picked up {item.name}")
            except ValueError:
                print("Something went wrong!")
                continue

        # Drop command

        # Inventory command

        # Look command


if __name__ == '__main__':
    mud()
