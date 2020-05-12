def weapons():
    map_weapons = {
        0: "M1911",
        1: "RK5",
        2: "Argus",
        3: "Locus",
        4: "KRM-262",
        5: "Sheiva",
        6: "KN-44",
        7: "Kuda",
        8: "Pharo",
        9: "VMP",
        10: "Weevil",
        11: "Vesper",
        12: "Bootlegger",
        13: "AK-74u",
        14: "MP40",
        15: "Man-O-War",
        16: "HVK-30",
        17: "ICR-1",
        18: "M8A7",
        19: "MX Garand",
        20: "StG-44",
        21: "205 Brecci",
        22: "Haymaker 12",
        23: "Dingo",
        24: "BRM",
        25: "48 Dredge",
        26: "Gorgon",
        27: "RPK",
        28: "Drakon",
        29: "SVG-100",
        30: "L-CAR 9",
        31: "XM-53",
        32: "Ray Gun",
        33: "Ray Gun Mark II",
        34: "Thundergun"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 35)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 9)
    box_weapons = range(3, 35)

    handguns = (0, 1, 30)
    submachine_guns = range(7, 15)
    assault_rifles = (5, 6, *range(15, 21))
    shotguns = (2, 4, 21, 22)
    sniper_rifles = (3, 28, 29)
    light_machine_guns = range(23, 28)
    heavy_weapons = 31
    wonder_weapons = (32, 33, 34)

    explosive_weapons = (31, 32)

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
        1: "Mule Kick",
        2: "Jugger-Nog",
        3: "Quick Revive",
        4: "Speed Cola",
        5: "Double Tap II",
        6: "Stamin-Up",
        7: "Deadshot Daiquiri",
        8: "Widow's Wine"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 9)

    on_map_perks = 1
    wunderfizz_only_perks = range(2, 9)

    speed_related_perks = range(3, 7)
    health_related_perks = (2, 3)
    weapon_related_perks = (1, 4, 5, 7)

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
    1 = On map perks (1)
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