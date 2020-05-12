def weapons():
    map_weapons = {
        0: "M1911",
        1: "M14",
        2: "Olympia",
        3: "B23R",
        4: "MP5",
        5: "AK74u",
        6: "PDW-57",
        7: "Colt M16A1",
        8: "AN-94",
        9: "Remington 870 MCS",
        10: "SVU-AS",
        11: "Five-Seven",
        12: "Five-Seven Dual Wield",
        13: "KAP-40",
        14: "Python",
        15: "Executioner",
        16: "Chicom CQB",
        17: "SMR",
        18: "FAL",
        19: "M8A1",
        20: "Type 25",
        21: "MTAR",
        22: "Galil",
        23: "M1216",
        24: "S12",
        25: "Barrett M82A1",
        26: "DSR 50",
        27: "HAMR",
        28: "RPD",
        29: "Ballistic Knife",
        30: "War Machine",
        31: "RPG",
        32: "Ray Gun",
        33: "Ray Gun Mark II",
        34: "Sliquifier"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 35)

    starting_weapons = 0
    wall_weapons = range(1, 8)
    box_weapons = range(8, 35)

    handguns = (0, 3, *range(11, 16))
    submachine_guns = (*range(4, 7), 16)
    assault_rifles = (1, 7, 8, *range(17, 23))
    shotguns = (2, 9, 23, 24)
    sniper_rifles = (10, 25, 26)
    light_machine_guns = (27, 28)
    special_weapons = 29
    heavy_weapons = (30, 31)
    wonder_weapons = (32, 33, 34)

    explosive_weapons = range(27, 30)

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

    category_list = f'''
    0 = All weapons ({len(all_weapons)})
    
    Location:
    1 = Starting weapons (1)
    2 = Wall weapons ({len(wall_weapons)})
    3 = Box weapons ({len(box_weapons)})
    
    Weapon Type:
    4 = Handguns ({len(handguns)})
    5 = Submachine guns ({len(submachine_guns)})
    6 = Assault Rifles ({len(assault_rifles)})
    7 = Shotguns ({len(shotguns)})
    8 = Sniper rifles ({len(sniper_rifles)})
    9 = Light machine guns ({len(light_machine_guns)})
    10 = Special weapons (1)
    11 = Heavy weapons ({len(heavy_weapons)})
    12 = Wonder weapons ({len(wonder_weapons)})

    Other Categories:
    13 = Explosive weapons ({len(explosive_weapons)})
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
        4: "Double Tap II",
        5: "Mule Kick",
        6: "Who's Who"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 7)

    speed_related_perks = (2, 3, 4)
    health_related_perks = (1, 2, 6)
    weapon_related_perks = (3, 4, 5)

    categories = {
        0: all_perks,
        1: speed_related_perks,
        2: health_related_perks,
        3: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Function:
    1 = Speed ({len(speed_related_perks)})
    2 = Health ({len(health_related_perks)})
    3 = Weapon ({len(weapon_related_perks)})
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 14
    perk = 4

    return eval(category)