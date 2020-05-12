def weapons():
    map_weapons = {
        0: "Mauser C96",
        1: "RK5",
        2: "Argus",
        3: "L-CAR 9",
        4: "Pharo",
        5: "Kuda",
        6: "Vesper",
        7: "VMP",
        8: "MP40",
        9: "M1927",
        10: "Sheiva",
        11: "KN-44",
        12: "ICR-1",
        13: "HVK-30",
        14: "M8A7",
        15: "StG-44",
        16: "Man-O-War",
        17: "Weevil",
        18: "AK-74u",
        19: "205 Brecci",
        20: "Haymaker 12",
        21: "KRM-262",
        22: "Dingo",
        23: "BRM",
        24: "48 Dredge",
        25: "Gorgon",
        26: "RPK",
        27: "MG-08/15",
        28: "Locus",
        29: "Drakon",
        30: "SVG-100",
        31: "XM-53",
        32: "Ray Gun",
        33: "Ray Gun Mark II",
        34: "Staff of Lightning",
        35: "Staff of Fire",
        36: "Staff of Ice",
        37: "Staff of Wind"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 38)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 16)
    box_weapons = range(3, 34)

    handguns = (0, 1, 3)
    submachine_guns = (*range(4, 10), 17, 18)
    assault_rifles = range(10, 17)
    shotguns = (2, 19, 20, 21)
    sniper_rifles = (28, 29, 30)
    light_machine_guns = range(22, 28)
    heavy_weapons = 31
    wonder_weapons = (32, 33)
    staffs = range(34, 38)

    explosive_weapons = (31, 32)
    shovel_weapons = (0, 8, 10, 15, 20, 21, 29, 32)

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
        12: staffs,
        13: explosive_weapons,
        14: shovel_weapons
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
        12 = Staffs ({len(staffs)})

        Other Categories:
        13 = Explosive weapons ({len(explosive_weapons)})
        14 = Shovel weapons ({len(shovel_weapons)})
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
        6: "Double Tap II",
        7: "Widow's Wine",
        8: "Deadshot Daiquiri",
        9: "Electric Cherry"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 10)

    generator_area_perks = range(1, 5)
    spawn_area_perks = (2, 3)
    center_area_perks = (1, 4, 5)
    on_map_perks = range(1, 6)
    wunderfizz_only_perks = range(6, 10)

    speed_related_perks = (2, 3, 4, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 5, 6, 8, 9)
    offensive_perks = (7, 9)

    categories = {
        0: all_perks,
        1: generator_area_perks,
        2: spawn_area_perks,
        3: center_area_perks,
        4: on_map_perks,
        5: wunderfizz_only_perks,
        6: speed_related_perks,
        7: health_related_perks,
        8: weapon_related_perks,
        9: offensive_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Location:
    1 = Generator areas ({len(generator_area_perks)})
    2 = Spawn area ({len(spawn_area_perks)})
    3 = Center area ({len(center_area_perks)})
    4 = On map perks ({len(on_map_perks)})
    5 = Wunderfizz/challenge only perks ({len(wunderfizz_only_perks)})

    Function:
    6 = Speed ({len(speed_related_perks)})
    7 = Health ({len(health_related_perks)})
    8 = Weapon ({len(weapon_related_perks)})
    9 = Offense ({len(offensive_perks)})
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 15
    perk = 10

    return eval(category)