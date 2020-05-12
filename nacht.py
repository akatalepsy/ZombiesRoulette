def weapons():
    map_weapons = {
        0: "M1911",
        1: "Scoped Kar98k",
        2: "M1A1 Carbine",
        3: "Kar98k",
        4: "Double-Barreled Shotgun",
        5: "Thompson",
        6: "BAR",
        7: "M1897 Trench Gun",
        8: "Sawed-Off Double-Barreled Shotgun w/Grip",
        9: ".357 Magnum",
        10: "MP40",
        11: "Springfield",
        12: "M1 Garand",
        13: "M1 Garand w/Launcher",
        14: "Gewehr 43",
        15: "STG-44",
        16: "PTRS-41",
        17: "Deployable FG42",
        18: "Deployable Browning M1919",
        19: "Deployable MG42",
        20: "M2 Flamethrower",
        21: "Panzerschreck",
        22: "Ray Gun"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 23)

    starting_weapons = 0
    wall_weapons = range(1, 9)
    box_weapons = range(2, 23)

    handguns = (0, 9)
    submachine_guns = (5, 10)
    assault_rifles = 15
    rifles = (2, 3, *range(11, 15), 17)
    shotguns = (4, 7, 8)
    sniper_rifles = (1, 16)
    light_machine_guns = (6, 18, 19)
    heavy_weapons = (20, 21)
    wonder_weapons = 22

    explosive_weapons = (21, 22)

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
    6 = Assault Rifles (1)
    7 = Rifles ({len(rifles)})
    8 = Shotguns ({len(shotguns)})
    9 = Sniper rifles ({len(sniper_rifles)})
    10 = Light machine guns ({len(light_machine_guns)})
    11 = Heavy weapons ({len(heavy_weapons)})
    12 = Wonder weapons (1)

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