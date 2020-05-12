def weapons():
    map_weapons = {
        0: "M1911",
        1: "RK5",
        2: "L-CAR 9",
        3: "Argus",
        4: "Pharo",
        5: "Kuda",
        6: "VMP",
        7: "Sheiva",
        8: "KN-44",
        9: "Man-O-War",
        10: "HVK-30",
        11: "ICR-1",
        12: "FFAR",
        13: "Galil",
        14: "M16",
        15: "Vesper",
        16: "AK-74u",
        17: "Weevil",
        18: "KRM-262",
        19: "205 Brecci",
        20: "Haymaker 12",
        21: "Dingo",
        22: "BRM",
        23: "48 Dredge",
        24: "Gorgon",
        25: "RPK",
        26: "Locus",
        27: "Drakon",
        28: "SVG-100",
        29: "L4 Siege",
        30: "XM-53",
        31: "Ray Gun",
        32: "Ray Gun Mark II",
        33: "Wave Gun"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 34)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 9)
    box_weapons = range(2, 34)

    handguns = (0, 1, 2)
    submachine_guns = (*range(4, 7), *range(15, 18))
    assault_rifles = range(7, 15)
    shotguns = (3, 18, 19, 20)
    sniper_rifles = (26, 27, 28)
    light_machine_guns = range(21, 26)
    heavy_weapons = (29, 30)
    wonder_weapons = (31, 32, 33)

    explosive_weapons = (29, 30, 31)

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
    10 = Heavy weapons ({len(heavy_weapons)})
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
        5: "Deadshot Daiquiri",
        6: "Mule Kick",
        7: "Double Tap II",
        8: "Widow's Wine"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 9)

    area_51_perks = (1, 3)
    rec_and_tunnel_perks = (2, 4)
    lab_perks = (5, 7)
    bio_dome_perks = (6, 8)

    speed_related_perks = (2, 3, 4, 7)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 5, 6, 7)

    categories = {
        0: all_perks,
        1: area_51_perks,
        2: rec_and_tunnel_perks,
        3: lab_perks,
        4: bio_dome_perks,
        5: speed_related_perks,
        6: health_related_perks,
        7: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Location:
    1 = Area 51 ({len(area_51_perks)})
    2 = Receiving Bay and Tunnels ({len(rec_and_tunnel_perks)})
    3 = Laboratories ({len(lab_perks)})
    4 = Bio Dome area ({len(bio_dome_perks)})

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
