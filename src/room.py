# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
    def __str__(self):
        return f"""Name: {self.name}
Description: {self.description}"""

    def add_item(self, item):
        self.items.append(item)
        return self.items
    
    def remove_item(self, item):
        self.items.remove(item)
        return self.items

    def get_items(self):
        if self.items == []:
            print("No items in room")
        for item in self.items:
            print(item)