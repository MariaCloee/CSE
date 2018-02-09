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
    }
}

current_node = world_map['WESTHOUSE']
print(current_node['DESCRIPTION'])
# 15 rooms at least
# Have title, descriptions, and paths
