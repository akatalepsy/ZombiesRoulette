def weapons():
    map_weapons = {
        0: "M1911",
        1: "M14",
        2: "Olympia",
        3: "MP5",
        4: "Remington 870 MCS",
        5: "Five-Seven",
        6: "Five-Seven Dual Wield",
        7: "KAP-40",
        8: "Python",
        9: "Executioner",
        10: "Chicom CQB",
        11: "SMR",
        12: "FAL",
        13: "M8A1",
        14: "Type 25",
        15: "MTAR",
        16: "Galil",
        17: "M1216",
        18: "S12",
        19: "Barrett M82A1",
        20: "DSR 50",
        21: "HAMR",
        22: "RPD",
        23: "Ballistic Knife",
        24: "War Machine",
        25: "RPG",
        26: "Ray Gun",
        27: "Ray Gun Mark II"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 28)

    starting_weapons = 0
    wall_weapons = range(1, 5)
    box_weapons = range(5, 28)

    handguns = (0, *range(5, 10))
    submachine_guns = (3, 10)
    assault_rifles = (1, *range(11, 17))
    shotguns = (2, 4, 17, 18)
    sniper_rifles = (19, 20)
    light_machine_guns = (21, 22)
    special_weapons = 23
    heavy_weapons = (24, 25)
    wonder_weapons = (26, 27)

    explosive_weapons = range(24, 27)

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


def category_range_list(category):
    weapon = 14
    perk = 0

    return eval(category)
