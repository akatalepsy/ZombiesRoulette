def weapons():
    map_weapons = {
        0: "M1911",
        1: "RK5",
        2: "Argus",
        3: "L-CAR 9",
        4: "Pharo",
        5: "MP40",
        6: "Vesper",
        7: "VMP",
        8: "Sheiva",
        9: "KN-44",
        10: "ICR-1",
        11: "HVK-30",
        12: "M8A7",
        13: "Man-O-War",
        14: "Galil",
        15: "FFAR",
        16: "M16",
        17: "Weevil",
        18: "Kuda",
        19: "AK-74u",
        20: "205 Brecci",
        21: "Haymaker 12",
        22: "KRM-262",
        23: "Dingo",
        24: "BRM",
        25: "48 Dredge",
        26: "Gorgon",
        27: "RPK",
        28: "Locus",
        29: "Drakon",
        30: "SVG-100",
        31: "XM-53",
        32: "Ray Gun",
        33: "Ray Gun Mark II",
        34: "Thundergun"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 35)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 13)
    box_weapons = range(3, 35)

    handguns = (0, 1, 3)
    submachine_guns = (*range(4, 8), *range(17, 20))
    assault_rifles = range(8, 17)
    shotguns = (2, 20, 21, 22)
    sniper_rifles = (28, 29, 30)
    light_machine_guns = range(23, 28)
    heavy_weapons = 31
    wonder_weapons = (32, 33, 34)

    explosive_weapons = (31, 32)

    categories = {
        0: all_weapons,
        1: starting_weapons,
        2: wall_weapons,
        3: box_weapons,
        4: handguns,
        5: submachine_guns,
        6: assault_rifles,
        7: shotguns,
        8: sniper_rifles,
        9: light_machine_guns,
        10: heavy_weapons,
        11: wonder_weapons,
        12: explosive_weapons
    }

    category_list = '''
    0 = All weapons (35)

    Location:
    1 = Starting weapons (2)
    2 = Wall weapons (12)
    3 = Box weapons (32)

    Weapon Type:
    4 = Handguns (3)
    5 = Submachine guns (7)
    6 = Assault Rifles (9)
    7 = Shotguns (4)
    8 = Sniper rifles (3)
    9 = Light machine guns (5)
    10 = Heavy weapons (1)
    11 = Wonder weapons (3)

    Other Categories:
    12 = Explosive weapons (2)
    '''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def perks():
    map_perks = {
        1: "Jugger-Nog",
        2: "Quick Revive",
        3: "Speed Cola",
        4: "Mule Kick",
        5: "Double Tap II",
        6: "Widow's Wine",
        7: "Stamin-Up",
        8: "Deadshot Daiquiri"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 9)

    on_map_perks = range(1, 6)
    wunderfizz_only_perks = (6, 7, 8)

    speed_related_perks = (2, 3, 5, 7)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 5, 8)

    categories = {
        0: all_perks,
        1: on_map_perks,
        2: wunderfizz_only_perks,
        3: speed_related_perks,
        4: health_related_perks,
        5: weapon_related_perks
    }

    category_list = '''
    0 = All perks (8)

    Location:
    1 = On map perks (5)
    2 = Wunderfizz only perks (3)

    Function:
    3 = Speed (4)
    4 = Health (2)
    5 = Weapon (4)
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 13
    perk = 6

    return eval(category)