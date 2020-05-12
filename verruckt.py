def weapons():
    map_weapons = {
        0: "M1911",
        1: "RK5",
        2: "L-CAR 9",
        3: "Bootlegger",
        4: "MP40",
        5: "Kuda",
        6: "Vesper",
        7: "KRM-262",
        8: "Sheiva",
        9: "STG-44",
        10: "ICR-1",
        11: "HVK-30",
        12: "KN-44",
        13: "M8A7",
        14: "MX Garand",
        15: "Man-O-War",
        16: "VMP",
        17: "Weevil",
        18: "Pharo",
        19: "AK-74u",
        20: "PPSh-41",
        21: "205 Brecci",
        22: "Haymaker 12",
        23: "Dingo",
        24: "BRM",
        25: "48 Dredge",
        26: "Gorgon",
        27: "RPK",
        28: "Locus",
        29: "Drakon",
        30: "SVG-100",
        31: "XM-53",
        32: "Ray Gun",
        33: "Ray Gun Mark II",
        34: "Wunderwaffe DG-2"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 35)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 12)
    box_weapons = range(2, 35)

    handguns = (0, 1, 2)
    submachine_guns = (*range(3, 7), *range(16, 21))
    assault_rifles = range(8, 16)
    shotguns = (7, 21, 22)
    sniper_rifles = (28, 29, 30)
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

    german_side_perks = (1, 5)
    american_side_perks = (2, 3, 4)
    downstairs_perks = (1, 2, 4)
    upstairs_perks = (3, 5)
    on_map_perks = range(1, 6)
    wunderfizz_only_perks = (6, 7, 8)

    speed_related_perks = (2, 3, 5, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 5, 7)

    categories = {
        0: all_perks,
        1: german_side_perks,
        2: american_side_perks,
        3: downstairs_perks,
        4: upstairs_perks,
        5: on_map_perks,
        6: wunderfizz_only_perks,
        7: speed_related_perks,
        8: health_related_perks,
        9: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Location:
    1 = German side ({len(german_side_perks)})
    2 = American side ({len(american_side_perks)})
    3 = Downstairs ({len(downstairs_perks)})
    4 = Upstairs ({len(upstairs_perks)})
    5 = On map perks ({len(on_map_perks)})
    6 = Wunderfizz only perks ({len(wunderfizz_only_perks)})

    Function:
    7 = Speed ({len(speed_related_perks)})
    8 = Health ({len(health_related_perks)})
    9 = Weapon ({len(weapon_related_perks)})
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 13
    perk = 10

    return eval(category)