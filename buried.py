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
        11: "LSAT",
        12: "Five-Seven",
        13: "Five-Seven Dual Wield",
        14: "KAP-40",
        15: "Remington New Model Army",
        16: "Executioner",
        17: "SMR",
        18: "FAL",
        19: "MTAR",
        20: "Galil",
        21: "M1216",
        22: "S12",
        23: "Barrett M82A1",
        24: "DSR 50",
        25: "HAMR",
        26: "Ballistic Knife",
        27: "War Machine",
        28: "RPG",
        29: "Ray Gun",
        30: "Ray Gun Mark II",
        31: "Paralyzer"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 32)

    starting_weapons = 0
    wall_weapons = range(1, 12)
    box_weapons = range(12, 32)

    handguns = (0, 3, *range(12, 17))
    submachine_guns = (4, 5, 6)
    assault_rifles = (1, 7, 8, *range(17, 21))
    shotguns = (2, 9, 21, 22)
    sniper_rifles = (10, 23, 24)
    light_machine_guns = (11, 25)
    special_weapons = 26
    heavy_weapons = (27, 28)
    wonder_weapons = (29, 30, 31)

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
        6: "Mule Kick",
        7: "Vulture Aid"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 8)

    town_perks = (1, 2, 3, 6, 7)
    mansion_and_maze_perks = (4, 5)

    speed_related_perks = range(2, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 6)

    categories = {
        0: all_perks,
        1: town_perks,
        2: mansion_and_maze_perks,
        3: speed_related_perks,
        4: health_related_perks,
        5: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})
    
    Location:
    1 = Town perks ({len(town_perks)})
    2 = Mansion and Maze perks ({len(mansion_and_maze_perks)})
    
    Function:
    3 = Speed ({len(speed_related_perks)})
    4 = Health ({len(health_related_perks)})
    5 = Weapon ({len(weapon_related_perks)})
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