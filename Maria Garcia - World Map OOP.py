class Room(object):
    def __init__(self, name, north, south, east, west, down, up, northeast, northwest, southeast, southwest,
                 description):
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# west_house = Room("West of House", "north_house")
# north_house = Room("North of House", None)
moana_house = ("Moana's House", 'ocean_shore', 'chief_stones', 'grandma_house', 'palm_trees', None, None, None, None,
               None, None, 'This place is where Moana lives with her family and there are 4 exits: to the west there is'
                           ' a path, \nto the east is where grandma lives, north is the ocean shore, '
                           'and south is a path.')
chief_stones = Room("Chief's Stones Mountains", 'moana_house', None, None, None, None, None, 'grandma_house',
                    'palm_trees', None, None, 'You have arrived to a sacred place only for chiefs. '
                                              '\nThere is only a pile of stones and paths to the north '
                                              'and northwest and northeast.')
grandma_house = Room("Grandma's House", )
