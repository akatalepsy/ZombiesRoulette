def weapons():
    map_weapons = {
        0: "M1911",
        1: "Olympia",
        2: "M14",
        3: "PM63",
        4: "MPL",
        5: "MP5k",
        6: "AK74u",
        7: "M16",
        8: "Stakeout",
        9: "CZ75",
        10: "CZ75 Dual Wield",
        11: "Python",
        12: "Spectre",
        13: "FN FAL",
        14: "G11",
        15: "Famas",
        16: "AUG",
        17: "Commando",
        18: "Galil",
        19: "HS-10",
        20: "SPAS-12",
        21: "Dragunov",
        22: "L96A1",
        23: "RPK",
        24: "HK21",
        25: "Ballistic Knife",
        26: "Crossbow",
        27: "China Lake",
        28: "M72 LAW",
        29: "Ray Gun",
        30: "Thundergun"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 32)

    starting_weapons = 0
    wall_weapons = range(1, 9)
    box_weapons = range(9, 31)

    handguns = (0, 9, 10, 11)
    submachine_guns = (*range(3, 7), 12)
    assault_rifles = (2, 7, *range(13, 19))
    shotguns = (1, 8, 19, 20)
    sniper_rifles = (21, 22)
    light_machine_guns = (23, 24)
    special_weapons = (25, 26)
    heavy_weapons = (27, 28)
    wonder_weapons = (29, 30)

    explosive_weapons = range(26, 30)

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
        10: special_weapons,
        11: heavy_weapons,
        12: wonder_weapons,
        13: explosive_weapons
    }

    category_list = '''
    0 = All weapons (31)

    Location:
    1 = Starting weapons (1)
    2 = Wall weapons (8)
    3 = Box weapons (22)

    Weapon Type:
    4 = Handguns (4)
    5 = Submachine guns (5)
    6 = Assault Rifles (8)
    7 = Shotguns (4)
    8 = Sniper rifles (2)
    9 = Light machine guns (2)
    10 = Special weapons (2)
    11 = Heavy weapons (2)
    12 = Wonder weapons (2)

    Other Categories:
    13 = Explosive weapons (4)
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
        5: "PhD Flopper",
        6: "Stamin-Up"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 7)

    lander_area_perks = (2, 4, 5, 6)
    central_area_perks = (1, 2)

    speed_related_perks = (2, 3, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4)

    categories = {
        0: all_perks,
        1: lander_area_perks,
        2: central_area_perks,
        3: speed_related_perks,
        4: health_related_perks,
        5: weapon_related_perks
    }

    category_list = '''
    0 = All perks (6)

    Location:
    1 = Lander areas (4)
    2 = Central area (2)

    Function:
    3 = Speed (3)
    4 = Health (2)
    5 = Weapon (2)
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 14
    perk = 6

    return eval(category)
