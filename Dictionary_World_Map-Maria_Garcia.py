moana_map = {
    'MOANA_HOUSE': {
        'NAME': "Moana's House",
        'DESCRIPTION': 'This place is where Moana lives with her family and there are 4 exits: to the west there is'
                       ' a path, \nto the east is where grandma lives, north is the ocean shore, and south is a path.',
        'PATHS': {
            'NORTH': 'OCEAN_SHORE',
            'SOUTH': 'CHIEF_STONES',
            'WEST': 'PALM_TREES',
            'EAST': 'GRANDMA_HOUSE'

        }
    },
    'CHIEF_STONES': {
        'NAME': 'Chief’s stones mountain',
        'DESCRIPTION': 'You have arrived to a sacred place only for chiefs. '
                       '\nThere is only a pile of stones and paths to the north and northwest and northeast.',
        'PATHS': {
            'NORTH': 'MOANA_HOUSE',
            'NORTHWEST': 'PALM_TREES',
            'NORTHEAST': 'GRANDMA_HOUSE'
        }
    },
    'GRANDMA_HOUSE':  {
        'NAME': 'Grandma’s home',
        'DESCRIPTION': 'Grandma lives and there are 3 exits: west, southwest and east.',
        'PATHS': {
            'WEST': 'MOANA_HOUSE',
            'EAST': 'VILLAGER_HOMES',
            'DOWN': 'CELLAR',
            'SOUTHWEST': 'CHIEF_STONES'
        }
    },
    'CELLAR': {
        'NAME': 'Cellar',
        'DESCRIPTION': 'There is a treasure chest.',
        'PATHS': {
            'UP': 'GRANDMA_HOUSE'
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
                       '\nbranch and only one coconut. There are 4 paths: west to ocean shore, east is a path,\n '
                       'southeast is a path up the mountain, and north is a block by rocks that are not movable.',
        'PATHS': {
            'WEST': 'OTHER_OCEAN_SHORE',
            'EAST': 'MOANA_HOUSE',
            'SOUTHEAST': 'CHIEF_STONES'
        }
    },
    'OTHER_OCEAN_SHORE': {
        'NAME': "The Other Ocean Shore",
        'DESCRIPTION': ' It is other ocean shore with the waterfall a path to the east,'
                       '\n and a path to the north that is blocked by a door.',
        'PATHS': {
            # 'NORTH': 'WATERFALL',
            'EAST': 'PALM TREES'
        }
    },
    'WATERFALL': {
        'NAME': "Waterfall",
        'DESCRIPTION': ' There is a waterfall leading to the other ocean shore to the south.  '
                       '\nAlso, there is a path back east. Also, there are some boats. ',
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
        'DESCRIPTION': 'You are in the middle of the ocean. There are 4 directions: north, east,'
                       '\n west - is blocked by a door - and back south.'
                       '\nI suggested to not go east until you find Mali. ',
        'PATHS': {
            # 'WEST': 'HIDDEN_CAVE',
            'EAST': 'FISHING_AREA',
            'SOUTH': "MOANA_HOUSE",
            'NORTH': 'INTO_OCEAN'
        }
    },
    'FISHING_AREA': {
        'NAME': "Fishing Area",
        'DESCRIPTION': 'This is where there are fishing nets and 2 paths to the west and to the east. '
                       '\nAlso, there are some boats with paddles.',
        'PATHS': {
            'WEST': 'WATERFALL',
            'SOUTHEAST': "VILLAGER_HOMES"
        }
    },
    'INTO_OCEAN': {
        'NAME': "Into the Ocean",
        'DESCRIPTION': 'You are in the middle of the ocean. There are 4 directions: west, north, east, and back south.'
                       '\nI suggested to not go east until you find Mali.',
        'PATHS': {
            'WEST': 'ISLAND',
            'SOUTH': "OCEAN_SHORE",
            'EAST': 'TACA',
            'NORTH': "RILM_OF_MONSTER"

        }
    },
    'ISLAND': {
        'NAME': "A Mystery Island",
        'DESCRIPTION': 'You will find Mali on this island and you can go to the west and back to the east.',
        'PATHS': {
            'WEST': 'BIG_CAVE',
            'EAST': 'INTO_OCEAN'

        }
    },
    'BIG_CAVE': {
        'NAME': "A BIG Cave",
        'DESCRIPTION': 'There is a cave with no doors and an exit back to the east; where you came from.',
        'PATHS': {
            'EAST': 'ISLAND'

        }
    },
    'TACA': {
        'NAME': "TACA",
        'DESCRIPTION': 'Taca is the new enemy. How can you defeat Taca? Figure it out! '
                       '\nThere is an exit back west and you can go east but you must defeat Taca.',
        'PATHS': {
            # 'EAST': 'TE_FIT',
            'WEST': 'INTO_OCEAN'

        }
    },
    'TE_FIT': {
        'NAME': "An Island with Te Fit",
        'DESCRIPTION': 'You defeated Taca. Congrats. You completed the game.',
        'PATHS': {
            'WEST': 'TACA'

        }
    },
    'RILM_OF_MONSTER': {
        'NAME': "Rilm of Monster",
        'DESCRIPTION': 'There are monsters here. To the east is the Crab Layer '
                       '\nand to the west is the Mission and back south.',
        'PATHS': {
            'WEST': 'MISSON',
            'EAST': 'CRAB_LAYER',
            'SOUTH': 'INTO_OCEAN'

        }
    },
    'MISSON': {
        'NAME': "The Mission",
        'DESCRIPTION': 'Here you will find Mail’s hook here to your right is a note '
                       '\nand to your northwest is a path and a path back to the east.',
        'PATHS': {
            'NORTHWEST': 'MALI_HOOK',
            'EAST': 'RILM_OF_MONSTER'

        }
    },
    'MAIL_HOOK': {
        'NAME': "Mail's Hook Room",
        'DESCRIPTION': 'You found Mali’s hook, but first you have to out the shell in the hole'
                       '\n with the shell hole to get the hook. '
                       '\nYou can go back to southeast to go back to the Mission.',
        'PATHS': {
            'SOUTHEAST': 'MISSION'

        }
    },
    'CRAB_LAYER': {
        'NAME': "Crab's Layer",
        'DESCRIPTION': 'You are in the crab’s layer. If you don’t leave, you will died. '
                       '\nThe only exit is back to the west.',
        'PATHS': {
            'WEST': 'RILM_OF_MONSTER'

        }
    }
}

current_node = moana_map['MOANA_HOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'SOUTHEAST', 'NORTHEAST', 'SOUTHWEST', 'NORTHWEST', 'DOWN', 'UP']


while True:
    print(current_node["NAME"])
    print(current_node['DESCRIPTION'])
    command = input('>_').strip().upper()
    if command == 'QUIT':
        quit(0)
    elif command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = moana_map[name_of_node]
        except KeyError:
            print("You cannot go that way. ")
    else:
        print("Command not recognize.")
