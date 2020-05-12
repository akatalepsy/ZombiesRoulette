def weapons():
    map_weapons = {
        0: "MR6",
        1: "RK5",
        2: "L-CAR 9",
        3: "KRM-262",
        4: "Kuda",
        5: "Vesper",
        6: "VMP",
        7: "Pharo",
        8: "Argus",
        9: "Sheiva",
        10: "KN-44",
        11: "M8A7",
        12: "ICR-1",
        13: "HVK-30",
        14: "SVG-100",
        15: "Locus",
        16: "Drakon",
        17: "MX Garand",
        18: "Man-O-War",
        19: "Marshal 16 Dual Wield",
        20: "205 Brecci",
        21: "Haymaker 12",
        22: "Dingo",
        23: "BRM",
        24: "Gorgon",
        25: "48 Dredge",
        26: "Weevil",
        27: "HG 40",
        28: "Razorback",
        29: "XM-53",
        30: "Ray Gun",
        31: "KT-4"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 32)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 14)
    box_weapons = range(6, 32)

    handguns = (0, 1, 2, 19)
    submachine_guns = (*range(4, 8), 26, 27, 28)
    assault_rifles = (*range(9, 14), 17, 18)
    shotguns = (3, 8, 20, 21)
    sniper_rifles = (14, 15, 16)
    light_machine_guns = (23, 24, 25)
    heavy_weapons = 29
    wonder_weapons = (30, 31)

    explosive_weapons = (29, 30)

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
        4: "Double Tap II",
        5: "Stamin-Up",
        6: "Mule Kick",
        7: "Deadshot Daiquiri",
        8: "Electric Cherry",
        9: "Widow's Wine"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 10)

    on_map_perks = range(1, 7)
    fruit_or_spider_perks = (7, 8, 9)

    speed_related_perks = range(2, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 6, 7, 8)

    categories = {
        0: all_perks,
        1: on_map_perks,
        2: fruit_or_spider_perks,
        3: speed_related_perks,
        4: health_related_perks,
        5: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Location:
    1 = On map perks ({len(on_map_perks)})
    2 = Fruit/Spider only perks ({len(fruit_or_spider_perks)})

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