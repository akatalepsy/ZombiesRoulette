def weapons():
    map_weapons = {
        0: "M1911",
        1: "M14",
        2: "Olympia",
        3: "B23R",
        4: "MP5",
        5: "AK74u",
        6: "Colt M16A1",
        7: "Remington 870 MCS",
        8: "Five-Seven",
        9: "Five-Seven Dual Wield",
        10: "KAP-40",
        11: "Python",
        12: "Executioner",
        13: "Chicom CQB",
        14: "SMR",
        15: "FAL",
        16: "M8A1",
        17: "Type 25",
        18: "MTAR",
        19: "M27",
        20: "Galil",
        21: "M1216",
        22: "S12",
        23: "Barrett M82A1",
        24: "DSR 50",
        25: "HAMR",
        26: "RPD",
        27: "LSAT",
        28: "Ballistic Knife",
        29: "War Machine",
        30: "RPG",
        31: "Ray Gun",
        32: "Ray Gun Mark II"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 33)

    starting_weapons = 0
    wall_weapons = range(1, 8)
    box_weapons = range(8, 33)

    handguns = (0, 3, *range(8, 13))
    submachine_guns = (4, 5, 13)
    assault_rifles = (1, 6, *range(14, 21))
    shotguns = (2, 7, 21, 22)
    sniper_rifles = (23, 24)
    light_machine_guns = (25, 26, 27)
    special_weapons = 28
    heavy_weapons = (29, 30)
    wonder_weapons = (31, 32)

    explosive_weapons = range(29, 32)

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
        4: "Double Tap II"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 5)

    speed_related_perks = range(2, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4)

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
