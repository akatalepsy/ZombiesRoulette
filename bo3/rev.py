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
        9: "M1927",
        10: "Argus",
        11: "Sheiva",
        12: "HVK-30",
        13: "M8A7",
        14: "ICR-1",
        15: "Man-O-War",
        16: "Peacekeeper MK2",
        17: "SVG-100",
        18: "Locus",
        19: "Drakon",
        20: "205 Brecci",
        21: "Haymaker 12",
        22: "Banshii",
        23: "Dingo",
        24: "BRM",
        25: "48 Dredge",
        26: "Gorgon",
        27: "Weevil",
        28: "XM-53",
        29: "Rift E9",
        30: "Ray Gun",
        31: "Thundergun",
        32: "Apothicon Servant"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 33)

    starting_weapons = (0, 1)
    wall_weapons = range(1, 15)
    box_weapons = range(7, 33)
    spawn_nacht_weapons = (1, 2, 6, 11)
    shang_de_weapons = (2, 3, 5, 8, 9, 13)
    kino_verruckt_weapons = (4, 12, 14)
    motd_origins_weapons = range(4, 13, 2)

    handguns = (0, 1, 2, 29)
    submachine_guns = (*range(5, 10), 27)
    assault_rifles = (4, *range(11, 17))
    shotguns = (3, 10, *range(20, 23))
    sniper_rifles = (17, 18, 19)
    light_machine_guns = range(23, 27)
    heavy_weapons = 28
    energy_weapons = (22, 29)
    wonder_weapons = (30, 31, 32)

    explosive_weapons = (28, 30)

    categories = {
        0: all_weapons,
        1: starting_weapons,
        2: wall_weapons,
        3: box_weapons,
        4: spawn_nacht_weapons,
        5: shang_de_weapons,
        6: kino_verruckt_weapons,
        7: motd_origins_weapons,
        8: handguns,
        9: submachine_guns,
        10: assault_rifles,
        11: shotguns,
        12: sniper_rifles,
        13: light_machine_guns,
        14: heavy_weapons,
        15: energy_weapons,
        16: wonder_weapons,
        17: explosive_weapons
    }

    category_list = f'''
    0 = All weapons ({len(all_weapons)})

    Location:
    1 = Starting weapons ({len(starting_weapons)})
    2 = Wall weapons ({len(wall_weapons)})
    3 = Box weapons ({len(box_weapons)})
    4 = Spawn/Nacht ({len(spawn_nacht_weapons)})
    5 = Shangri-La/Der Eisendrache ({len(shang_de_weapons)})
    6 = Kino der Toten/Verrückt ({len(kino_verruckt_weapons)})
    7 = Mob of the Dead/Origins ({len(motd_origins_weapons)})

    Weapon Type:
    8 = Handguns ({len(handguns)})
    9 = Submachine guns ({len(submachine_guns)})
    10 = Assault Rifles ({len(assault_rifles)})
    11 = Shotguns ({len(shotguns)})
    12 = Sniper rifles ({len(sniper_rifles)})
    13 = Light machine guns ({len(light_machine_guns)})
    14 = Heavy weapons (1)
    15 = Energy weapons ({len(energy_weapons)})
    16 = Wonder weapons ({len(wonder_weapons)})

    Other Categories:
    17 = Explosive weapons ({len(explosive_weapons)})
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
        7: "Widow's Wine",
        8: "Deadshot Daiquiri",
        9: "Electric Cherry"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 10)

    on_map_perks = range(1, 8)
    wunderfizz_only_perks = (8, 9)
    spawn_nacht_perks = (1, 2)
    shang_de_perks = 5
    kino_verruckt_perks = (3, 7)
    motd_origins_perks = (4, 6)

    speed_related_perks = range(2, 6)
    health_related_perks = (1, 2)
    weapon_related_perks = (3, 4, 6, 8, 9)

    categories = {
        0: all_perks,
        1: on_map_perks,
        2: wunderfizz_only_perks,
        3: spawn_nacht_perks,
        4: shang_de_perks,
        5: kino_verruckt_perks,
        6: motd_origins_perks,
        7: speed_related_perks,
        8: health_related_perks,
        9: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Location:
    1 = On map perks ({len(on_map_perks)})
    2 = Wunderfizz only perks ({len(wunderfizz_only_perks)})
    3 = Spawn/Nacht ({len(spawn_nacht_perks)})
    4 = Shangri-La/Der Eisendrache (1)
    5 = Kino der Toten/Verrückt ({len(kino_verruckt_perks)})
    6 = Mob of the Dead/Origins ({len(motd_origins_perks)})

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
    weapon = 18
    perk = 10

    return eval(category)
