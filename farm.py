def weapons():
    map_weapons = {
        0: "M1911",
        1: "Olympia",
        2: "MP5",
        3: "Five-Seven",
        4: "Five-Seven Dual Wield",
        5: "KAP-40",
        6: "Python",
        7: "Executioner",
        8: "Chicom CQB",
        9: "SMR",
        10: "FAL",
        11: "M8A1",
        12: "Type 25",
        13: "MTAR",
        14: "Galil",
        15: "M1216",
        16: "S12",
        17: "Barrett M82A1",
        18: "DSR 50",
        19: "HAMR",
        20: "RPD",
        21: "Ballistic Knife",
        22: "War Machine",
        23: "RPG",
        24: "Ray Gun",
        25: "Ray Gun Mark II"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 26)

    starting_weapons = 0
    wall_weapons = range(1, 3)
    box_weapons = range(3, 26)

    handguns = (0, *range(3, 8))
    submachine_guns = (2, 8)
    assault_rifles = range(9, 15)
    shotguns = (1, 15, 16)
    sniper_rifles = (17, 18)
    light_machine_guns = (19, 20)
    special_weapons = 21
    heavy_weapons = (22, 23)
    wonder_weapons = (24, 25)

    explosive_weapons = range(22, 25)

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
        2: "Speed Cola",
        3: "Quick Revive",
        4: "Double Tap II"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 5)

    speed_related_perks = range(2, 5)
    health_related_perks = (1, 3)
    weapon_related_perks = (2, 4)

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