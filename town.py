def weapons():
    map_weapons = {
        0: "M1911",
        1: "M14",
        2: "Olympia",
        3: "MP5",
        4: "Five-Seven",
        5: "Five-Seven Dual Wield",
        6: "KAP-40",
        7: "Python",
        8: "Executioner",
        9: "Chicom CQB",
        10: "SMR",
        11: "FAL",
        12: "M8A1",
        13: "Type 25",
        14: "MTAR",
        15: "Galil",
        16: "M1216",
        17: "S12",
        18: "Barrett M82A1",
        19: "DSR 50",
        20: "HAMR",
        21: "RPD",
        22: "Ballistic Knife",
        23: "War Machine",
        24: "RPG",
        25: "Ray Gun",
        26: "Ray Gun Mark II"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 27)

    starting_weapons = 0
    wall_weapons = range(1, 4)
    box_weapons = range(4, 27)

    handguns = (0, *range(4, 9))
    submachine_guns = (3, 9)
    assault_rifles = (1, *range(10, 16))
    shotguns = (2, 16, 17)
    sniper_rifles = (18, 19)
    light_machine_guns = (20, 21)
    special_weapons = 22
    heavy_weapons = (23, 24)
    wonder_weapons = (25, 26)

    explosive_weapons = range(23, 26)

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
        5: "Stamin-Up",
        6: "Tombstone Soda"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 7)
    solo_perks = range(1, 6)

    speed_related_perks = range(2, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4)

    categories = {
        0: all_perks,
        1: solo_perks,
        2: speed_related_perks,
        3: health_related_perks,
        4: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})
    1 = Solo perks ({len(solo_perks)})

    Function:
    2 = Speed ({len(speed_related_perks)})
    3 = Health ({len(health_related_perks)})
    4 = Weapon ({len(weapon_related_perks)})
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 14
    perk = 5

    return eval(category)