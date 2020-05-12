def weapons():
    map_weapons = {
        0: "MR6",
        1: "RK5",
        2: "L-CAR 9",
        3: "KRM-262",
        4: "KN-44",
        5: "Kuda",
        6: "Vesper",
        7: "Pharo",
        8: "VMP",
        9: "Argus",
        10: "Sheiva",
        11: "ICR-1",
        12: "M8A7",
        13: "HVK-30",
        14: "MX Garand",
        15: "Man-O-War",
        16: "FFAR",
        17: "SVG-100",
        18: "Locus",
        19: "Drakon",
        20: "205 Brecci",
        21: "Haymaker 12",
        22: "Dingo",
        23: "BRM",
        24: "48 Dredge",
        25: "Gorgon",
        26: "RPK",
        27: "Weevil",
        28: "HG 40",
        29: "PPSh-41",
        30: "L4 Siege",
        31: "XM-53",
        32: "NX ShadowClaw Dual Wield",
        33: "Ray Gun",
        34: "GKZ-45 Mk3"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 35)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 14)
    box_weapons = range(7, 35)

    handguns = (0, 1, 2)
    submachine_guns = (*range(5, 9), 27, 28, 29)
    assault_rifles = (4, *range(10, 17))
    shotguns = (3, 9, 20, 21)
    sniper_rifles = (17, 18, 19)
    light_machine_guns = range(22, 27)
    heavy_weapons = (30, 31)
    special_weapons = 32
    wonder_weapons = (33, 34)

    explosive_weapons = (30, 31, 33)

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
        11: special_weapons,
        12: wonder_weapons,
        13: explosive_weapons
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
    10 = Heavy weapons ({len(heavy_weapons)})
    11 = Special weapons (1)
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
    wunderfizz_only_perks = range(7, 10)

    speed_related_perks = range(2, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 6, 7, 8)

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
