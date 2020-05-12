def weapons():
    map_weapons = {
        0: "M1911",
        1: "RK5",
        2: "Argus",
        3: "L-CAR 9",
        4: "KRM-262",
        5: "Pharo",
        6: "Kuda",
        7: "Vesper",
        8: "VMP",
        9: "Sheiva",
        10: "KN-44",
        11: "ICR-1",
        12: "HVK-30",
        13: "M8A7",
        14: "Man-O-War",
        15: "MX Garand",
        16: "StG-44",
        17: "MP40",
        18: "Weevil",
        19: "Bootlegger",
        20: "AK-74u",
        21: "PPSh-41",
        22: "205 Brecci",
        23: "Haymaker 12",
        24: "Dingo",
        25: "BRM",
        26: "48 Dredge",
        27: "Gorgon",
        28: "RPK",
        29: "Locus",
        30: "Drakon",
        31: "SVG-100",
        32: "XM-53",
        33: "Ray Gun",
        34: "Ray Gun Mark II",
        35: "Wunderwaffe DG-2"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 36)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 14)
    box_weapons = range(3, 36)

    handguns = (0, 1, 3)
    submachine_guns = (*range(5, 9), *range(17, 22))
    assault_rifles = range(9, 17)
    shotguns = (2, 4, 22, 23)
    sniper_rifles = (29, 30, 31)
    light_machine_guns = range(24, 29)
    heavy_weapons = 32
    wonder_weapons = (33, 34, 35)

    explosive_weapons = (32, 33)

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
    10 = Heavy weapons (1)
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
        4: "Mule Kick",
        5: "Double Tap II",
        6: "Stamin-Up",
        7: "Deadshot Daiquiri",
        8: "Widow's Wine"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 9)

    on_map_perks = range(1, 6)
    wunderfizz_only_perks = (6, 7, 8)

    speed_related_perks = (2, 3, 5, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 5, 7)

    categories = {
        0: all_perks,
        1: on_map_perks,
        2: wunderfizz_only_perks,
        3: speed_related_perks,
        4: health_related_perks,
        5: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})
    
    Location:
    1 = On map perks ({len(on_map_perks)})
    2 = Wunderfizz only perks ({len(wunderfizz_only_perks)})

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
    weapon = 13
    perk = 6

    return eval(category)