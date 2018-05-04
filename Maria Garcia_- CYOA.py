import time
# Order:
# - import statements (might)
# - class definition
#   - Items
#   - Characters
#   - Rooms
# - Instantiation of classes
# - Controller
# REMOVE THE DEFAULT CHARACTERS!!!!!
# Items
SLEEP_TIME = 3


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

    def open(self, person):
        print("%s open the %s in half." % (person.name, self.name))

    def found(self, person, heartname):
        print("%s found the %s in the %s." % (person.name, heartname.name, self.name))


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
    def __init__(self, name, value, color, items):
        super(Sack, self).__init__(name, value)
        self.color = color
        self.items = items

    def open(self, person):
        print("%s opened the %s." % (person.name, self.name))


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


# Characters:
class Character(object):
    def __init__(self, name, description, health, state, dmg=10):
        self.name = name
        self.inventory = []
        self.pep_with_you = []
        self.description = description
        self.health = health
        self.state = state
        self.damage = dmg
        self.alive = True
        self.location = None

    def take(self, item_object):
        self.inventory.append(item_object)
        print("Taken")

    def drop(self, item_object):
        self.inventory.remove(item_object)
        print("Dropped")

    def fight_taca(self, person):
        print("%s" % self.name)
        print("%s is fighting Taca." % person.name)
        maui.attack(TACA)
        print("Attacks with Fireball:")
        TACA.attack(maui)
        TACA.attack(maui)
        TACA.attack(maui)
        TACA.attack(maui)
        TACA.attack(maui)
        print("%s shoots a fire ball at %s's boat and misses." % (taca.name, person.name))
        print("You are losing! What are you going to do to stop the fight and defeat Taca? Fight or...")
# Finish Fight Scene

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
        self.health -= amt
        if self.health <= 0:
            self.alive = False
            print("%s has died." % self.name)

    def attack(self, target):
        if self.alive:
            print("%s attacks %s. %s's health is %d. The %s's health is %d." % (self.name, target.name, self.name,
                                                                                self.health, target.name,
                                                                                target.health))
            target.take_damage(self.damage)
        else:
            print("%s is dead and cannot attack" % self.name)

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]


# Rooms:
class Room(object):
    def __init__(self, name, north, south, east, west, down, up, northeast, northwest, southeast, southwest,
                 description, characters=None, non_talk_characters=None, items=None):
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
        self.non_talk_characters = non_talk_characters
        self.items = items


# Items:
mango = Fruits('Mango', '$1', 'Green with red skin and yellow mango', 'delicious')
banana = Fruits('Banana', '$1', 'yellow', 'good')
magic_coconut = Coconuts('Magic Coconut', 'Valuable', 'brown with white', None)
the_coconuts = Coconuts('Coconuts', '$5', 'brown', 'There is water inside the coconuts to drink.')
water_bottle = Water('Water Bottle', '$3', 'clear')
drum = Drum("Magic Drum", 'Shows you the truth', 'wood brown')
chief_hat = ChiefHat("Chief Hat", 'Makes you head of the village', 'Medium', 'Red & White & Light Brown')
stick = Stick("Grandma's Stick", 'Helps you along the way.', 'Light tan', 'Long')
necklace = Necklace("Grandma's Necklace", 'You need it to store the heart', 'Blue, White, and aqua', 'small',
                    '15 beads')
rug = Rug("Rug", 'Has a secret to share.', 'Rug with rings', 'Large')
ball = Ball("Child's Ball", 'Use for something on your boat.', 'blue', 'small')  # payment for the little boy
shell = Shell('Shell', 'The key to a chest.', 'Pink with white.', 'Normal shell size.')
sack = Sack("Sack", 'You can put everything you find in it.', 'Brown', [])
ladder = Ladder('Ladder', 'Helps you climb.')  # Needed to get up the hole in maui's island
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

# Characters:
moana = Character('Moana', "She has the power to find Maui and deliver him across the ocean.\n"
                           " She is the daughter of the chief. She has power of the ocean. \nShe thoroughly "
                           "thinks everything. She is positive. ", 100, 'happy', 10)
maui = Character('Maui', "He has the hook from the gods. \nHe helps Moana find Te Fit and defeat Taca. "
                         "\nHe has animal changing powers", 1000, 'happy', 10)
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


# Rooms:
moana_house = Room("Moana's House", 'ocean_shore', 'chief_stones', 'grandma_house', 'palm_trees', None, None, None,
                   None, None, None, 'This place is where Moana and Malawi '
                                     'lives with her family and \nthere are 4 exits: to the '
                                     'west there is a path, \nto the east is where grandma lives, north is the '
                                     'ocean shore, and south is a path.', [moana, malawi, mom], None, [bowl, ball])
chief_stones = Room("Chief's Stones Mountains", 'moana_house', None, None, None, None, None, 'grandma_house',
                    'palm_trees', None, None, 'You have arrived to a sacred place only for chiefs. '
                                              '\nThere is only a pile of stones and paths to the \nnorth '
                                              'and northwest and northeast.', [dad], None, [chief_hat])
grandma_house = Room("Grandma's House", None, None, 'villager_homes', 'moana_house', 'cellar', None, None, None, None,
                     'chief_stones', 'Grandma lives and there are 3 exits: \nwest, southwest and east.', [grandma],
                     None, [stick, necklace, rug])    # fix
cellar = Room("Cellar", None, None, None, None, None, 'grandma_house', None, None, None, None,
              'There is a treasure chest. The treasure is open. Inside there is a key.', None, None, [treasure, key])
villager_homes = Room("Villager's Homes", None, None, None, 'grandma_house', None, None, None, 'fishing_area',
                      None, None,
                      'This is where all the villagers sleep and play. \nThere are 2 paths: west and northwest.',
                      [villagers], None, [sack, water_bottle])
palm_trees = Room("Palm Trees", None, None, 'moana_house', 'other_ocean_shore', None, None, None, None,
                  'chief_stones',
                  None,
                  'You are surrounded by palm trees with coconuts. \nThere is a tree to your left that has a low '
                  '\nbranch and only one coconut. There are 4 paths: \nwest to ocean shore, east is a path,\n'
                  'southeast is a path up the mountain, and \nnorth is a block by rocks that are not movable.',
                  None, [villagers], [mango, the_coconuts])
up_tree = Room("Up the Tree", None, None, None, None, None, None, None, None, None, None,
               "You are up the tree and to your left you see the ocean. \nTo your left, there is a coconut on a tree "
               "that's the only coconut there.", None, None, [magic_coconut])
other_ocean_shore = Room("The Other Ocean Shore", None, None, 'palm_trees', None, None, None, None, None, None, None,
                         'It is other ocean shore with the waterfall a path to the east,'
                         '\n and a path to the north that is blocked by a door.', None, [ocean], None)
waterfall = Room("Waterfall", None, 'other_ocean_shore', 'hidden_cave', None, None, None, None, None, None, None,
                 ' There is a waterfall leading to the other ocean shore to the south.  '
                 '\nAlso, there is a path back east. Also, there are some boats. ', None, None, [travelling_boats])
hidden_cave = Room("The Hidden Cave", None, None, 'ocean_shore', 'waterfall', None, None, None, None, None, None,
                   'You found the hidden cave. \nThere is only 2 exits: back to the east and to the west.', None,
                   None, [paddle, drum])
ocean_shore = Room("Ocean Shore", 'into_ocean', 'moana_house', 'fishing_area', None, None, None, None, None, None, None,
                   'The name says it all. \nThis is where the ocean shore is at and where the beach is at.\n'
                   'There is paths in all main directions: \nnorth, east, south, and west. West is blocked by a door.',
                   None, [ocean, villagers], [shell])
fishing_area = Room("Fishing Area", None, None, None, 'waterfall', None, None, None, None, 'villagers_homes', None,
                    'This is where there are fishing nets and \n2 paths to the west and to the southeast. '
                    '\nAlso, there are some boats with paddles.', None, [ocean, villagers], [fishing_boats])
into_ocean = Room("Into the Ocean", 'rilm_of_monster', 'ocean_shore', 'taca', 'island', None, None, 'Kakamora', None,
                  None,
                  None, 'You are in the middle of the ocean. \nThere are 5 directions: west, north, east, northeast, '
                        'and back '
                        'south. \nI suggested to not go east until you find Maui. \n'
                        'Be careful you can get attack by the '
                        'coconuts.', None, [ocean], None)
coconuts = Room("Kakamora", None, None, None, None, None, None, None, None, None, 'into_ocean', "The Kakamora are "
                "coconuts that are evil. \nThey will kill you unless you have the special item. "
                "\nThe special item is grandma's stick to beat them up with.", None, [kakamora], None)
island = Room("A Mystery Island", None, None, 'into_ocean', 'big_cave', None, None, None, None, None, None,
              'You will find Maui on this island and \nyou can go to the west and back to the east.', None, [maui],
              None)
big_cave = Room("A BIG Cave", None, None, 'island', None, None, None, None, None, None, None,
                'There is a cave with no doors and \nan exit back to the east; where you came from.', None, None,
                [ladder])
taca = Room("Taca", None, None, None, 'into_ocean', None, None, None, None, None, None, 'Taca is the new enemy. '
            'How can you defeat Taca? \nFigure it out! '
            '\nThere is an exit back west and \nyou can go east but you must defeat Taca.', None, [TACA], None)
te_fiti = Room("An Island with Te Fit", None, None, None, None, None, None, None, None, None, None,
               'You defeated Taca.\n'
               'Congrats. You completed the game.\n'
               'What is your response?', None, [TeFiti], None)
rilm_of_monster = Room("Rilm of Monsters", None, 'into_ocean', 'crab_layer', 'mission', None, None, None, None, None,
                       None, 'There are monsters here. \nTo the east is the Crab Layer '
                       '\nand to the west is the Mission and back south.', None, [monsters], None)
mission = Room("The Mission", None, None, 'rilm_of_monster', None, None, None, None, 'maui_hook', None, None,
               'Here you will find Maui’s hook here to your right is a note '
               '\nand to your northwest is a path and a path back to the east.', None, None, None)
maui_hook = Room("Maui's Hook Room", None, None, None, None, None, None, None, None, 'mission', None,
                 'You found Maui’s hook, but first you have to out the shell in the hole'
                 '\n with the shell hole to get the hook. '
                 '\nYou can go back to southeast to go back to the Mission.', None, None, [hook_maui])
crab_layer = Room("Crab's Layer", None, None, None, 'rilm_of_monster', None, None, None, None, None, None,
                  'You are in the crab’s layer. \nIf you don’t leave, you will died. '
                  '\nThe only exit is back to the west.', None, [shiny])

# Variables:
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


def clues():
    print("%s cheat sheets:\n" % player.name)
    print("Here is the commands you can type to get and use things:\n"
          "1) type 'i' to see your inventory\n"
          "2) type 'take[item name]' to take an item\n"
          "3) type 'drop[item name]' to drop an item\n"
          "4) type 'north' or 'n' to go north\n"
          "5) type 'south' or 's' to go south\n"
          "6) type 'west' or 'w' to go west\n"
          "7) type 'east' or 'e' to go east\n"
          "8) type 'northwest' or 'nw' to go northwest\n"
          "9) type 'northeast' or 'ne' to go northeast\n"
          "10) type 'southwest' or 'sw' to go southwest\n"
          "11) type 'up' or 'u' to go up\n"
          "12) type 'down' or 'd' to go down\n"
          "13) type 'open sack' to look in sack\n"
          "14) type move[item name] to move things\n"
          "15) type 'put' or 'leave' to put and drop things to and from your sack. \n"
          "16) type 'climb[item name]' to climb things.\n"
          "17) type 'clues' to show this again")
    time.sleep(5)


# clues()     # Redo this
player.location = moana_house
if player == moana:
    if player.location == moana_house:
        player.location.characters.remove(moana)
elif player == malawi:
    if player.location == moana_house:
        player.location.characters.remove(malawi)

# Main Game
while True:
    # Room information
    print()
    print(player.location.name)
    print(player.location.description)

    if len(player.location.items) > 0:
        print()
        print("You can take and drop items from your inventory.\n"
              "You have to type the exact name shown below to take and drop item. \n"
              "The following items are here:")
        for num, item in enumerate(player.location.items):
            print(str(num + 1) + ") " + item.name)
        print()
    if len(player.location.characters) > 0:
        print()
        print("You can talk to characters.\nAll you have to do is type 'talk to' "
              "\nand whoever you want and you can talk to them. \nYou can talk to:")
        for num, character in enumerate(player.location.characters):   # Ask Wiebe why the pep happens
            print(str(num + 1) + ") " + character.name)
    elif len(player.location.characters) == 'None':
        print("There are no characters here.")

    command = input('>_ ').strip().lower()

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
            time_between = 10
            if character == moana:
                print("Moana: Hi. \n"
                      "Moana: Welcome to the Save The World Game. Your goal is to find Te Fift and defeat Taca.\n"
                      "You have to collect series of items along the way. \nThere are some items that are necessary"
                      "\n"
                      "and some are not. You have to unlock new paths and finds clues. \nHint: Follow the right "
                      "path.\n"
                      'Moana: Are you Ready?')
                time.sleep(time_between)
                # Don't add more directions because I am going to add directions at the beginning of the game.
                response = input("%s: " % player.name).lower()
                if response == 'yes':
                    print("Lets Go!!")
                elif response == "no" or "maybe":
                    print("Moana: You can do it. Let's Go!!")
            elif character == malawi:
                print("Malawi: Hi. \n"
                      "Malawi: Welcome to the Save The World Game. Your goal is to find Te Fift and defeat Taca.\n"
                      "You have to collect series of items along the way. \nThere are some items that are necessary"
                      "\n"
                      "and some are not. You have to unlock new paths and finds clues. \nHint: Follow the right "
                      "path.\n"
                      'Malawi: Are you Ready? Yes or No or Maybe so')
                time.sleep(time_between)

                #  Add more directions
                response = input("%s: " % player.name).lower()
                if response == 'yes':
                    print("Malawi: Lets Go!!")
                elif response == "no" or "maybe" or "maybe so":
                    print("Malawi: You can do it. Let's Go!!")
            elif character == mom:
                print("Mom: You can do it great warrior. \nI will give you a clue to your quest. Find the sack first.\n"
                      "It will help you carry things along the way. \nHere is a riddle to find the sack: "
                      "The sack will be near the pack. Where is the pack?")
                # sack = villagers homes
                time.sleep(time_between)

            elif character == dad:
                print("Dad: Welcome to the Chief's Stones Mountains.")   # Add more dialogue with Dad
                time.sleep(time_between)

            elif character == grandma:
                print("Grandma: Hello my darling. \nYou have been chosen to deliver Maui across the ocean.")

                if player == moana:
                    print("Grandma: You have the power of the ocean sweetie. \nYou can do it.")
                    time.sleep(time_between)

                elif player == malawi:
                    print("Grandma: You have amazing sailing skills.\n"
                          "With your skills you can make it across the ocean.")
                print("Grandma: I will give you a hint to finding the items: \n"
                      "Some items are in my house. You can do it.")
                time.sleep(time_between)

            elif character == villagers:
                print("**Narrator**: A little boy is near you and he has an item you need: the sack.")
                print("%s: Can I have the sack little boy?" % player.name)
                print("Boy: You can have it if you give me a blue ball that is really bounces. "
                      "Can you you give me a ball?")
                time.sleep(time_between)

# Take
    elif 'take' in command:
        take_name = command[5:]
        found = None
        for item in player.location.items:
            if take_name == item.name.lower():
                player.take(item)
                found = item
        if found is None:
            print("Invalid Item")
        else:
            player.location.items.remove(found)
            time.sleep(SLEEP_TIME)

# Drop
    elif 'drop' in command:
        drop_name = command[5:]
        dropped = None
        for item in player.inventory:
            if drop_name == item.name.lower():
                player.drop(item)
                dropped = item
        if dropped is None:
            print("Invalid Item. Item not in inventory.")
        else:
            player.location.items.append(dropped)
            time.sleep(SLEEP_TIME)

# Put the heart in the key
    elif command == 'open magic coconut':
        heart_found = False
        magic_coconut_here = True
        for item in player.inventory:
            if isinstance(item, Coconuts):
                heart_found = True
                magic_coconut_here = False
                player.take(heart)
                magic_coconut.open(player)
                magic_coconut.found(player, heart)
                time.sleep(SLEEP_TIME / 2)
                player.inventory.remove(magic_coconut)
            elif heart_found is None:
                print("Heart not found.")
            else:
                print("You don't have that item.")

# Find Maui
    elif 'find' in command:
        find_name = command[5:]
        found = None
        for chars in player.location.non_talk_characters:
            if find_name == chars.name.lower():
                player.pep_with_you.append(chars)
                found = chars
                print("%s found %s. \nNow %s will be with you at all times \nand you can use %s for many things." %
                      (player.name, chars.name, chars.name, chars.name))
                print("Here is/are the people with you:")
                for num, charas in enumerate(player.pep_with_you):
                    print(str(num + 1) + ") " + charas.name)
        if found is None:
            print("Maui is not in this room.")
        else:
            player.location.non_talk_characters.remove(found)
            time.sleep(SLEEP_TIME)

# Fight scene
    elif command == 'fight':
        for maui in player.pep_with_you:
            player.fight_taca(player)
            command4 = input(">_ ".lower().strip())
            if command4 == 'show heart':
                heart_name = command[5:]
                for item1 in player.inventory:
                    if heart_name == item1.name.lower():
                        player.take(item1)
                        heart_name = item1
                player.inventory.remove(heart)
                print("%s showed %s." % (player.name, heart.name))
                print("***Narrator***: You showed Taca the heart and Taca turned into Te Fiti. You did it. ")
                player.location = te_fiti
            if heart not in player.inventory:
                print("You don't have the heart to show.")

        if maui not in player.pep_with_you:
            print("%s can't fight without Maui." % player.name)

# Find Te Fift
    elif player.location == te_fiti:
        quit(0)

# Tree
    elif command == 'climb tree':
        player.location = up_tree

    elif command == 'climb back down':
        player.location = palm_trees
# Clues
    elif command == 'clues':
        clues()
        print()
# Inventory
    elif command == 'i':
        print("Your Inventory is:")
        for num, item in enumerate(player.inventory):
            print(str(num + 1) + ") " + item.name)
            time.sleep(SLEEP_TIME)
# Sack
    elif command == 'open sack':
        found = False
        for item in player.inventory:
            if isinstance(item, Sack):
                found = True
                sack.open(player)
                time.sleep(SLEEP_TIME/2)
        if sack in player.inventory:
            print("Your Sack is:")
            for num, item in enumerate(sack.items):
                print(str(num + 1) + ") " + item.name)
                time.sleep(SLEEP_TIME)
        if sack not in player.inventory:
            print("%s doesn't have the sack." % player.name)

    elif 'put' in command:
        take_name = command[4:]
        found = None
        for item in player.inventory:
            if take_name == item.name.lower():
                sack.items.append(item)
                found = item
                print("%s is in sack." % item.name)
        if found is None:
            print("Invalid Item")
        else:
            player.inventory.remove(found)
            time.sleep(SLEEP_TIME)
    elif 'leave' in command:
        drop_name = command[6:]
        dropped = None
        for item in sack.items:
            if drop_name == item.name.lower():
                sack.items.remove(item)
                dropped = item
                print("%s left the sack." % item.name)
        if dropped is None:
            print("Invalid Item. Item not in sack.")
        else:
            player.location.items.append(dropped)
            time.sleep(SLEEP_TIME)

    else:
        print("Command not recognized.")
