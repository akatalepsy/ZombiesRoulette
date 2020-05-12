def weapons():
    map_weapons = {
        0: "M1911",
        1: "BAR+Bipod",
        2: "Springfield",
        3: "M1 Garand",
        4: "Kar98k",
        5: "Gewehr 43",
        6: "MP40",
        7: "Double-Barreled Shotgun",
        8: "STG-44",
        9: "Thompson",
        10: "M1897 Trench Gun",
        11: ".357 Magnum",
        12: "PPSh-41",
        13: "Sawed-Off Double-Barreled Shotgun w/Grip",
        14: "M1 Garand w/Launcher",
        15: "M1A1 Carbine",
        16: "PTRS-41",
        17: "BAR",
        18: "Deployable FG42",
        19: "Deployable Browning M1919",
        20: "Deployable MG42",
        21: "M2 Flamethrower",
        22: "Panzerschreck",
        23: "Ray Gun"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 24)

    starting_weapons = 0
    wall_weapons = range(1, 11)
    box_weapons = range(2, 24)

    handguns = (0, 11)
    submachine_guns = range(6, 13, 3)
    assault_rifles = 8
    rifles = (*range(2, 6), 14, 15, 18)
    shotguns = range(7, 14, 3)
    sniper_rifles = 16
    light_machine_guns = (1, 17, 19, 20)
    heavy_weapons = (21, 22)
    wonder_weapons = 23

    explosive_weapons = (22, 23)

    categories = {
        0: all_weapons,
        1: starting_weapons,
        2: wall_weapons,
        3: box_weapons,
        4: handguns,
        5: submachine_guns,
        6: assault_rifles,
        7: rifles,
        8: shotguns,
        9: sniper_rifles,
        10: light_machine_guns,
        11: heavy_weapons,
        12: wonder_weapons,
        13: explosive_weapons
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
    6 = Assault Rifles (1)
    7 = Rifles ({len(rifles)})
    8 = Shotguns ({len(shotguns)})
    9 = Sniper rifles (1)
    10 = Light machine guns ({len(light_machine_guns)})
    11 = Heavy weapons ({len(heavy_weapons)})
    12 = Wonder weapons (1)
    
    Other Categories:
    13 = Explosive weapons ({len(explosive_weapons)})
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
        3: "Double Tap Root Beer",
        4: "Speed Cola"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 5)
    solo_perks = (1, 3, 4)

    german_side_perks = (1, 3)
    american_side_perks = (2, 4)
    american_side_perks_solo = 4
    downstairs_perks = (1, 2)
    downstairs_perks_solo = 1
    upstairs_perks = (3, 4)

    speed_related_perks = range(2, 5)
    speed_related_perks_solo = (3, 4)
    health_related_perks = (1, 2)
    health_related_perks_solo = 1
    weapon_related_perks = (3, 4)

    categories = {
        0: all_perks,
        1: solo_perks,
        2: german_side_perks,
        3: american_side_perks,
        4: american_side_perks_solo,
        5: downstairs_perks,
        6: downstairs_perks_solo,
        7: upstairs_perks,
        8: speed_related_perks,
        9: speed_related_perks_solo,
        10: health_related_perks,
        11: health_related_perks_solo,
        12: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})
    1 = Solo perks ({len(solo_perks)})
    
    Location:
    2 = German side ({len(german_side_perks)})
    3 = American side ({len(american_side_perks)})
    4 = American side (solo) (1)
    5 = Downstairs ({len(downstairs_perks)})
    6 = Downstairs (solo) (1)
    7 = Upstairs ({len(upstairs_perks)})
    
    Function:
    8 = Speed ({len(speed_related_perks)})
    9 = Speed (solo) ({len(speed_related_perks_solo)})
    10 = Health ({len(health_related_perks)})
    11 = Health (solo) (1)
    12 = Weapon ({len(weapon_related_perks)})
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 14
    perk = 13

    return eval(category)
