world_map = {
    'MOANA_HOUSE': {
        'NAME': "Moana's House",
        'DESCRIPTION': 'This place is where Moana lives with her family and there are 4 exits: to the west there is'
                       'a path, to the east is where grandma lives, north is the ocean shore, and south is a path.',
        'PATHS': {
            'NORTH': 'OCEAN_SHORE',
            'SOUTH': 'CHIEF_STONES',
            'WEST': 'PALM_TREES',
            'EAST': 'GRANDMA_HOME'

        }
    },
    'CHIEF_STONES': {
        'NAME': 'Chief’s stones mountain',
        'DESCRIPTION': 'You have arrived to a sacred place only for chiefs. '
                       'There is only a pile of stones and paths to the north and northwest and northeast.',
        'PATHS': {
            'NORTH': 'MOANA_HOUSE',
            'SOUTH': 'CHIEF_STONES',
            'NORTHWEST': 'PALM_TREES',
            'NORTHEAST': 'GRANDMA_HOME'
        }
    },
    'GRANDMA_HOUSE':  {
        'NAME': 'Grandma’s home',
        'DESCRIPTION': 'Grandma lives and there are 3 exits: west, southwest and east.',
        'PATHS': {
            'WEST': 'MOANA_HOUSE',
            'EAST': 'VILLAGER_HOMES'
        }
    },
    'VILLAGER_HOMES': {
        'NAME': "Villagers' Homes",
        'DESCRIPTION': 'This is where all the villagers sleep and play. There are 2 paths: west and northwest.',
        'PATHS': {
            'WEST': 'GRANDMA_HOUSE',
            'NORTHWEST': 'FISHING_AREA'
        }
    },
    'PALM_TREES': {
        'NAME': "Palm Trees",
        'DESCRIPTION': 'You are surrounded by palm trees with coconuts. There is a tree to your left that has a low '
                       'branch and only one coconut. There are 4 paths: west to ocean shore, east is a path, southeast '
                       'is a path up the mountain, and north is a block by rocks.',
        'PATHS': {
            'WEST': 'OTHER_OCEAN_SHORE',
            'EAST': 'MOANA_HOUSE',
            'SOUTHEAST': 'CHIEF_STONES'
        }
    },
    'OTHER_OCEAN_SHORE': {
        'NAME': "The Other Ocean Shore",
        'DESCRIPTION': ' It is other ocean shore with the waterfall to the north and a path to the east.',
        'PATHS': {
            'NORTH': 'WATERFALL',
            'EAST': 'PALM TREES'
        }
    },
    'WATERFALL': {
        'NAME': "Waterfall",
        'DESCRIPTION': ' There is a waterfall leading to the other ocean shore to the south.  '
                       'Also, there is a path back east. Also, there are some boats. ',
        'PATHS': {
            'SOUTH': 'OTHER_OCEAN_SHORE',
            'EAST': 'HIDDEN_CAVE'
        }
    },
    'HIDDEN_CAVE': {
        'NAME': "The Hidden Cave",
        'DESCRIPTION': 'You found the hidden cave. There is only 2 exits: back to the east and to the west. ',
        'PATHS': {
            'WEST': 'WATERFALL',
            'EAST': 'OCEAN_SHORE'
        }
    },
    'OCEAN_SHORE': {
        'NAME': "Ocean Shore",
        'DESCRIPTION': 'You are in the middle of the ocean. There are 4 directions: west, north, east, and back south.'
                       'I suggested to not go east until you find Mali. ',
        'PATHS': {
            'WEST': 'HIDDEN_CAVE',
            'EAST': 'FISHING_AREA',
            'SOUTH': "MOANA_HOUSE",
            'NORTH': 'INTO_OCEAN'
        }
    },
    'FISHING_AREA': {
        'NAME': "Fishing Area",
        'DESCRIPTION': 'This is where there are fishing nets and 2 paths to the west and to the east. '
                       'Also, there are some boats with paddles.',
        'PATHS': {
            'WEST': 'WATERFALL',
            'SOUTHEAST': "VILLAGER_HOMES"
        }
    },
    'INTO_OCEAN': {
        'NAME': "Into the Ocean",
        'DESCRIPTION': 'This is where there are fishing nets and 2 paths to the west and to the east. '
                       'Also, there are some boats with paddles.',
        'PATHS': {
            'WEST': 'WATERFALL',
            'SOUTHEAST': "VILLAGER_HOMES"
        }
    },

}

# current_node = world_map['WESTHOUSE']
# print(current_node['DESCRIPTION'])
# 15 rooms at least
# Have title, descriptions, and paths
