def games(item):
    game_list = '''
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

    game_dict = {
        0: 'waw',
        1: 'bo1',
        2: 'bo2',
        3: 'bo3',
        4: 'bo4',
        5: 'aw',
        6: 'ww2',
        7: 'iw'
    }

    if item is -2:
        return game_list
    elif item is -1:
        return len(game_dict)
    else:
        return game_dict[item]


def maps(game, item, number=0):

    # Treyarch Studios

    waw_maps_list = '''
    1 = Nacht der Untoten
    2 = Verrückt
    3 = Shi No Numa
    4 = Der Riese
        '''
    waw_maps = {
        1: 'waw_nacht',
        2: 'waw_verruckt',
        3: 'waw_numa',
        4: 'waw_riese'
    }

    bo1_maps_list = '''
    1 = Kino der Toten
    2 = "Five"
    3 = Ascension
    4 = Call of the Dead
    5 = Shangri-La
    6 = Moon
    7 = Nacht der Untoten
    8 = Verrückt
    9 = Shi No Numa
    10 = Der Riese
        '''
    bo1_maps = {
        1: 'bo1_kino',
        2: 'bo1_five',
        3: 'bo1_ascension',
        4: 'bo1_cotd',
        5: 'bo1_shang',
        6: 'bo1_moon',
        7: 'bo1_nacht',
        8: 'bo1_verruckt',
        9: 'bo1_numa',
        10: 'bo1_riese'
    }

    bo2_maps_list = '''
    1 = TranZit
    2 = Bus Depot
    3 = Town
    4 = Farm
    5 = Nuketown Zombies
    6 = Die Rise
    7 = Mob of the Dead
    8 = Buried
    9 = Origins
    '''
    bo2_maps = {
        1: 'bo2_tranzit',
        2: 'bo2_depot',
        3: 'bo2_town',
        4: 'bo2_farm',
        5: 'bo2_nuke',
        6: 'bo2_rise',
        7: 'bo2_mob',
        8: 'bo2_buried',
        9: 'bo2_origins'
    }

    bo3_maps_list = '''
    1 = Shadows of Evil
    2 = The Giant
    3 = Der Eisendrache
    4 = Zetsubou No Shima
    5 = Gorod Krovi
    6 = Revelations
    7 = Nacht der Untoten
    8 = Verrückt
    9 = Shi No Numa
    10 = Kino der Toten
    11 = Ascension
    12 = Shangri-La
    13 = Moon
    14 = Origins
    '''
    bo3_maps = {
        1: 'bo3_soe',
        2: 'bo3_giant',
        3: 'bo3_de',
        4: 'bo3_zns',
        5: 'bo3_gk',
        6: 'bo3_rev',
        7: 'bo3_nacht',
        8: 'bo3_verruckt',
        9: 'bo3_numa',
        10: 'bo3_kino',
        11: 'bo3_ascension',
        12: 'bo3_shang',
        13: 'bo3_moon',
        14: 'bo3_origins'
    }

    bo4_maps_list = '''
    1 = Voyage of Despair
    2 = IX
    3 = Blood of the Dead
    4 = Classified
    5 = Dead of the Night
    6 = Ancient Evil
    7 = Alpha Omega
    8 = Tag der Toten
    '''
    bo4_maps = {
        1: 'bo4_vod',
        2: 'bo4_ix',
        3: 'bo4_botd',
        4: 'bo4_classified',
        5: 'bo4_dotn',
        6: 'bo4_evil',
        7: 'bo4_omega',
        8: 'bo4_tag'
    }

    # Sledgehammer Games

    aw_maps_list = '''
    1 = Outbreak
    2 = Infection
    3 = Carrier
    4 = Descent
    '''
    aw_maps = {
        1: 'aw_outbreak',
        2: 'aw_infection',
        3: 'aw_carrier',
        4: 'aw_descent'
    }

    ww2_maps_list = '''
    1 = Gröesten Haus
    2 = The Final Reich
    3 = The Darkest Shore
    4 = The Shadowed Throne
    5 = The Tortured Path
    6 = Into the Storm
    7 = Across the Depth
    8 = Beneath the Ice
    9 = The Frozen Dawn
    '''
    ww2_maps = {
        1: 'ww2_haus',
        2: 'ww2_reich',
        3: 'ww2_shore',
        4: 'ww2_throne',
        5: 'ww2_path',
        6: 'ww2_storm',
        7: 'ww2_depth',
        8: 'ww2_ice',
        9: 'ww2_dawn'
    }

    # Infinity Ward

    iw_maps_list = '''
    1 = Zombies in Spaceland
    2 = Rave in the Redwoods
    3 = Shaolin Shuffle
    4 = Attack of the Radioactive Thing
    5 = The Beast from Beyond
    '''
    iw_maps = {
        1: 'iw_spaceland',
        2: 'iw_rave',
        3: 'iw_shaolin',
        4: 'iw_attack',
        5: 'iw_beyond'
    }

    ranges = {
        'waw': 5,
        'bo1': 11,
        'bo2': 10,
        'bo3': 15,
        'bo4': 9,
        'aw': 5,
        'ww2': 10,
        'iw': 6
    }

    if item == 'dict':
        return eval(f'{game}_maps[{number}]')
    elif item == 'list':
        return eval(f'{game}_maps_list')
    elif item == 'range':
        return ranges[game]
    else:
        pass