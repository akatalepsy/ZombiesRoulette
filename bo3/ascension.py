def weapons():
    map_weapons = {
        0: "M1911",
        1: "RK5",
        2: "Argus",
        3: "L-CAR 9",
        4: "Kuda",
        5: "Vesper",
        6: "VMP",
        7: "Sheiva",
        8: "KN-44",
        9: "ICR-1",
        10: "HVK-30",
        11: "Man-O-War",
        12: "M8A7",
        13: "Galil",
        14: "FFAR",
        15: "M16",
        16: "Weevil",
        17: "Pharo",
        18: "AK-74u",
        19: "205 Brecci",
        20: "Haymaker 12",
        21: "KRM-262",
        22: "Dingo",
        23: "BRM",
        24: "48 Dredge",
        25: "Gorgon",
        26: "RPK",
        27: "Locus",
        28: "Drakon",
        29: "SVG-100",
        30: "XM-53",
        31: "Ray Gun",
        32: "Ray Gun Mark II",
        33: "Thundergun"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 34)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 11)
    box_weapons = range(3, 34)

    handguns = (0, 1, 3)
    submachine_guns = (*range(4, 7), *range(16, 19))
    assault_rifles = range(7, 16)
    shotguns = (2, 19, 20, 21)
    sniper_rifles = (27, 28, 29)
    light_machine_guns = range(22, 27)
    heavy_weapons = 30
    wonder_weapons = (31, 32, 33)

    explosive_weapons = (30, 31)

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
        4: "Stamin-Up",
        5: "Mule Kick",
        6: "Widow's Wine",
        7: "Double Tap II",
        8: "Deadshot Daiquiri"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 9)

    on_map_perks = range(1, 7)
    wunderfizz_only_perks = (7, 8)
    lander_area_perks = range(3, 7)
    central_area_perks = (1, 2)

    speed_related_perks = (2, 3, 4, 7)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 5, 7, 8)

    categories = {
        0: all_perks,
        1: on_map_perks,
        2: wunderfizz_only_perks,
        3: lander_area_perks,
        4: central_area_perks,
        5: speed_related_perks,
        6: health_related_perks,
        7: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Location:
    1 = On map perks ({len(on_map_perks)})
    2 = Wunderfizz only perks ({len(wunderfizz_only_perks)})
    3 = Lander areas ({len(lander_area_perks)})
    4 = Central area ({len(central_area_perks)})

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
    weapon = 13
    perk = 8

    return eval(category)
