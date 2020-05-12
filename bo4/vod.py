def weapons():
    map_weapons = {
        0: "Welling",
        1: "Strife",
        2: "RK7 Garrison",
        3: "Essex Model 07",
        4: "MOG 12",
        5: "Saug 9mm",
        6: "Escargot",
        7: "Spitfire",
        8: "MX9",
        9: "GKS",
        10: "M1897 Trebuchet",
        11: "Swordfish",
        12: "Auger DMR",
        13: "Titan",
        14: "Koshka",
        15: "Maddox RFB",
        16: "KN-57",
        17: "ICR-7",
        18: "Vapr-XKG",
        19: "Hitchcock M9",
        20: "Rampart 17",
        21: "Grav",
        22: "Swat RFT",
        23: "Peacekeeper",
        24: "AN-94",
        25: "Echohawk Dual Bore",
        26: "M16",
        27: "Cordite",
        28: "MP-40",
        29: "Daemon 3XB",
        30: "Switchblade X9",
        31: "VMP",
        32: "MicroMG 9mm",
        33: "ABR 223",
        34: "S6 Stingray",
        35: "Hades",
        36: "VKM 750",
        37: "Zweihänder",
        38: "Tigershark",
        39: "SDM",
        40: "Paladin HB50",
        41: "Outlaw",
        42: "Vendetta",
        43: "Locus",
        44: "Havelina AA50",
        45: "Mozu",
        46: "KAP 45",
        47: "SG12",
        48: "Rampage",
        49: "Argus",
        50: "Hellion Salvo",
        51: "Ballistic Knife",
        52: "Reaver C86",
        53: "Kraken",
        54: "Grip of Akkorokamui",
        55: "Breath of Leviathan",
        56: "Inkanyamba's Roar",
        57: "Jörmungandr's Fang"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = range(0, 54)

    starting_weapons = range(0, 6)
    wall_weapons = range(1, 19)
    box_weapons = range(2, 54)

    handguns = (0, 1, 2, 45, 46)
    submachine_guns = (*range(5, 10), *range(26, 32))
    assault_rifles = range(15, 27)
    shotguns = (4, 10, 47, 48, 49)
    tactical_rifles = (3, 11, 12, 33, 34)
    sniper_rifles = range(39, 45)
    light_machine_guns = (13, *range(35, 39))
    special_weapons = (51, 52)
    heavy_weapons = 50
    krakens = range(53, 58)
    upgraded_krakens = range(54, 58)

    explosive_weapons = 50

    categories = {
        0: all_weapons,
        1: starting_weapons,
        2: wall_weapons,
        3: box_weapons,
        4: handguns,
        5: submachine_guns,
        6: assault_rifles,
        7: shotguns,
        8: tactical_rifles,
        9: sniper_rifles,
        10: light_machine_guns,
        11: special_weapons,
        12: heavy_weapons,
        13: krakens,
        14: upgraded_krakens,
        15: explosive_weapons,
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
        8 = Tactical Rifles ({len(tactical_rifles)})
        9 = Sniper rifles ({len(sniper_rifles)})
        10 = Light machine guns ({len(light_machine_guns)})
        11 = Special weapons ({len(special_weapons)})
        12 = Heavy weapons (1)
        13 = Krakens ({len(krakens)})
        14 = Upgraded Krakens ({len(upgraded_krakens)})

        Other Categories:
        15 = Explosive weapons (1)
        '''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def perks():
    map_perks = {
        1: "Timeslip",
        2: "Quick Revive",
        3: "Death Perception",
        4: "Stamin-Up",
        5: "Electric Burst",
        6: "Dying Wish",
        7: "Stone Cold Stronghold",
        8: "Victorious Tortoise",
        9: "Deadshot Dealer",
        10: "Bandolier Bandit",
        11: "Winter's Wail",
        12: "Mule Kick",
        13: "PhD Slider",
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 17)

    speed_related_perks = (1, 2, 4)
    health_related_perks = 2
    weapon_related_perks = (5, 9, 10, 12)
    offensive_perks = (5, 9, 13)
    defensive_perks = (5, 6, 7, 8, 11)

    categories = {
        0: all_perks,
        1: speed_related_perks,
        2: health_related_perks,
        3: weapon_related_perks,
        4: offensive_perks,
        5: defensive_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})

    Function:
    1 = Speed ({len(speed_related_perks)})
    2 = Health (1)
    3 = Weapon ({len(weapon_related_perks)})
    4 = Offense ({len(offensive_perks)})
    5 = Defense ({len(defensive_perks)})
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 16
    perk = 6

    return eval(category)