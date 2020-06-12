# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location
        self.items = []

    def __str__(self):
        print(f'This is {self.name}. They are currently standing {self.current_location}')
    
    def move_to(self, direction):
        if direction == 'n' and self.current_location.n_to != None:
            self.current_location = self.current_location.n_to
            return True
        if direction == 'e' and self.current_location.e_to != None:
            self.current_location = self.current_location.e_to
            return True
        if direction == 's' and self.current_location.s_to != None:
            self.current_location = self.current_location.s_to
            return True
        if direction == 'w' and self.current_location.w_to != None:
            self.current_location = self.current_location.w_to
            return True
        return False

    def take(self, item):
        if item in self.current_location.items:
            self.items.append(item)
            self.current_location.items.remove(item)
            return True
        return False

    def drop(self, item):
        if item in self.items:
            self.items.remove(item)
            self.current_location.items.remove(item)
            return True
        return False