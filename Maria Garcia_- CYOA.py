class Room(object):
    def __init__(self, name, north, south, east, west, down, up, northeast, northwest, southeast, southwest,
                 description, characters=None):
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

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]


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


class MaliHook(Item):
    def __init__(self, name, value, color, shape):
        super(MaliHook, self).__init__(name, value)
        self.color = color
        self.shape = shape

    def attack(self, person):
        print("%s attacked with Grandma's %s." % (person.name, self.name))

    def defend(self, person):
        print("%s defended with Grandma's %s against %s." % (person.name, self.name, person.name))

    def glow(self, person):
        print("%s is glowing. %s is holding it." % (self.name, person.name))


moana_house = Room("Moana's House", 'ocean_shore', 'chief_stones', 'grandma_house', 'palm_trees', None, None, None,
                   None, None, None, 'This place is where Moana lives with her family and there are 4 exits: to the '
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
                   '\nI suggested to not go east until you find Mali. ')
fishing_area = Room("Fishing Area", None, None, None, 'waterfall', None, None, None, None, None, None,
                    'This is where there are fishing nets and 2 paths to the west and to the east. '
                    '\nAlso, there are some boats with paddles.')
into_ocean = Room("Into the Ocean", 'rilm_of_monster', 'ocean_shore', 'taca', 'island', None, None, 'Kakamora', None,
                  None,
                  None, 'You are in the middle of the ocean. There are 5 directions: west, north, east, northeast, '
                        'and back '
                        'south. \nI suggested to not go east until you find Mali. Be careful you can get attack by the '
                        'coconuts.')
coconuts = Room("Kakamora", None, None, None, None, None, None, None, None, None, 'into_ocean', "The Kakamora are "
                "coconuts that are evil. They will kill you unless you have the special item. "
                "The special item is grandma's stick to beat them up with.")
island = Room("A Mystery Island", None, None, 'into_ocean', 'big_cave', None, None, None, None, None, None,
              'You will find Mali on this island and you can go to the west and back to the east.')

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
mission = Room("The Mission", None, None, 'rilm_of_monster', None, None, None, None, 'mali_hook', None, None,
               'Here you will find Mail’s hook here to your right is a note '
               '\nand to your northwest is a path and a path back to the east.')
mali_hook = Room("Mali's Hook Room", None, None, None, None, None, None, None, None, 'mission', None,
                 'You found Mali’s hook, but first you have to out the shell in the hole'
                 '\n with the shell hole to get the hook. '
                 '\nYou can go back to southeast to go back to the Mission.')
crab_layer = Room("Crab's Layer", None, None, None, 'rilm_of_monster', None, None, None, None, None, None,
                  'You are in the crab’s layer. If you don’t leave, you will died. '
                  '\nThe only exit is back to the west.')


player = Character("Player", 'Strong', 100, "Fine", moana_house)

current_node = moana_house
directions = ['north', 'south', 'east', 'west', 'down', 'up', 'northeast', 'northwest', 'southeast', 'southwest']
short_directions = ['n', 's', 'e', 'w', 'd', 'u', 'ne', 'nw', 'se', 'sw']


while True:
    print(player.location.name)
    print(player.location.description)
    command = input('>_').strip().lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            player.move(command)
        except KeyError:
            print("You cannot go that way. ")
    else:
        print("Command not recognize.")
