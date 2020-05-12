def weapons():
    map_weapons = {
        0: "M1911",
        1: "Olympia",
        2: "M14",
        3: "PM63",
        4: "MPL",
        5: "MP5k",
        6: "AK74u",
        7: "MP40",
        8: "M16",
        9: "Stakeout",
        10: "CZ75",
        11: "CZ75 Dual Wield",
        12: "Python",
        13: "Spectre",
        14: "FN FAL",
        15: "G11",
        16: "Famas",
        17: "AUG",
        18: "Commando",
        19: "Galil",
        20: "HS-10",
        21: "SPAS-12",
        22: "Dragunov",
        23: "L96A1",
        24: "RPK",
        25: "HK21",
        26: "Ballistic Knife",
        27: "Crossbow",
        28: "China Lake",
        29: "M72 LAW",
        30: "Ray Gun",
        31: "V-R11",
        32: "Scavenger"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 33)

    starting_weapons = 0
    wall_weapons = range(1, 10)
    box_weapons = range(10, 33)

    handguns = (0, 10, 11, 12)
    submachine_guns = (*range(3, 8), 13)
    assault_rifles = (2, 8, *range(14, 20))
    shotguns = (1, 9, 20, 21)
    sniper_rifles = (22, 23, 32)
    light_machine_guns = (24, 25)
    special_weapons = (26, 27)
    heavy_weapons = (28, 29)
    wonder_weapons = range(30, 32)

    explosive_weapons = (*range(27, 31), 32)

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
    10 = Special weapons ({len(special_weapons)})
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
        3: "Double Tap Root Beer",
        4: "Speed Cola",
        5: "Mule Kick",
        6: "PhD Flopper",
        7: "Stamin-Up",
        8: "Deadshot Daiquiri"

    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 9)

    lighthouse_side_perks = (4, 6, 7, 8)
    ship_side_perks = (1, 2, 3, 5)

    speed_related_perks = (2, 3, 4, 7)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 8)

    categories = {
        0: all_perks,
        1: lighthouse_side_perks,
        2: ship_side_perks,
        3: speed_related_perks,
        4: health_related_perks,
        5: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Location:
    1 = Lighthouse side ({len(lighthouse_side_perks)})
    2 = Ship side ({len(ship_side_perks)})

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
