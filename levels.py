from entities.level import Level

walls = [[[500, 80], [510, 80], [520, 80], [500, 90], [510, 90], [520, 90], [500, 100], [510, 100], [520, 100]],
        [],
        [],
        [],
        ]
bombs = [[[500, 20], [510, 20], [520, 20], [500, 30], [510, 30], [520, 30], [500, 40], [510, 40], [520, 40]],
         [],
         [],
         [],
         ]

Levels = [
    Level(10, walls=walls[0], win_point=[[500,500]]),
    Level(2),
    Level(9),
    Level(9)
]
