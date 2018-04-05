# Order:
# - import statements (might)
# - class definition
#   - Items
#   - Characters
#   - Rooms
# - Instantiation of classes
# - Controller


class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def trade(self, person):
        if self.trade:
            self.value = True
        else:
            self.value = False
        print("%s traded with %s." % (person.name, self.name))

    def take(self, person):
        print("%s took %s." % (person.name, self.name))

    def drop(self, person):
        print("%s dropped %s." % (person.name, self.name))


class Consumables(Item):
    def __init__(self, name, value, color):
        super(Consumables, self).__init__(name, value)
        self.color = color

    def eat(self, person):
        print("%s is eating the %s" % (person.name, self.name))


class Fruits(Consumables):
    def __init__(self, name, value, color, taste):
        super(Fruits, self).__init__(name, value, color)
        self.taste = taste


class Coconuts(Consumables):
    def __init__(self, name, value, color, water):
        super(Coconuts, self).__init__(name, value, color)
        self.water = water

    def broke(self, person):
        print("%s broke the %s in half." % (person.name, self.name))


class Water(Consumables):
    def __init__(self, name, value, color):
        super(Water, self).__init__(name, value, color)

    def drink(self, person):
        print("%s drank the %s." % (person.name, self.name))

    def spill(self, person):
        print("%s spilled the %s." % (person.name, self.name))


class Ancient(Item):
    def __init__(self, name, value, color):
        super(Ancient, self).__init__(name, value)
        self.color = color


class Drum(Ancient):
    def __init__(self, name, value, color):
        super(Drum, self).__init__(name, value, color)

    def hit(self, person):
        print("%s hit the %s." % (person.name, self.name))


class ChiefHat(Ancient):
    def __init__(self, name, value, size, color):
        super(ChiefHat, self).__init__(name, value, color)
        self.size = size

    def wear(self, person):
        print("%s is wearing the %s." % (person.name, self.name))


class GrandmaItems(Ancient):
    def __init__(self, name, value, color, size):
        super(GrandmaItems, self).__init__(name, value, color)
        self.size = size


class Stick(GrandmaItems):
    def __init__(self, name, value, color, size):
        super(Stick, self).__init__(name, value, color, size)

    def attack(self, person):
        print("%s attacked with Grandma's %s." % (person.name, self.name))

    def defend(self, person):
        print("%s defended with Grandma's %s against %s." % (person.name, self.name, person.name))


class Necklace(GrandmaItems):
    def __init__(self, name, value, color, size, beads):
        super(Necklace, self).__init__(name, value, color, size)
        self.beads = beads

    def wear(self, person):
        print("%s is wearing the %s." % (person.name, self.name))


class Rug(GrandmaItems):
    def __init__(self, name, value, color, size):
        super(Rug, self).__init__(name, value, color, size)

    def moves(self):
        print("The %s has moved." % self.name)


class Toys(Item):
    def __init__(self, name, value, color, size):
        super(Toys, self).__init__(name, value)
        self.color = color
        self.size = size


class Ball(Toys):
    def __init__(self, name, value, color, size):
        super(Ball, self).__init__(name, value, color, size)

    def bounce(self):
        print("The %s is bouncing." % self.name)


class Shell(Toys):
    def __init__(self, name, value, color, size):
        super(Shell, self).__init__(name, value, color, size)

    def listen(self, person):
        print("%s is listening through the %s." % (person.name, self.name))


class Tools(Item):
    def __init__(self, name, value):
        super(Tools, self).__init__(name, value)

    def use(self, person):
        print("%s is using the %s." % (person.name, self.name))


class Sack(Tools):
    def __init__(self, name, value, color):
        super(Sack, self).__init__(name, value)
        self.color = color

    def put_in(self, person):
        print("%s put %s in the %s." % (person.name, self.name, self.name))


class Ladder(Tools):
    def __init__(self, name, value):
        super(Ladder, self).__init__(name, value)

    def climb(self, person):
        print("%s is climbing the %s." % (person.name, self.name))


class Paddle(Tools):
    def __init__(self, name, value, size):
        super(Paddle, self).__init__(name, value)
        self.size = size

    def attack(self, person):
        print("%s attacked with Grandma's %s." % (person.name, self.name))

    def defend(self, person):
        print("%s defended with Grandma's %s against %s." % (person.name, self.name, person.name))

    def paddle(self, person):
        print("%s is paddling with the %s" % (person.name, self.name))


class Boat(Tools):
    def __init__(self, name, value, size, sail):
        super(Boat, self).__init__(name, value)
        self.size = size
        self.sail = sail

    def sail(self, person):
        print("%s is sailing on a %s." % (person.name, self.name))


class Magic(Item):
    def __init__(self, name, value, color):
        super(Magic, self).__init__(name, value)
        self.color = color

    def use(self, person):
        print("%s is using the %s." % (person.name, self.name))


class Key(Magic):
    def __init__(self, name, value, color):
        super(Key, self).__init__(name, value, color)

    def open(self, person):
        print("%s is opening the %s with the %s." % (person.name, self.name, self.name))


class Treasure(Magic):
    def __init__(self, name, value, color, key):
        super(Treasure, self).__init__(name, value, color)
        self.key = key

    def open(self):
        print("The %s is open." % self.name)


class Heart(Magic):
    def __init__(self, name, value, color):
        super(Heart, self).__init__(name, value, color)

    def glow(self):
        print("%s glows." % self.name)


class MauiHook(Item):
    def __init__(self, name, value, color, shape):
        super(MauiHook, self).__init__(name, value)
        self.color = color
        self.shape = shape

    def attack(self, person):
        print("%s attacked with Grandma's %s." % (person.name, self.name))

    def defend(self, person):
        print("%s defended with Grandma's %s against %s." % (person.name, self.name, person.name))

    def glow(self, person):
        print("%s is glowing. %s is holding it." % (self.name, person.name))


class Character(object):
    def __init__(self, name, description, health, state, location, dmg=10):
        self.name = name
        self.inventory = []
        self.description = description
        self.health = health
        self.state = state
        self.location = location  # Must be a Room
        self.damage = dmg
        self.alive = True

    def take(self, item):
        self.inventory.append(item)
        print("Taken")

    def drop(self, item):
        self.inventory.remove(item)
        print("Dropped")

    def look(self):
        print(self.location.name)

    def read(self):
        self.state = "happy"
        print("Reading.")

    def climb(self):
        self.state = "happy"
        print("You are climbing.")

    def jump(self):
        self.state = "jumpy"
        print("You are jumping.")

    def take_damage(self, amt):
        if self.health <= 0:
            print("%s is already dead" % self.name)
            return
        self.health -= amt
        if self.health <= 0:
            self.alive = False
            print("%s has died." % self.name)

    def attack(self, target):
        if self.alive:
            print("%s attacks %s. %s's health is %d. The enemy's health is %d." % (self.name, target.name, self.name,
                                                                                   self.health,
                                                                                   target.health))
            target.take_damage(self.damage)
        else:
            print("%s is dead and cannot attack" % self.name)

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]


class Room(object):
    def __init__(self, name, north, south, east, west, down, up, northeast, northwest, southeast, southwest,
                 description, characters=8, items=None):
        if items is None:
            items = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.up = up
        self.southwest = southwest
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.description = description
        self.characters = characters
        self.items = items


moana_house = Room("Moana's House", 'ocean_shore', 'chief_stones', 'grandma_house', 'palm_trees', None, None, None,
                   None, None, None, 'This place is where Moana and Malawi '
                                     'lives with her family and there are 4 exits: to the '
                                     'west there is a path, \nto the east is where grandma lives, north is the '
                                     'ocean shore, and south is a path.')
chief_stones = Room("Chief's Stones Mountains", 'moana_house', None, None, None, None, None, 'grandma_house',
                    'palm_trees', None, None, 'You have arrived to a sacred place only for chiefs. '
                                              '\nThere is only a pile of stones and paths to the north '
                                              'and northwest and northeast.')
grandma_house = Room("Grandma's House", None, None, 'villager_homes', 'moana_house', 'cellar', None, None, None, None,
                     'chief_stones', 'Grandma lives and there are 3 exits: west, southwest and east.')
cellar = Room("Cellar", None, None, None, None, None, 'grandma_house', None, None, None, None,
              'There is a treasure chest.')
villager_homes = Room("Villager's Homes", None, None, None, 'grandma_house', None, None, None, 'fishing_area',
                      None, None,
                      'This is where all the villagers sleep and play. There are 2 paths: west and northwest.')
palm_trees = Room("Palm Trees", None, None, 'moana_house', 'other_ocean_shore', None, 'up_tree', None, None,
                  'chief_stones',
                  None,
                  'You are surrounded by palm trees with coconuts. There is a tree to your left that has a low '
                  '\nbranch and only one coconut. There are 4 paths: west to ocean shore, east is a path,\n '
                  'southeast is a path up the mountain, and north is a block by rocks that are not movable.')
up_tree = Room("Up the Tree", None, None, None, None, 'palm_trees', None, None, None, None, None,
               "You are up the tree and to your left you see the ocean. To your left, there is a coconut on a tree "
               "that's the only coconut there.")
other_ocean_shore = Room("The Other Ocean Shore", None, None, 'palm_trees', None, None, None, None, None, None, None,
                         'It is other ocean shore with the waterfall a path to the east,'
                         '\n and a path to the north that is blocked by a door.')
waterfall = Room("Waterfall", None, 'other_ocean_shore', 'hidden_cave', None, None, None, None, None, None, None,
                 ' There is a waterfall leading to the other ocean shore to the south.  '
                 '\nAlso, there is a path back east. Also, there are some boats. ')
hidden_cave = Room("The Hidden Cave", None, None, 'ocena_shore', 'waterfall', None, None, None, None, None, None,
                   'You found the hidden cave. There is only 2 exits: back to the east and to the west. ')
ocean_shore = Room("Ocean Shore", 'into_ocean', 'moana_house', 'fishing_area', None, None, None, None, None, None, None,
                   'You are in the middle of the ocean. There are 4 directions: north, east,'
                   '\n west - is blocked by rocks and you see a tiny hole - and back south.'
                   '\nI suggested to not go east until you find Maui. ')
fishing_area = Room("Fishing Area", None, None, None, 'waterfall', None, None, None, None, None, None,
                    'This is where there are fishing nets and 2 paths to the west and to the east. '
                    '\nAlso, there are some boats with paddles.')
into_ocean = Room("Into the Ocean", 'rilm_of_monster', 'ocean_shore', 'taca', 'island', None, None, 'Kakamora', None,
                  None,
                  None, 'You are in the middle of the ocean. There are 5 directions: west, north, east, northeast, '
                        'and back '
                        'south. \nI suggested to not go east until you find Maui. Be careful you can get attack by the '
                        'coconuts.')
coconuts = Room("Kakamora", None, None, None, None, None, None, None, None, None, 'into_ocean', "The Kakamora are "
                "coconuts that are evil. They will kill you unless you have the special item. "
                "The special item is grandma's stick to beat them up with.")
island = Room("A Mystery Island", None, None, 'into_ocean', 'big_cave', None, None, None, None, None, None,
              'You will find Maui on this island and you can go to the west and back to the east.')
big_cave = Room("A BIG Cave", None, None, 'island', None, None, None, None, None, None, None,
                'There is a cave with no doors and an exit back to the east; where you came from.')
taca = Room("Taca", None, None, None, 'into_ocean', None, None, None, None, None, None, 'Taca is the new enemy. '
            'How can you defeat Taca? Figure it out! '
            '\nThere is an exit back west and you can go east but you must defeat Taca.')
te_fiti = Room("An Island with Te Fit", None, None, None, None, None, None, None, None, None, None,
               'You defeated Taca.'
               ' Congrats. You completed the game.')
rilm_of_monster = Room("Rilm of Monsters", None, 'into_ocean', 'crab_layer', 'mission', None, None, None, None, None,
                       None, 'There are monsters here. To the east is the Crab Layer '
                       '\nand to the west is the Mission and back south.')
mission = Room("The Mission", None, None, 'rilm_of_monster', None, None, None, None, 'maui_hook', None, None,
               'Here you will find Maui’s hook here to your right is a note '
               '\nand to your northwest is a path and a path back to the east.')
maui_hook = Room("Maui's Hook Room", None, None, None, None, None, None, None, None, 'mission', None,
                 'You found Maui’s hook, but first you have to out the shell in the hole'
                 '\n with the shell hole to get the hook. '
                 '\nYou can go back to southeast to go back to the Mission.')
crab_layer = Room("Crab's Layer", None, None, None, 'rilm_of_monster', None, None, None, None, None, None,
                  'You are in the crab’s layer. If you don’t leave, you will died. '
                  '\nThe only exit is back to the west.')

moana = Character('Moana', "She has the power to find Maui and deliver him across the ocean.\n"
                           " She is the daughter of the chief. She has power of the ocean. \nShe thoroughly "
                           "thinks everything. She is positive. ", 100, 'happy', moana_house, 10)
maui = Character('Maui', "He has the hook from the gods. \nHe helps Moana find Te Fit and defeat Taca. "
                         "\nHe has animal changing powers", 1000, 'happy', island, 5)
malawi = Character('Malawi', "He has great sailing skills. He is also the long lost cousin/step-brother of Moana.\n "
                             "He is a great seeker. He lost is dad while going sailing and his mom abandoned him.\n "
                             "He is sad about that. He is adopted by Moana's family ", 100, 'sad', moana_house, 10)
grandma = Character('Grandma', 'She knows where the boats are at and she has items that you need.', 85, 'glad',
                    grandma_house, 10)
Tefiti = Character('Te Fiti', 'She gives good to the people.', 10000, 'always happy and positive', te_fiti, 5)
TACA = Character('Taca', 'She is powerful enough to destroy. \nShe has fire powers. Kill or...', 1000, 'angry', taca,
                 20)
villagers = Character('Villagers', 'They work and play around the island. \nThey could help.', 100, 'working',
                      villager_homes, 10)
mom = Character('Mom', 'She supports Moana, but follows what the chief says.\n She is the leaders of the village. '
                       'She will support you.', 100, 'willing', moana_house)
dad = Character('Chief or Dad', 'He doesn’t want Moana to go to the ocean. \nHe is the chief of the island. '
                                '\nHer dad knows every inch of Chief Mountain.', 100, 'serious and loving',
                chief_stones)
ocean = Character('Ocean', 'It is Moana friend. It helps Moana throughout the journey.', 1000, 'caring', into_ocean
                  and ocean_shore, 10)
kakamora = Character('Kakamora', 'Coconuts that are evil. \nThey will kill you unless you give them the heart. '
                                 'DON’T GIVE THEM THE HEART. \nFIGHT OR BAIL!', 1000, 'angry', coconuts, 25)
shiny = Character('Shiny the Crab', 'He loves gold and is annoying. '
                                    '\nHe will eat you unless you do something to prevent that.', 100, 'greedy',
                  crab_layer, 20)
monsters = Character('Monsters of the Rilm', 'They will eat you unless you kill them or run away.', 100, 'hungry',
                     rilm_of_monster, 30)

current_node = moana_house
directions = ['north', 'south', 'east', 'west', 'down', 'up', 'northeast', 'northwest', 'southeast', 'southwest']
short_directions = ['n', 's', 'e', 'w', 'd', 'u', 'ne', 'nw', 'se', 'sw']

# print("This is your character:")
# print("Name: %s" % moana.name)
# print("Health: %s" % moana.health)
# print("State of being: %s" % moana.state)
# print("Description: %s" % moana.description)
# print()
while True:
    print(moana.location.name)
    print(moana.location.description)
    command = input('>_').strip().lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        print("")
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            moana.move(command)
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not recognize.")
