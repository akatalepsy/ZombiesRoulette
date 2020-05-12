def weapons():
    map_weapons = {
        0: "Bloodhound",
        1: "RK5",
        2: "Sheiva",
        3: "L-CAR 9",
        4: "KRM-262",
        5: "Kuda",
        6: "Vesper",
        7: "VMP",
        8: "M8A7",
        9: "KN-44",
        10: "HVK-30",
        11: "Bootlegger",
        12: "Weevil",
        13: "Pharo",
        14: "Man-O-War",
        15: "ICR-1",
        16: "205 Brecci",
        17: "Argus",
        18: "Haymaker 12",
        19: "Dingo",
        20: "BRM",
        21: "48 Dredge",
        22: "Gorgon",
        23: "Locus",
        24: "Drakon",
        25: "SVG-100",
        26: "XM-53",
        27: "Ray Gun",
        28: "Apothicon Servant"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 29)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 12)
    box_weapons = range(10, 30)

    handguns = (0, 1, 3)
    submachine_guns = (5, 6, 7, 11, 12, 13)
    assault_rifles = (2, 8, 9, 10, 14, 15)
    shotguns = (4, 16, 17, 18)
    sniper_rifles = (23, 24, 25)
    light_machine_guns = range(19, 23)
    heavy_weapons = 26
    wonder_weapons = (27, 28)

    explosive_weapons = (26, 27)
    pod_weapons = (0, 1, 3, 4, 11, 14, 18, 23, 27)

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
        13: pod_weapons
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
    13 = Pod weapons ({len(pod_weapons)})
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
        7: "Widow's Wine"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 8)

    ritual_area_perks = range(1, 5)
    center_area_perks = (5, 6, 7)

    speed_related_perks = range(2, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 6)

    categories = {
        0: all_perks,
        1: ritual_area_perks,
        2: center_area_perks,
        3: speed_related_perks,
        4: health_related_perks,
        5: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})
    
    Location:
    1 = Ritual areas ({len(ritual_area_perks)})
    2 = Center area ({len(center_area_perks)})
    
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
    weapon = 14
    perk = 6

    return eval(category)
