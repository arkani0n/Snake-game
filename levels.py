import classes

wall = [[[500, 80], [510, 80], [520, 80], [500, 90], [510, 90], [520, 90], [500, 100], [510, 100], [520, 100]],
        [],
        [],
        [],
        ]
bombs = [[[500, 20], [510, 20], [520, 20], [500, 30], [510, 30], [520, 30], [500, 40], [510, 40], [520, 40]],
         [],
         [],
         [],
         ]
Level_1 = classes.Level(10, walls=wall[0], win_point=[[500,500]])
Level_2 = classes.Level(0)
Level_3 = classes.Level(9)
Level_4 = classes.Level(9)
Levels = [Level_1, Level_2, Level_3, Level_4]
