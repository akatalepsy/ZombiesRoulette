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
        19: "Galil",
        20: "M1216",
        21: "S12",
        22: "Barrett M82A1",
        23: "DSR 50",
        24: "HAMR",
        25: "RPD",
        26: "Ballistic Knife",
        27: "War Machine",
        28: "RPG",
        29: "Ray Gun",
        30: "Ray Gun Mark II"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 31)

    starting_weapons = 0
    wall_weapons = range(1, 8)
    box_weapons = range(8, 31)

    handguns = (0, 3, *range(8, 13))
    submachine_guns = (4, 5, 13)
    assault_rifles = (1, 6, *range(14, 20))
    shotguns = (2, 7, 20, 21)
    sniper_rifles = (22, 23)
    light_machine_guns = (24, 25)
    special_weapons = 26
    heavy_weapons = (27, 28)
    wonder_weapons = (29, 30)

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
