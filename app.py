import maps
from roulette import choose_random


def choose(category):
    return input(f'Choose {category} (L for list): ').upper()


error = '''Invalid selection
'''
map_name = ''
weapons = ''
perks = ''
map_weapons = ''
map_perks = ''

games = {
    0: 'waw',
    1: 'bo1',
    2: 'bo2',
    3: 'bo3',
    4: 'bo4',
    5: 'aw',
    6: 'ww2',
    7: 'iw'
}
maps_list = {
    'waw': maps.waw_maps_list,
    'bo1': maps.bo1_maps_list,
    'bo2': maps.bo2_maps_list,
    'bo3': maps.bo3_maps_list,
    'bo4': maps.bo4_maps_list,
    'aw': maps.aw_maps_list,
    'ww2': maps.ww2_maps_list,
    'iw': maps.iw_maps_list
}

range_list = {
    'waw': 5,
    'bo1': 11,
    'bo2': 10,
    'bo3': 15,
    'bo4': 9,
    'aw': 5,
    'ww2': 10,
    'iw': 6
}
games_list = '''
Treyarch:
    0 = World at War
    1 = Black Ops
    2 = Black Ops II
    3 = Black Ops III
    4 = Black Ops IIII

Sledgehammer:
    5 = Advanced Warfare
    6 = WWII

Infinity Ward:
    7 = Infinite Warfare
        '''

while True:
    try:
        game = choose('Game')
        if game == 'L':
            print(games_list)
        elif int(game) in range(0, 8):
            game_name = games[int(game)]
            break
        else:
            print(error)
    except ValueError:
        print(error)

while True:
    try:
        map_number = choose('Map')
        if map_number == 'L':
            print(maps_list[game_name])
        elif int(map_number) in range(1, range_list[game_name]):
            exec(f'map_name = maps.{game_name}_maps[{int(map_number)}]')
            break
        else:
            print(error)
    except ValueError:
        print(error)

while True:
    weapons_or_perks = input('Choose Category ([W]eapons or [P]erks): ').upper()
    if weapons_or_perks == 'W':
        while True:
            try:
                weapons_per_player = int(input('Number of weapons per player: '))
                if int(weapons_per_player) > 0:
                    break
                else:
                    print(error)
            except ValueError:
                print(error)
        break
    elif weapons_or_perks == 'P':
        while True:
            try:
                perks_per_player = int(input('Number of perks per player: '))
                if int(perks_per_player) > 0:
                    break
                else:
                    print(error)
            except ValueError:
                print(error)
        break
    else:
        print(error)

while True:
# try:
    number_of_players = int(input('Number of players: '))
    if number_of_players > 0:
        if weapons_or_perks == 'W':
            exec(f'from {map_name} import weapons')
            choose_random(map_name.all_weapons, weapons_per_player, number_of_players, map_weapons)
        elif weapons_or_perks == 'P':
            exec(f'from {map_name} import perks')
            # for random_perk in random.sample(, )
        break
    else:
        print(error)
# except ValueError:
#     print(error)
#     print(type(number_of_players))