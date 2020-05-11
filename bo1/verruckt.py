def weapons():
    map_weapons = {
        0: "M1911",
        1: "Springfield",
        2: "M1 Garand",
        3: "Kar98k",
        4: "Gewehr 43",
        5: "MP40",
        6: "Double-Barreled Shotgun",
        7: "STG-44",
        8: "Thompson",
        9: "M1897 Trench Gun",
        10: "BAR+Bipod",
        11: "CZ75",
        12: "CZ75 Dual Wield",
        13: "Python",
        14: "Spectre",
        15: "FN FAL",
        16: "G11",
        17: "Famas",
        18: "AUG",
        19: "Commando",
        20: "Galil",
        21: "HS-10",
        22: "SPAS-12",
        23: "Dragunov",
        24: "L96A1",
        25: "RPK",
        26: "HK21",
        27: "Ballistic Knife",
        28: "Crossbow",
        29: "China Lake",
        30: "M72 LAW",
        31: "Ray Gun",
        32: "Winter's Howl"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 33)

    starting_weapons = 0
    wall_weapons = range(1, 11)
    box_weapons = range(11, 33)

    handguns = (0, 11, 12, 13)
    submachine_guns = (5, 8, 14)
    assault_rifles = (7, *range(15, 21))
    rifles = range(1, 5)
    shotguns = (6, 9, 21, 22)
    sniper_rifles = (23, 24)
    light_machine_guns = (10, 25, 26)
    special_weapons = (27, 28)
    heavy_weapons = (29, 30)
    wonder_weapons = (31, 32)

    explosive_weapons = range(28, 32)

    categories = {
        0: all_weapons,
        1: starting_weapons,
        2: wall_weapons,
        3: box_weapons,
        4: handguns,
        5: submachine_guns,
        6: assault_rifles,
        7: rifles,
        8: shotguns,
        9: sniper_rifles,
        10: light_machine_guns,
        11: special_weapons,
        12: heavy_weapons,
        13: wonder_weapons,
        14: explosive_weapons
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
    7 = Rifles ({len(rifles)})
    8 = Shotguns ({len(shotguns)})
    9 = Sniper rifles ({len(sniper_rifles)})
    10 = Light machine guns ({len(light_machine_guns)})
    11 = Special weapons ({len(special_weapons)})
    12 = Heavy weapons ({len(heavy_weapons)})
    13 = Wonder weapons ({len(wonder_weapons)})

    Other Categories:
    14 = Explosive weapons ({len(explosive_weapons)})
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
        5: "Mule Kick"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 6)

    german_side_perks = (1, 3)
    american_side_perks = (2, 4, 5)
    downstairs_perks = (1, 2, 5)
    upstairs_perks = (3, 4)

    speed_related_perks = range(2, 5)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 5)

    categories = {
        0: all_perks,
        1: german_side_perks,
        2: american_side_perks,
        3: downstairs_perks,
        4: upstairs_perks,
        5: speed_related_perks,
        6: health_related_perks,
        7: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Location:
    1 = German side ({len(german_side_perks)})
    2 = American side ({len(american_side_perks)})
    3 = Downstairs ({len(downstairs_perks)})
    4 = Upstairs ({len(upstairs_perks)})

    Function:
    5 = Speed ({len(speed_related_perks)})
    6 = Health ({len(health_related_perks)})
    7 = Weapon ({len(weapon_related_perks)})
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 15
    perk = 8

    return eval(category)
