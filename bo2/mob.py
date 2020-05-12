def weapons():
    map_weapons = {
        0: "M1911",
        1: "M14",
        2: "Olympia",
        3: "B23R",
        4: "MP5",
        5: "Uzi",
        6: "M1927",
        7: "Remington 870 MCS",
        8: "M1911",
        9: "Five-Seven Dual Wield",
        10: "Executioner",
        11: "PDW-57",
        12: "FAL",
        13: "MTAR",
        14: "AK-47",
        15: "Galil",
        16: "S12",
        17: "Barrett M82A1",
        18: "DSR 50",
        19: "LSAT",
        20: "Death Machine",
        21: "RPG",
        22: "Ray Gun",
        23: "Ray Gun Mark II",
        24: "Blundergat"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(1, 25)

    starting_weapons = 0
    wall_weapons = range(1, 8)
    box_weapons = range(8, 25)

    handguns = (3, *range(8, 11))
    submachine_guns = (4, 5, 6, 11)
    assault_rifles = (1, *range(12, 16))
    shotguns = (2, 7, 16)
    sniper_rifles = (17, 18)
    light_machine_guns = 19
    heavy_weapons = (20, 21)
    wonder_weapons = (22, 23, 24)

    explosive_weapons = (21, 22)

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
    9 = Light machine guns (1)
    10 = Heavy weapons ({len(heavy_weapons)})
    11 = Wonder weapons ({len(wonder_weapons)})

    Other Categories:
    12 = Explosive weapons ({len(explosive_weapons)})
    '''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def perks():
    map_perks = {
        1: "Jugger-Nog",
        2: "Speed Cola",
        3: "Double Tap II",
        4: "Deadshot Daiquiri",
        5: "Electric Cherry"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 6)

    speed_related_perks = (2, 3)
    weapon_related_perks = range(2, 6)

    categories = {
        0: all_perks,
        1: speed_related_perks,
        2: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Function:
    1 = Speed ({len(speed_related_perks)})
    2 = Weapon ({len(weapon_related_perks)})
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 13
    perk = 3

    return eval(category)
