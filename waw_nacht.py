def weapons():
    map_weapons = {
        0: 'M1911',
        1: 'M1A1 Carbine',
        2: 'Kar98k',
        3: 'Double-Barreled Shotgun',
        4: 'Thompson',
        5: 'BAR',
        6: 'M1897 Trench Gun',
        7: 'Sawed-Off Double-Barreled Shotgun w/Grip',
        8: 'Scoped Kar98k',
        9: '.357 Magnum',
        10: 'Thompson',
        11: 'MP40',
        12: 'M1897 Trench Gun',
        13: 'Double-Barreled Shotgun',
        14: 'Sawed-Off Double-Barreled Shotgun w/Grip',
        15: 'Kar98k',
        16: 'Springfield',
        17: 'M1 Garand',
        18: 'M1 Garand w/Launcher',
        19: 'Gewehr 43',
        20: 'M1A1 Carbine',
        21: 'STG-44',
        22: 'PTRS-41',
        23: 'BAR',
        24: 'Deployable FG42',
        25: 'Deployable Browning M1919',
        26: 'Deployable MG42',
        27: 'M2 Flamethrower',
        28: 'Panzerschreck',
        29: 'Ray Gun'
    }

    all_weapons = range(0, 30)

    starting_weapons = 0
    wall_weapons = range(1, 9)
    box_weapons = range(9, 30)

    handguns = (0, 9)
    submachine_guns = (4, 10, 11)
    assault_rifles = 21
    rifles = (1, 2, 15, 16, 17, 18, 19, 20, 24)
    shotguns = (3, 6, 7, 12, 13, 14)
    sniper_rifles = (8, 22)
    light_machine_guns = (5, 23, 25, 26)
    heavy_weapons = (27, 28)
    wonder_weapons = 29

