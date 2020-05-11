def weapons():
    map_weapons = {
        0: "M1911",
        1: "M1A1 Carbine",
        2: "Kar98k",
        3: "Double-Barreled Shotgun",
        4: "Thompson",
        5: "BAR",
        6: "M1897 Trench Gun",
        7: "Sawed-Off Double-Barreled Shotgun w/Grip",
        8: "Scoped Kar98k",
        9: "CZ75",
        10: "CZ75 Dual Wield",
        11: "Python",
        12: "Spectre",
        13: "FN FAL",
        14: "G11",
        15: "Famas",
        16: "AUG",
        17: "Commando",
        18: "Galil",
        19: "HS-10",
        20: "SPAS-12",
        21: "Dragunov",
        22: "L96A1",
        23: "RPK",
        24: "HK21",
        25: "Ballistic Knife",
        26: "Crossbow",
        27: "China Lake",
        28: "M72 LAW",
        29: "Ray Gun",
        30: "Thundergun"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 31)

    starting_weapons = 0
    wall_weapons = range(1, 9)
    box_weapons = range(9, 31)

    handguns = (0, 9, 10, 11)
    submachine_guns = (4, 12)
    assault_rifles = range(13, 19)
    rifles = (1, 2)
    shotguns = (3, 6, 7, 19, 20)
    sniper_rifles = (8, 21, 22)
    light_machine_guns = (5, 23, 24)
    special_weapons = (25, 26)
    heavy_weapons = (27, 28)
    wonder_weapons = (29, 30)

    explosive_weapons = range(26, 30)

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


def category_range_list(category):
    weapon = 15
    perk = 1

    return eval(category)