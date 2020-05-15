# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items = []):
        self.name = name
        self.current_room = current_room
        self.items = items
    def __str__(self):
        return f"""Name: {self.name}
Current Room: {self.current_room.name}"""

    def pick_up_item(self, room, item):
        self.items.append(item)
        room.remove_item(item)
        return self.items
    
    def drop_item(self, room, item):
        self.items.remove(item)
        room.add_item(item)
        return self.items

    def get_items(self):
        if self.items == []:
            print("No items in bag")
        for item in self.items:
            print(item)