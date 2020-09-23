# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def list_items(self):
        return ', '.join(str(item.name) for item in self.items)

    def __str__(self):
        print(f'This is {self.name}. {self.description}. There is something in here: {self.list_items()}')