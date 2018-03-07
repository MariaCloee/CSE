class Character(object):
    def __init__(self, name, description, health, state, location):
        self.name = name
        self.inventory = []
        self.description = description
        self.health = health
        self.state = state
        self.location = location  # Must be a Room

    def take(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def look(self):
        print(self.location.name)

    def read(self):
        print("Reading.")

    def climb(self):
        self.state = "happy"
        print(self.state)

    def jump(self):
        self.state = "jumpy"
        print(self.location.name)


# characters = ['Moana', 'Mali', 'Grandma', 'Mom', 'Dad']
#
# character_choosing = input('Which character do you?').lower
# if input == characters:
#     print("You are %s." % character_choosing)
