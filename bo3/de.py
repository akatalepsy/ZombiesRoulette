def weapons():
    map_weapons = {
        0: "MR6",
        1: "RK5",
        2: "L-CAR 9",
        3: "KRM-262",
        4: "M8A7",
        5: "Kuda",
        6: "Vesper",
        7: "KN-44",
        8: "Sheiva",
        9: "HVK-30",
        10: "VMP",
        11: "BRM",
        12: "SVG-100",
        13: "Locus",
        14: "Drakon",
        15: "Dingo",
        16: "48 Dredge",
        17: "Gorgon",
        18: "RPK",
        19: "Argus",
        20: "205 Brecci",
        21: "Haymaker 12",
        22: "Man-O-War",
        23: "ICR-1",
        24: "Pharo",
        25: "Weevil",
        26: "XM-53",
        27: "Ray Gun",
        28: "Wrath of the Ancients",
        29: "Kreema'ahm la Ahmahm (Storm)",
        30: "Kreegakaleet lu Gosata'ahm (Void)",
        31: "Kreeaho'ahm nal Ahmhogaroc (Fire)",
        32: "Kreeholo lu Kreemasaleet (Wolf)"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 33)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 12)
    box_weapons = range(8, 28)

    handguns = (0, 1, 2)
    submachine_guns = (5, 6, 10, 24, 25)
    assault_rifles = (4, 7, 8, 9, 22, 23)
    shotguns = (3, 19, 20, 21)
    sniper_rifles = (12, 13, 14)
    light_machine_guns = (11, *range(15, 19))
    heavy_weapons = 26
    wonder_weapons = (27, 28)
    all_bows = range(28, 33)
    upgraded_bows = range(29, 33)

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
        12: all_bows,
        13: upgraded_bows,
        14: explosive_weapons
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
    12 = All Bows ({len(all_bows)})
    13 = Upgraded Bows ({len(upgraded_bows)})

    Other Categories:
    14 = Explosive weapons ({len(explosive_weapons)})
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
    weapon = 15
    perk = 6

    return eval(category)
