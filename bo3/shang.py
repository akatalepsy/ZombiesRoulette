def weapons():
    map_weapons = {
        0: "M1911",
        1: "RK5",
        2: "L-CAR 9",
        3: "Pharo",
        4: "Kuda",
        5: "VMP",
        6: "Sheiva",
        7: "ICR-1",
        8: "KN-44",
        9: "Man-O-War",
        10: "HVK-30",
        11: "FFAR",
        12: "Galil",
        13: "M16",
        14: "Vesper",
        15: "AK-74u",
        16: "Weevil",
        17: "KRM-262",
        18: "205 Brecci",
        19: "Argus",
        20: "Haymaker 12",
        21: "Dingo",
        22: "BRM",
        23: "48 Dredge",
        24: "Gorgon",
        25: "RPK",
        26: "Locus",
        27: "Drakon",
        28: "SVG-100",
        29: "L4 Siege",
        30: "XM-53",
        31: "Ray Gun",
        32: "Ray Gun Mark II",
        33: "31-79 JGb215"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 34)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 9)
    box_weapons = range(2, 34)

    handguns = (0, 1, 2)
    submachine_guns = (*range(3, 7), *range(14, 17))
    assault_rifles = range(6, 14)
    shotguns = range(17, 21)
    sniper_rifles = (26, 27, 28)
    light_machine_guns = range(21, 26)
    heavy_weapons = (29, 30)
    wonder_weapons = (31, 32, 33)

    explosive_weapons = (29, 30, 31)

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
    1 = Starting weapons ({len(starting_weapons)})
    2 = Wall weapons ({len(wall_weapons)})
    3 = Box weapons ({len(box_weapons)})

    Weapon Type:
    4 = Handguns ({len(handguns)})
    5 = Submachine guns ({len(submachine_guns)})
    6 = Assault Rifles ({len(assault_rifles)})
    7 = Shotguns ({len(shotguns)})
    8 = Sniper rifles ({len(sniper_rifles)})
    9 = Light machine guns ({len(light_machine_guns)})
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
        2: "Quick Revive",
        3: "Speed Cola",
        4: "Double Tap II",
        5: "Stamin-Up",
        6: "Deadshot Daiquiri",
        7: "Mule Kick",
        8: "Widow's Wine"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 9)

    speed_related_perks = range(2, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 6, 7)

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
    weapon = 13
    perk = 4

    return eval(category)
