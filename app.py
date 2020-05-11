from games import *
from roulette import *


def choose(category):
    return input(f'Choose {category} (L for list): ').upper()


def has_one(category, item):
    return f'''
This {category} only has one {item}!'''


def has_none(item):
    return f'''
This map has no {item}s!'''


error = '''
Invalid selection'''
include_upgrade_query = None
include_packed_weapons = None
packed_weapons_only = None
test = 'test'


try:
    while True:
        try:
            game = choose('Game')
            if game == 'L':
                print(games(-2))
            elif int(game) in range(0, games(-1)):
                game_name = games(int(game))
                break
            else:
                print(error)
        except ValueError:
            print(error)

    while True:
        try:
            map_number = choose('Map')
            if map_number == 'L':
                print(maps(game_name, 'list'))
            elif int(map_number) in range(1, maps(game_name, 'range')):
                map_name = maps(game_name, 'dict', int(map_number))
                not_found = False
                try:
                    exec(f'from {map_name} import category_range_list')
                except ModuleNotFoundError:
                    not_found = True
                    print('''
    This map hasn't been added yet.''')
                if not_found is True:
                    pass
                else:
                    break
            else:
                print(error)
        except ValueError:
            print(error)

    while True:
        while True:
            weapons_or_perks = input('Choose Category ([W]eapons or [P]erks): ').upper()
            if weapons_or_perks == 'W':
                weapons_or_perks = 'weapon'
                include_upgrade_query = True
                break
            elif weapons_or_perks == 'P':
                weapons_or_perks = 'perk'
                include_upgrade_query = False
                break
            else:
                print(error)
        if category_range_list(f'{weapons_or_perks}') > 1:
            break
        elif category_range_list(f'{weapons_or_perks}') > 0:
            print(has_one('map', f'{weapons_or_perks}'))
        else:
            print(has_none(f'{weapons_or_perks}'))

    exec(f'from {map_name} import {weapons_or_perks}s, {weapons_or_perks}_categories')
    categories = eval(f'{weapons_or_perks}_categories')
    dictionary = eval(f'{weapons_or_perks}s()')

    while True:
        try:
            subset = choose('Category')
            range_high = category_range_list(f'{weapons_or_perks}')
            if subset == 'L':
                category_list = categories('l')
                print(category_list)
            elif int(subset) in range(0, range_high):
                subset = categories(subset)
                if type(subset) is int:
                    print(has_one('category', weapons_or_perks))
                else:
                    num_set = subset
                    break
            else:
                print(error)
        except ValueError:
            print(error)

    while True:
        if include_upgrade_query is True:
            include_packed_weapons = input('Include Pack-a-Punched weapons? [Y]es, [N]o or [O]nly: ').upper()
            if include_packed_weapons == 'Y':
                include_packed_weapons = True
                packed_weapons_only = False
                break
            elif include_packed_weapons == 'N':
                include_packed_weapons = False
                break
            elif include_packed_weapons == 'O':
                include_packed_weapons = True
                packed_weapons_only = True
                break
            else:
                print(error)

    while True:
        try:
            items_per_player = int(input(f'Number of {weapons_or_perks}s per player: '))
            if items_per_player in range(1, len(subset) + 1):
                number_of_choices = items_per_player
                break
            else:
                print(error)
        except ValueError:
            print(error)

    while True:
        try:
            number_of_players = int(input('Number of players: '))
            if number_of_players > 0:
                selections = choose_random(num_set, number_of_choices, number_of_players, dictionary)
                break
            else:
                print(error)
        except ValueError:
            print(error)

    if include_packed_weapons is True:
        if packed_weapons_only is True:
            pass
        else:
            pass
    else:
        pass
except KeyboardInterrupt:
    pass