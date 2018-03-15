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

# west_house = Room("West of House", "north_house")
# north_house = Room("North of House", None)


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
palm_trees = Room("Palm Trees", None, None, 'moana_house', 'other_ocean_shore', None, None, None, None, 'chief_stones',
                  None,
                  'You are surrounded by palm trees with coconuts. There is a tree to your left that has a low '
                  '\nbranch and only one coconut. There are 4 paths: west to ocean shore, east is a path,\n '
                  'southeast is a path up the mountain, and north is a block by rocks that are not movable.')
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
