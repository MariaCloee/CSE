import time
import datetime
import webbrowser
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
a = datetime.datetime.now()


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


class FruitBowl(Consumables):
    def __init__(self, name, value, color):
        super(FruitBowl, self).__init__(name, value, color)

    def combine(self, person):
        print("%s combined the %s with the %s." % (person.name, self.name, self.name))


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

    def get_on(self, person):
        print("%s gets on the %s." % (person.name, self.name))


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
        self.first_time = True
        self.first_time1 = True
        self.first_time2 = True
        self.first_time3 = True
        self.first_time4 = True
        self.first_time5 = True

    def take(self, item_object):
        if len(self.inventory) >= 10:
            print("You have too many items!")
            return False
        self.inventory.append(item_object)
        print("Taken")
        return True

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
        print("%s shoots a fire ball at %s's boat and misses." % (TACA.name, person.name))
        print("You are losing! What are you going to do to stop the fight and defeat Taca? Fight or...")

    # Finish Fight Scene

    def showing_heart(self):
        print("%s" % self.name)
        heart_name = command1[5:]
        for item1 in player.inventory:
            if heart_name == item1.name.lower():
                player.take(item1)
                heart_name = item1
        player.inventory.remove(heart)
        print("%s showed %s." % (player.name, heart.name))
        print("***Narrator***: You showed Taca the heart and Taca turned into Te Fiti. You did it. ")
        player.location = te_fiti

    def fight_coconuts(self):
        print('%s' % self.name)
        if heart in player.inventory:
            if stick in player.inventory:
                print("You invaded their place. Now you fight.....")
                print("Say attack to 'attack' or 'no more' to leave.")
                print("%s attacks with Grandma's Stick." % player.name)
                player.attack(kakamora)
                player.attack(kakamora)
                player.attack(kakamora)
                player.attack(kakamora)
                print("%s attacks with Bows and Arrows." % kakamora.name)
                kakamora.attack(player)
                kakamora.attack(player)
                kakamora.attack(player)
                kakamora.attack(player)
                print("%s attack but miss." % kakamora.name)
                print("%s attack but miss." % player.name)
                command3 = input(">_ ".lower().strip())
                if command3 == 'attack':
                    player.fight_coconuts()
                if command3 == 'no more':
                    print("They left.")
                    player.location.description = "There is no one to fight."
            if stick not in player.inventory:
                print("You don't have the Stick.")
        if heart not in player.inventory:
            print("You don't have the heart so they will not bothered you at all.")

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
        self.first_time = True
        self.first_time1 = True
        self.first_time2 = True
        self.first_time3 = True
        self.first_time4 = True
        self.first_time5 = True


# Items:
mango = Fruits('Mango', '$1', 'Green with red skin and yellow mango', 'delicious')
banana = Fruits('Banana', '$1', 'yellow', 'good')
magic_coconut = Coconuts('Magic Coconut', 'Valuable', 'brown with white', None)
the_coconuts = Coconuts('Coconuts', '$5', 'brown', 'There is water inside the coconuts to drink.')
water_bottle = Water('Water Bottle', '$3', 'clear')
drum = Drum("Magic Drum", 'Shows you the truth', 'wood brown')
# chief_hat = ChiefHat("Chief Hat", 'Makes you head of the village', 'Medium', 'Red & White & Light Brown')
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
fruitbowl = FruitBowl('FruitBowl', 'Great for minimizing your inventory. 3 for 1.', 'Colorful')

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
dad = Character('Dad', "He doesn’t want Moana to go to the ocean. \nHe is the chief of the island. "
                       "\nHer dad knows every inch of Chief Mountain.", 100, 'serious and loving')
ocean = Character('Ocean', 'It is Moana friend. It helps Moana throughout the journey.', 1000, 'caring', 10)
kakamora = Character('Kakamora', 'Coconuts that are evil. \nThey will kill you unless you give them the heart. '
                                 'DON’T GIVE THEM THE HEART. \nFIGHT OR BAIL!', 100, 'angry', 5)
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
                                              '\nThere is only a pile of stones, and paths to the \nnorth '
                                              'and northwest and northeast.', [dad], None, None)
grandma_house = Room("Grandma's House", None, None, 'villager_homes', 'moana_house', None, None, None, None, None,
                     'chief_stones', 'Grandma lives and there are 3 exits: \nwest, southwest and east. '
                                     'There is a rug in the middle of the room.', [grandma],
                     None, [stick, necklace])
cellar = Room("Cellar", None, None, None, None, None, 'grandma_house', None, None, None, None,
              'There is a treasure chest. The treasure is open. The treasure has something in it.', None, None, [key])
villager_homes = Room("Villager's Homes", None, None, None, 'grandma_house', None, None, None, 'fishing_area',
                      None, None,
                      'This is where all the villagers sleep and play. \nThere are 2 paths: west and northwest.',
                      [villagers], None, [water_bottle])
palm_trees = Room("Palm Trees", None, None, 'moana_house', 'other_ocean_shore', None, None, None, None,
                  'chief_stones',
                  None,
                  'You are surrounded by palm trees with coconuts. \nThere is a tree to your left that has a low '
                  '\nbranch and only one coconut. There are 4 paths: \nwest to ocean shore, east is a path,\n'
                  'southeast is a path up the mountain, and \nnorth is a block by rocks that are not movable.',
                  None, [villagers], [banana, mango, the_coconuts])
up_tree = Room("Up the Tree", None, None, None, None, None, None, None, None, None, None,
               "You are up the tree and to your left you see the ocean. \nTo your left, there is a coconut on a tree "
               "that's the only coconut there.", None, None, [magic_coconut])
other_ocean_shore = Room("The Other Ocean Shore", None, None, 'palm_trees', None, None, None, None, None, None, None,
                         'It is other ocean shore with a path to the east,'
                         '\n and a path to the north that is blocked by a door.', None, [ocean], None)
waterfall = Room("Waterfall", None, 'other_ocean_shore', 'hidden_cave', None, None, None, None, None, None, None,
                 ' There is a waterfall leading to the other ocean shore to the south.  '
                 '\nAlso, there is a path back east. Also, there are some boats. ', None, None, [travelling_boats])
hidden_cave = Room("The Hidden Cave", None, None, 'ocean_shore', 'waterfall', None, None, None, None, None, None,
                   'You found the hidden cave. \nThere is only 2 exits: back to the east and to the west.', None,
                   None, [paddle, drum])
ocean_shore = Room("Ocean Shore", None, 'moana_house', 'fishing_area', None, None, None, None, None, None, None,
                   'The name says it all. \nThis is where the ocean shore is at and where the beach is at.\n'
                   'There is paths in all main directions: \nnorth, east, south, and west. West is blocked by a door. '
                   '\n'
                   'You can go Into the Ocean until you find the travelling boats and get on the boat.',
                   None, [ocean, villagers], [shell])
fishing_area = Room("Fishing Area", None, None, None, None, None, None, None, None, 'villager_homes', None,
                    'This is where there are fishing nets and \nonly one path to the southeast. '
                    '\nAlso, there are some boats with paddles to fish with.', None, [ocean, villagers], None)
into_ocean = Room("Into the Ocean", 'rilm_of_monster', 'ocean_shore', 'taca', 'island', None, None, 'coconuts', None,
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
                 'You found Maui’s hook, but first you have to put the shell in the hole'
                 '\nwith the shell to get the hook. '
                 '\nYou can go back to southeast to go back to the Mission.', None, None, None)
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
    print("------------------------------------------------------------------------------------------------------")
    print("%s cheat sheets:\n" % player.name)
    print("Here is the commands you can type to get and use things:\n"
          "1) type 'inventory' to see your inventory\n"
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
          "17) type 'help' to show this again")


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
    print("------------------------------------------------------------------------------------------------------")
    print(player.location.name)
    print(player.location.description)

    if len(player.location.items) > 0:
        print("------------------------------------------------------------------------------------------------------")
        print("You can take and drop items from your inventory.\n"
              "You have to type the exact name shown below to take and drop item. \n"
              "The following items are here:")
        for num, item in enumerate(player.location.items):
            print(str(num + 1) + ") " + item.name)
    if len(player.location.characters) > 0:
        print("------------------------------------------------------------------------------------------------------")
        print("You need talk to characters.\nAll you have to do is type 'talk to' "
              "\nand you can talk to them. \nYou need talk to:")
        for num, character in enumerate(player.location.characters):   # Ask Wiebe why the pep happens
            print(str(num + 1) + ") " + character.name)
    elif len(player.location.characters) == 'None':
        print("There are no characters here.")
    # Timer Starts
    if player.location == crab_layer:
        a = datetime.datetime.now()
    command = input('>_ ').strip().lower()

    # handles specific events before processing
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    # Timer stops
    check_movement = False
    if player.location == crab_layer:
        b = datetime.datetime.now()
        check_movement = True
        duration_object = b - a
        if duration_object.days != 0 or duration_object.seconds > 10:
            print("You stayed to long.\n"
                  "You died. Game Over.")
            quit(0)

    # Movement
    elif command in directions:
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
            if character == moana and player.first_time is False:
                print("You already talk to Moana.")

            if character == moana and player.first_time is True:
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
                player.first_time = False

            elif character == malawi and player.first_time1 is False:
                print("You already talk to Malawi.")

            elif character == malawi and player.first_time1 is True:
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
                player.first_time1 = False

            elif character == mom and player.first_time2 is False:
                print("You already talk to Mom.")

            elif character == mom and player.first_time2 is True:
                print("Mom: You can do it great warrior. \nI will give you a clue to your quest. Find the sack first.\n"
                      "It will help you carry things along the way. \nHere is a riddle to find the sack: "
                      "The sack will be near the pack. Where is the pack?")
                # sack = villagers homes
                time.sleep(time_between)
                player.first_time2 = False

            elif character == dad and player.first_time3 is False:
                print("You already talk to Dad.")

            elif character == dad and player.first_time3 is True:
                print("Dad: Welcome to the Chief's Stones Mountains.")   # Add more dialogue with Dad
                time.sleep(time_between)
                player.first_time3 = False

            elif character == grandma and player.first_time4 is False:
                print("You already talk to Grandma.")

            elif character == grandma and player.first_time4 is True:
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
                player.first_time4 = False

            elif character == villagers and player.first_time5 is False:
                print("Can you you give me a ball?")
                answer = input(">_ ")
                correct = 'give ball'
                if correct in answer:
                    found = False
                    for item in player.inventory:
                        if isinstance(item, Ball):
                            found = True
                        if ball in player.inventory:
                            player.inventory.remove(ball)
                            print("You gave the ball to the little boy.")
                            print("Boy: Thank you.")
                            player.inventory.append(sack)
                            print("The boy gave you the sack.")
                            print("Your Inventory is:")
                            for num, thing in enumerate(player.inventory):
                                print(str(num + 1) + ") " + thing.name)
                                time.sleep(1.5)
                    if found is False:
                            print("You don't have the Child's ball.")

            elif character == villagers and player.first_time5 is True:
                print("**Narrator**: A little boy is near you and he has an item you need: the sack.")
                print("%s: Can I have the sack little boy?" % player.name)
                print("Boy: You can have it if you give me a blue ball that is really bounces. "
                      "Can you you give me a ball?")
                # Give Ball to Boy
                answer = input(">_ ")
                correct = 'give ball'
                if correct in answer:
                    found = False
                    for item in player.inventory:
                        if isinstance(item, Ball):
                            found = True
                        if ball in player.inventory:
                            player.inventory.remove(ball)
                            print("You gave the ball to the little boy.")
                            print("Boy: Thank you.")
                            player.inventory.append(sack)
                            print("The boy gave you the sack.")
                            print("Your Inventory is:")
                            for num, thing in enumerate(player.inventory):
                                print(str(num + 1) + ") " + thing.name)
                                time.sleep(1.5)
                    if found is False:
                            print("You don't have the Child's ball.")
                player.first_time5 = False
# Take
    elif 'take' in command:
        take_name = command[5:]
        found = False
        for item in player.location.items:
            if take_name == item.name.lower():
                if player.take(item):
                    found = item
        if found is False:
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
        if magic_coconut not in player.inventory:
            print("You don't have Magic Coconut.")

# Help
    elif 'help' in command:
        clues()

# Find Maui
    elif 'find' in command:
        find_name = command[5:]
        found = None
        for objects in player.location.non_talk_characters:
            if find_name == objects.name.lower():
                player.pep_with_you.append(objects)
                found = objects
                print("%s found %s. \nNow %s will be with you at all times \nand you can use %s for many things." %
                      (player.name, objects.name, objects.name, objects.name))
                print("Here is/are the people with you:")
                for num, thing in enumerate(player.pep_with_you):
                    print(str(num + 1) + ") " + thing.name)
        if found is None:
            print("Maui is not in this room.")
        else:
            player.location.non_talk_characters.remove(found)
            time.sleep(SLEEP_TIME)

# Fight scene with Taca
    elif command == 'fight':
        while player.location == taca:
            print("Remember you attack, TACA attacks more!")
            if heart not in player.inventory:
                print("You don't have the heart to show.")
            elif hook_maui not in player.inventory:
                print("You don't have Maui's Hook.")
            elif necklace not in player.inventory:
                print("You don't have Grandma's Necklace.")
            if maui in player.pep_with_you:
                # while True:
                command1 = input(">_ ".lower().strip())
                answer_name = 'attack'
                if answer_name in command1:
                    player.fight_taca(player)
                if command1 == 'show heart':
                    player.showing_heart()
                    player.location.east = te_fiti
                    print("You Did It!!!!!!!")
                    # quit(0)

        if maui not in player.pep_with_you:
            print("%s can't fight without Maui." % player.name)

# Fight with Coconuts
    elif 'fight with them' in command:
        if player.location == coconuts:
            if kakamora.health <= 0:
                print("They can't fight they are dead.")
            if kakamora.health != 0:
                player.fight_coconuts()

# Player dead
    elif player.health <= 0:
        print("You died.")
        quit(0)

# Find Te Fift
    elif player.location == te_fiti:
        quit(0)

# Boats
    elif command == 'get on the boat':
        if player.location == ocean_shore:
            if travelling_boats and paddle in player.inventory:
                travelling_boats.get_on(player)
                print("You got the boat and have open to the sea area called:")
                print("Into the Ocean!!!")
                player.location.north = 'into_ocean'
                if player.location.north == 'into_ocean':
                    print("You got the the whole sea to explore.")
            elif travelling_boats or paddle not in player.inventory:
                print("You don't have the travelling boats and/or paddle.")
        if player.location != ocean_shore:
            print('You need to be at the Ocean Shore to do this.')

# The other ocean shore door opening with key
    elif 'open door' in command:
        if key in player.inventory:
            print("You have a key to open the door at the:")
            if player.location == ocean_shore:
                print("The Ocean Shore")
            if player.location == other_ocean_shore:
                print("The Other Ocean Shore")
            print("You put the key in the hole....")
            if player.location == other_ocean_shore:
                player.location.north = 'waterfall'
                print("You have open 1 new place called: the Waterfall.")
                print("You kept the key.")
                if player.location.north == 'waterfall':
                    player.location.description = 'It is other ocean shore with the waterfall to the north,' \
                                                  ' a path to the east, ' \
                                                   '\n and a path to the north that is now open.'
            if player.location == ocean_shore:
                player.location.west = 'hidden_cave'
                print("You have open 1 new place called: the Hidden Cave")
                print("You kept the key.")
                if player.location.west == 'hidden_cave':
                    player.location.description = 'The name says it all. \nThis is where the ocean ' \
                                                  'shore is at and where the beach is at.\n' \
                                                      'There is paths in all main directions: \nnorth, east, south, ' \
                                                      'and west. West is now open.'
        if key not in player.inventory:
            print("You don't have the Magical Key.")

# Tree
    elif command == 'climb tree':
        player.location = up_tree

    elif command == 'climb back down':
        player.location = palm_trees
# Clues
    elif 'help' in command:
        clues()

# Put Fruit in Bowl
    elif command == 'combine':
        print("Do you want to minimize your inventory:")
        response1 = input(">_ ")
        if response1 == 'yes':
            found = False
            for item in player.inventory:
                if isinstance(item, Fruits):
                    found = True
                    player.inventory.remove(mango)
                    player.inventory.remove(banana)
                    player.inventory.remove(bowl)
                    player.inventory.append(fruitbowl)
                    print("You combine the fruits with the bowl.")
                    print("It turned into A ... FruitBowl!")
                    print('It takes your fruits and your bowl and')
        if response1 != 'yes':
            print("Okay! You lost your chance.")
        if player.inventory != mango and banana and bowl:
            print("You don't have all three items.")
# Eat
    elif 'eat mango' in command:
        mango.eat(player)
        print("Yummmm!!!!")
        if mango not in player.inventory:
            player.location.items.remove(mango)
        if mango in player.inventory:
            player.inventory.remove(mango)

    elif 'eat banana' in command:
        banana.eat(player)
        print("Delicious")
        if banana not in player.inventory:
            player.location.items.remove(banana)
        if banana in player.inventory:
            player.inventory.remove(banana)

    elif 'eat coconut' in command:
        the_coconuts.eat(player)
        if the_coconuts not in player.inventory:
            player.location.items.remove(the_coconuts)
        if the_coconuts in player.inventory:
            player.inventory.remove(the_coconuts)

    elif 'eat fruitbowl' in command:
        fruitbowl.eat(player)
        if fruitbowl not in player.inventory:
            player.location.items.remove(fruitbowl)
        if fruitbowl in player.inventory:
            player.inventory.remove(fruitbowl)

# Drink
    elif 'drink water' in command:
        if water_bottle in player.inventory:
            print("You drank the water.")
            player.inventory.remove(water_bottle)
        elif water_bottle not in player.inventory:
            print("You don't have the water bottle.")
# Shell
    elif command == 'put shell in hole':
        if player.location == maui_hook:
            if shell not in player.inventory:
                print("You don't have the shell.")
            shell_found = True
            hook_maui1 = False
            for item in player.inventory:
                if isinstance(item, Shell):
                    shell_found = True
                    hook_maui1 = False
                    print("The hole lowers and....")
                    print("Maui's hook pops out!")
                    player.take(hook_maui)
                    time.sleep(SLEEP_TIME / 2)
                    player.inventory.remove(shell)

# Note
    elif command == 'read note':
        if player.location == mission:
            print("--------------------------------------------------------------------------------------------"
                  "----------")
            print("Hint:\n"
                  "You thankful pick up this note.\n"
                  "You must have these 3 items to defeat Taca:\n"
                  "1) Maui's Hook\n"
                  "2) Grandma's Necklace\n"
                  "3) Te Fiti's Heart\n"
                  "Your Welcome")
            time.sleep(2)

# Rug
    elif command == 'move rug':
        if player.location == grandma_house:
            print("You found a place called the Cellar.")
            player.location.down = 'cellar'
            if player.location.down == 'cellar':
                player.location.description = 'Grandma lives and there are 4 exits: west, southwest,\n' \
                                              'now down (to the cellar) and east. There is a rug that was moved. '

# Inventory
    elif command == 'inventory':
        print("Your Inventory is:")
        for num, item in enumerate(player.inventory):
            print(str(num + 1) + ") " + item.name)
            time.sleep(1.5)
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

# Open Youtube
    elif command == 'open':
        webbrowser.open("www.youtube.com")

    else:
        print("Command not recognized.")

    if check_movement:
        if player.location == crab_layer:
            print("You stayed to long.\n"
                  "You died. Game Over.")
            quit(0)
