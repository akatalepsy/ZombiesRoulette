def weapons():
    map_weapons = {
        0: "MR6",
        1: "RK5",
        2: "L-CAR 9",
        3: "KRM-262",
        4: "Kuda",
        5: "Vesper",
        6: "M8A7",
        7: "KN-44",
        8: "Sheiva",
        9: "HVK-30",
        10: "VMP",
        11: "Weevil",
        12: "Pharo",
        13: "Man-O-War",
        14: "ICR-1",
        15: "205 Brecci",
        16: "Argus",
        17: "Haymaker 12",
        18: "Dingo",
        19: "BRM",
        20: "48 Dredge",
        21: "Gorgon",
        22: "RPK",
        23: "Locus",
        24: "Drakon",
        25: "SVG-100",
        26: "XM-53",
        27: "Ray Gun",
        28: "Wunderwaffe DG-2"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 29)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 11)
    box_weapons = range(8, 29)

    handguns = (0, 1, 2)
    submachine_guns = (4, 5, 10, 11, 12)
    assault_rifles = (*range(6, 10), 13, 14)
    shotguns = (3, 15, 16, 17)
    sniper_rifles = (23, 24, 25)
    light_machine_guns = range(18, 23)
    heavy_weapons = 26
    wonder_weapons = (27, 28)

    explosive_weapons = (26, 27)

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
        12: explosive_weapons,
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
        4: "Double Tap II",
        5: "Mule Kick",
        6: "Stamin-Up/Deadshot Daiquiri",
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 7)
    non_secret_perks = range(1, 6)

    speed_related_perks = (2, 3, 4)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 5)

    categories = {
        0: all_perks,
        1: non_secret_perks,
        2: speed_related_perks,
        3: health_related_perks,
        4: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})
    1 = Non secret perks ({len(non_secret_perks)})

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
    weapon = 13
    perk = 5

    return eval(category)
