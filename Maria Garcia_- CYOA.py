# Order:
# - import statements (might)
# - class definition
#   - Items
#   - Characters
#   - Rooms
# - Instantiation of classes
# - Controller
# REMOVE THE DEFAULT CHARACTERS!!!!!


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

    def put(self, person):
        print("%s put the %s in the hole." % (person.name, self.name))


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
        print("%s put the %s in the %s." % (person.name, self.name, self.name))


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
    def __init__(self, name, value, color):
        super(Treasure, self).__init__(name, value, color)

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


class Bowl(Item):
    def __init__(self, name, value, color, size):
        super(Bowl, self).__init__(name, value)
        self.color = color
        self.size = size

    def put_in(self, person):
        print("%s put a %s in the %s." % (person.name, self.name, self.name))


class Character(object):
    def __init__(self, name, description, health, state, dmg=10):
        self.name = name
        self.inventory = []
        self.description = description
        self.health = health
        self.state = state
        self.damage = dmg
        self.alive = True
        self.location = None

    def take(self, item):
        self.inventory.append(item)
        print("Taken")

    def drop(self, item):
        self.inventory.remove(item)
        print("Dropped")

    # def look(self):
    #     print(self.location.name)

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
                 description, characters=None, items=None):
        if characters is None:
            characters = []
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


mango = Fruits('Mango', '$1', 'Green with red skin and yellow mango', 'delicious')
banana = Fruits('Banana', '$1', 'yellow', 'good')
magic_coconut = Coconuts('The One', 'Valuable', 'brown with white', None)
the_coconuts = Coconuts('Coconuts', '$5', 'brown', 'There is water inside the coconuts to drink.')
water_bottle = Water('Water Bottle', '$3', 'clear')
drum = Drum("Magic Drum", 'Shows you the truth', 'wood brown')
chief_hat = ChiefHat("Chief Hat", 'Makes you head of the village', 'Medium', 'Red & White & Light Brown')
stick = Stick("Grandma's Stick", 'Helps you along the way.', 'Light tan', 'Long')
necklace = Necklace("Grandma's Necklace", 'You need it to store the heart', 'Blue, White, and aqua', 'small',
                    '15 beads')
rug = Rug("Rug", 'Has a secret to share.', 'Rug with rings', 'Large')
ball = Ball("Child's Ball", 'Use for something on your boat.', 'blue', 'small')
shell = Shell('Shell', 'The key to a chest.', 'Pink with white.', 'Normal shell size.')
sack = Sack("Sack", 'You can put everything you find in it.', 'Brown')
ladder = Ladder('Ladder', 'Helps you climb.')
paddle = Paddle('Paddle', 'Useful for many things.', 'long')
fishing_boats = Boat('Fishing boats', 'Use for catching fishes.', 'large', 'Has a big sail')
travelling_boats = Boat('Travelling Boats', 'Use for travelling far places.', 'Larger or the same as '
                                                                              'than the fishing boats', "Bigger sail.")
key = Key('Magical Key', 'The key for a new path.', 'Gold')
treasure = Treasure("Treasure Chest", 'Contains one thing: Shell. No Key. You need the ball to put on the'
                                      ' hole at the top of the chest.', 'Gold with light brown')
heart = Heart("Te Fift's Heart", 'creates life or destroys life', 'glowing green')
hook_maui = MauiHook("Maui's Hook", 'Will help you defeat Taca.', 'White with blue handle', 'Hook Shape')
bowl = Bowl('Round Bowl', 'Use for put things like fruit in.', 'Gray that shines', 'Small bowl that may '
                                                                                   'fit in a small sack.')

moana = Character('Moana', "She has the power to find Maui and deliver him across the ocean.\n"
                           " She is the daughter of the chief. She has power of the ocean. \nShe thoroughly "
                           "thinks everything. She is positive. ", 100, 'happy', 10)
maui = Character('Maui', "He has the hook from the gods. \nHe helps Moana find Te Fit and defeat Taca. "
                         "\nHe has animal changing powers", 1000, 'happy', 5)
malawi = Character('Malawi', "He has great sailing skills. \nHe is also the long lost cousin/step-brother of Moana.\n "
                             "He is a great seeker. He lost is dad while going sailing and his mom abandoned him.\n "
                             "He is sad about that. \nHe is adopted by Moana's family ", 100, 'sad', 10)
grandma = Character('Grandma', 'She knows where the boats are at and she has items that you need.', 85, 'glad',
                    10)
TeFiti = Character('Te Fiti', 'She gives good to the people.', 10000, 'always happy and positive', 5)
TACA = Character('Taca', 'She is powerful enough to destroy. \nShe has fire powers. Kill or...', 1000, 'angry', 20)
villagers = Character('Villagers', 'They work and play around the island. \nThey could help.', 100, 'working',
                      10)
mom = Character('Mom', 'She supports Moana, but follows what the chief says.\n She is the leaders of the village. '
                       'She will support you.', 100, 'willing')
dad = Character('Chief or Dad', 'He doesn’t want Moana to go to the ocean. \nHe is the chief of the island. '
                                '\nHer dad knows every inch of Chief Mountain.', 100, 'serious and loving')
ocean = Character('Ocean', 'It is Moana friend. It helps Moana throughout the journey.', 1000, 'caring', 10)
kakamora = Character('Kakamora', 'Coconuts that are evil. \nThey will kill you unless you give them the heart. '
                                 'DON’T GIVE THEM THE HEART. \nFIGHT OR BAIL!', 1000, 'angry', 25)
shiny = Character('Shiny the Crab', 'He loves gold and is annoying. '
                                    '\nHe will eat you unless you do something to prevent that.', 100, 'greedy', 20)
monsters = Character('Monsters of the Rilm', 'They will eat you unless you kill them or run away.', 100, 'hungry', 30)

moana_house = Room("Moana's House", 'ocean_shore', 'chief_stones', 'grandma_house', 'palm_trees', None, None, None,
                   None, None, None, 'This place is where Moana and Malawi '
                                     'lives with her family and there are 4 exits: to the '
                                     'west there is a path, \nto the east is where grandma lives, north is the '
                                     'ocean shore, and south is a path.', [mom, moana, malawi])
chief_stones = Room("Chief's Stones Mountains", 'moana_house', None, None, None, None, None, 'grandma_house',
                    'palm_trees', None, None, 'You have arrived to a sacred place only for chiefs. '
                                              '\nThere is only a pile of stones and paths to the north '
                                              'and northwest and northeast.', [dad])
grandma_house = Room("Grandma's House", None, None, 'villager_homes', 'moana_house', 'cellar', None, None, None, None,
                     'chief_stones', 'Grandma lives and there are 3 exits: west, southwest and east.', [grandma])
cellar = Room("Cellar", None, None, None, None, None, 'grandma_house', None, None, None, None,
              'There is a treasure chest.', [None])
villager_homes = Room("Villager's Homes", None, None, None, 'grandma_house', None, None, None, 'fishing_area',
                      None, None,
                      'This is where all the villagers sleep and play. There are 2 paths: west and northwest.',
                      [villagers])
palm_trees = Room("Palm Trees", None, None, 'moana_house', 'other_ocean_shore', None, 'up_tree', None, None,
                  'chief_stones',
                  None,
                  'You are surrounded by palm trees with coconuts. There is a tree to your left that has a low '
                  '\nbranch and only one coconut. There are 4 paths: west to ocean shore, east is a path,\n '
                  'southeast is a path up the mountain, and north is a block by rocks that are not movable.',
                  [villagers])
up_tree = Room("Up the Tree", None, None, None, None, 'palm_trees', None, None, None, None, None,
               "You are up the tree and to your left you see the ocean. To your left, there is a coconut on a tree "
               "that's the only coconut there.", [None])
other_ocean_shore = Room("The Other Ocean Shore", None, None, 'palm_trees', None, None, None, None, None, None, None,
                         'It is other ocean shore with the waterfall a path to the east,'
                         '\n and a path to the north that is blocked by a door.', [ocean])
waterfall = Room("Waterfall", None, 'other_ocean_shore', 'hidden_cave', None, None, None, None, None, None, None,
                 ' There is a waterfall leading to the other ocean shore to the south.  '
                 '\nAlso, there is a path back east. Also, there are some boats. ', [None])
hidden_cave = Room("The Hidden Cave", None, None, 'ocean_shore', 'waterfall', None, None, None, None, None, None,
                   'You found the hidden cave. There is only 2 exits: back to the east and to the west.', [None])
ocean_shore = Room("Ocean Shore", 'into_ocean', 'moana_house', 'fishing_area', None, None, None, None, None, None, None,
                   'The name says it all. \nThis is where the ocean shore is at and where the beach is at.\n'
                   'There is paths in all main directions: \nnorth,east, south, and west. West is blocked by a door.',
                   [ocean, villagers])
fishing_area = Room("Fishing Area", None, None, None, 'waterfall', None, None, None, None, None, None,
                    'This is where there are fishing nets and 2 paths to the west and to the east. '
                    '\nAlso, there are some boats with paddles.', [ocean, villagers])
into_ocean = Room("Into the Ocean", 'rilm_of_monster', 'ocean_shore', 'taca', 'island', None, None, 'Kakamora', None,
                  None,
                  None, 'You are in the middle of the ocean. There are 5 directions: west, north, east, northeast, '
                        'and back '
                        'south. \nI suggested to not go east until you find Maui. Be careful you can get attack by the '
                        'coconuts.', [ocean])
coconuts = Room("Kakamora", None, None, None, None, None, None, None, None, None, 'into_ocean', "The Kakamora are "
                "coconuts that are evil. They will kill you unless you have the special item. "
                "The special item is grandma's stick to beat them up with.", [kakamora])
island = Room("A Mystery Island", None, None, 'into_ocean', 'big_cave', None, None, None, None, None, None,
              'You will find Maui on this island and you can go to the west and back to the east.', [maui])
big_cave = Room("A BIG Cave", None, None, 'island', None, None, None, None, None, None, None,
                'There is a cave with no doors and an exit back to the east; where you came from.', [None])
taca = Room("Taca", None, None, None, 'into_ocean', None, None, None, None, None, None, 'Taca is the new enemy. '
            'How can you defeat Taca? Figure it out! '
            '\nThere is an exit back west and you can go east but you must defeat Taca.', [TACA])
te_fiti = Room("An Island with Te Fit", None, None, None, None, None, None, None, None, None, None,
               'You defeated Taca.\n'
               ' Congrats. You completed the game.', [TeFiti])
rilm_of_monster = Room("Rilm of Monsters", None, 'into_ocean', 'crab_layer', 'mission', None, None, None, None, None,
                       None, 'There are monsters here. To the east is the Crab Layer '
                       '\nand to the west is the Mission and back south.', [monsters])
mission = Room("The Mission", None, None, 'rilm_of_monster', None, None, None, None, 'maui_hook', None, None,
               'Here you will find Maui’s hook here to your right is a note '
               '\nand to your northwest is a path and a path back to the east.', [None])
maui_hook = Room("Maui's Hook Room", None, None, None, None, None, None, None, None, 'mission', None,
                 'You found Maui’s hook, but first you have to out the shell in the hole'
                 '\n with the shell hole to get the hook. '
                 '\nYou can go back to southeast to go back to the Mission.', [None])
crab_layer = Room("Crab's Layer", None, None, None, 'rilm_of_monster', None, None, None, None, None, None,
                  'You are in the crab’s layer. If you don’t leave, you will died. '
                  '\nThe only exit is back to the west.', [shiny])

directions = ['north', 'south', 'east', 'west', 'down', 'up', 'northeast', 'northwest', 'southeast', 'southwest']
short_directions = ['n', 's', 'e', 'w', 'd', 'u', 'ne', 'nw', 'se', 'sw']
special_commands = ['i']   # i = inventory

# Character Selection
player = None
selection_complete = False
while not selection_complete:
    print("Who would you like to play as? Moana or Malawi?")
    player_selection = input(">_ ").lower().strip()
    if player_selection == "moana":
        player = moana
        selection_complete = True
    elif player_selection == 'malawi':
        player = malawi
        selection_complete = True
    else:
        print("Invalid option.")

player.location = moana_house
# Main Game
while True:
    # Room information
    print(player.location.name)
    print(player.location.description)

    command = input('>_').strip().lower()

    # handles specific events before processing
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    # Movement
    if command in directions:
        try:
            player.move(command)
        except KeyError:
            print("You cannot go that way.")
    # Talk to other character
    elif 'talk to' in command:
        character_name = command[8:]  # Finds the string of the character
        character = None
        for char in player.location.characters:
            if character_name == char.name.lower():
                character = char
        if character is None:
            print("Invalid character")
        else:
            if character == moana:
                print("Moana: Hi. \n"
                      "Moana: Welcome to the Save The World Game. Your goal is to find Te Fift and defeat Taca.\n"
                      "You have to collect series of items along the way. \nThere are some items that are necessary"
                      "\n"
                      "and some are not. You have to unlock new paths and finds clues. \nHint: Follow the right "
                      "path.\n"
                      'Moana: Are you Ready?')
                #  Add more directions
                response = input("%s: " % player.name).lower()
                if response == 'yes':
                    print("Lets Go!!")
                elif response == "no" or "maybe":
                    print("Moana: You can do it. Let's Go!!")
            if character == malawi:
                print("Malawi: Hi. \n"
                      "Malawi: Welcome to the Save The World Game. Your goal is to find Te Fift and defeat Taca.\n"
                      "You have to collect series of items along the way. \nThere are some items that are necessary"
                      "\n"
                      "and some are not. You have to unlock new paths and finds clues. \nHint: Follow the right "
                      "path.\n"
                      'Malawi: Are you Ready?')
                #  Add more directions
                response = input("%s: " % player.name).lower()
                if response == 'yes':
                    print("Lets Go!!")
                elif response == "no" or "maybe":
                    print("Malawi: You can do it. Let's Go!!")
            if character == mom:
                print("Mom: You can do great warrior. \nI will give you a clue to your quest. Find the sack first.\n"
                      "It will help you carry things along the way. \nHere is a riddle to find the sack: "
                      "The sack will be near the pack.")
                # sack = villagers homes

    else:
        print("Command not recognize.")
