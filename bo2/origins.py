def weapons():
    map_weapons = {
        0: "Mauser C96",
        1: "M14",
        2: "Ballista",
        3: "Five-Seven",
        4: "B23R",
        5: "AK74u",
        6: "MP40",
        7: "STG-44",
        8: "Remington 870 MCS",
        9: "Five-Seven Dual Wield",
        10: "B23R Extended Clip",
        11: "KAP-40",
        12: "Python",
        13: "Chicom CQB",
        14: "AK-74u Extended Clip",
        15: "MP40 Adjustable Stock",
        16: "PDW-57",
        17: "Skorpion EVO",
        18: "M1927",
        19: "FAL",
        20: "Type 25",
        21: "SCAR-H",
        22: "Galil",
        23: "M1216",
        24: "KSG",
        25: "DSR 50",
        26: "HAMR",
        27: "MG08/15",
        28: "War Machine",
        29: "Ray Gun",
        30: "Ray Gun Mark II",
        31: "Staff of Lightning",
        32: "Staff of Fire",
        33: "Staff of Ice",
        34: "Staff of Wind"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 35)

    starting_weapons = 0
    wall_weapons = range(1, 8)
    box_weapons = range(8, 31)

    handguns = (0, 3, 4, *range(9, 13))
    submachine_guns = (5, 6, *range(13, 19))
    assault_rifles = (1, 7, *range(19, 23))
    shotguns = (8, 23, 24)
    sniper_rifles = (2, 25)
    light_machine_guns = (26, 27)
    heavy_weapons = 28
    wonder_weapons = (29, 30)
    staffs = range(31, 35)

    explosive_weapons = (28, 29)
    shovel_weapons = (0, 2, 6, 7, 8, 23, 24, 25)

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
    1 = Starting weapons (1)
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
        7: "PhD Flopper",
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
