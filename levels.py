from entities.level import Level

walls = [[[500, 80], [510, 80], [520, 80], [500, 90], [510, 90], [520, 90], [500, 100], [510, 100], [520, 100]],
         [[220, 0], [220, 10], [220, 20], [220, 30], [220, 40], [220, 50], [220, 60], [220, 70], [220, 80], [220, 90], [220, 100], [220, 110], [220, 120], [220, 130], [220, 140], [220, 150], [220, 160], [220, 170], [220, 180], [220, 190], [220, 200], [220, 210], [220, 220], [220, 230], [220, 240], [220, 250], [220, 260], [220, 290], [220, 300], [220, 310], [220, 320], [220, 330], [220, 340], [220, 350], [220, 360], [220, 370], [220, 380], [220, 390], [220, 400], [220, 420], [220, 430], [230, 430], [240, 430], [250, 430], [260, 430], [270, 430], [280, 430], [290, 430], [300, 430], [310, 430], [320, 430], [330, 430], [340, 430], [350, 430], [360, 430], [370, 430], [380, 430], [390, 430], [400, 430], [410, 430], [420, 430], [430, 430], [440, 430], [450, 430], [460, 430], [470, 430], [480, 430], [490, 430], [500, 430], [510, 430], [520, 430], [530, 430], [540, 430], [550, 430], [560, 430], [570, 430], [580, 430], [590, 430], [230, 400], [240, 400], [250, 400], [250, 410], [260, 410], [270, 410], [280, 410], [290, 410], [320, 420], [290, 400], [300, 400], [310, 400], [320, 400], [330, 400], [340, 400], [340, 410], [350, 410], [360, 410], [370, 410], [380, 410], [390, 410], [420, 420], [420, 410], [390, 400], [390, 390], [400, 390], [410, 390], [420, 390], [430, 390], [440, 390], [440, 400], [460, 420], [460, 410], [460, 400], [460, 390], [440, 380], [440, 370], [440, 360], [450, 360], [460, 360], [470, 360], [480, 360], [480, 370], [480, 380], [480, 390], [480, 400], [490, 400], [500, 400], [500, 390], [500, 380], [500, 370], [500, 360], [510, 360], [520, 360], [530, 360], [540, 360], [550, 360], [590, 360], [230, 290], [240, 290], [250, 290], [260, 290], [260, 280], [260, 270], [260, 260], [260, 250], [260, 240], [260, 230], [260, 220], [260, 210], [260, 200], [260, 190], [260, 180], [260, 170], [260, 160], [260, 150], [260, 140], [260, 130], [230, 100], [240, 100], [250, 100], [260, 100], [270, 100], [280, 100], [270, 130], [280, 130], [290, 130], [300, 130], [310, 130], [310, 120], [310, 110], [310, 100], [310, 90], [310, 80], [310, 70], [310, 60], [300, 60], [290, 60], [280, 60], [270, 70], [240, 20], [230, 20], [250, 20], [260, 20], [270, 20], [280, 20], [290, 20], [300, 20], [310, 20], [320, 20], [320, 60], [330, 60], [340, 60], [350, 60], [360, 60], [330, 20], [340, 20], [350, 20], [360, 20], [370, 20], [370, 60], [380, 60], [390, 60], [400, 60], [400, 50], [400, 40], [400, 30], [370, 10], [370, 0], [380, 0], [390, 0], [400, 0], [410, 0], [410, 30], [420, 30], [420, 0], [430, 0], [440, 0], [450, 0], [430, 30], [440, 30], [450, 30], [460, 30], [470, 30], [480, 30], [460, 0], [470, 0], [480, 0], [490, 0], [500, 0], [490, 30], [500, 30], [510, 0], [520, 0], [530, 0], [540, 0], [540, 10], [540, 20], [540, 30], [500, 40], [500, 50], [500, 60], [500, 70], [540, 40], [540, 50], [540, 60], [540, 70], [540, 80], [540, 90], [540, 100], [500, 80], [500, 90], [500, 100], [500, 110], [500, 120], [500, 130], [500, 140], [500, 150], [500, 160], [540, 110], [540, 120], [540, 130], [540, 140], [540, 150], [590, 350], [590, 340], [590, 330], [590, 320], [590, 310], [580, 310], [570, 310], [540, 160], [500, 180], [500, 170], [500, 190], [500, 200], [510, 200], [520, 200], [530, 200], [540, 200], [540, 170], [550, 170], [560, 170], [570, 170], [570, 180], [570, 190], [570, 200], [570, 210], [570, 220], [570, 230], [570, 240], [570, 250], [570, 260], [570, 270], [570, 280], [570, 290], [570, 300], [540, 210], [540, 220], [540, 230], [540, 240], [540, 250], [540, 260], [540, 270], [540, 280], [540, 290], [540, 300], [540, 310], [540, 320], [550, 350], [550, 340], [550, 330], [540, 330],[590,370],[590,380],[590,390],[590,400],[590,410],[590,420] ],
         [[160, 120], [150, 120], [140, 120], [130, 120], [120, 120], [110, 120], [100, 120], [90, 120], [80, 120], [70, 120], [60, 120], [50, 120], [40, 120], [30, 120], [20, 120], [10, 120], [0, 120], [210, 110], [210, 100], [210, 90], [210, 80], [210, 70], [210, 60], [210, 50], [210, 40], [210, 30], [210, 20], [210, 10], [210, 0], [160, 160], [160, 170], [160, 180], [160, 190], [160, 200], [160, 210], [160, 220], [160, 230], [160, 240], [160, 250], [160, 260], [160, 270], [160, 280], [160, 290], [160, 300], [160, 310], [160, 320], [160, 330], [160, 340], [160, 350], [160, 360], [160, 370], [160, 380], [200, 390], [200, 410], [200, 400], [200, 420], [200, 430], [200, 440], [200, 450], [200, 460], [200, 480], [200, 470], [200, 490], [200, 500], [200, 510], [200, 520], [200, 530], [200, 540], [200, 550], [200, 560], [200, 570], [200, 580], [200, 590], [250, 390], [260, 390], [270, 390], [280, 390], [290, 390], [300, 390], [310, 390], [320, 390], [330, 390], [350, 390], [340, 390], [360, 390], [380, 390], [370, 390], [390, 390], [400, 390], [410, 390], [420, 390], [460, 380], [470, 380], [480, 380], [490, 380], [500, 380], [520, 380], [510, 380], [530, 380], [540, 380], [550, 380], [560, 380], [570, 380], [580, 380], [590, 380], [460, 340], [460, 330], [460, 320], [460, 310], [460, 300], [460, 290], [460, 280], [460, 270], [460, 260], [460, 250], [460, 240], [460, 230], [460, 220], [460, 210], [460, 200], [460, 190], [460, 180], [460, 170], [460, 160], [460, 150], [460, 140], [460, 130], [460, 120], [460, 110], [450, 110], [440, 110], [430, 110], [420, 110], [400, 110], [410, 110], [390, 110], [380, 110], [360, 110], [370, 110], [350, 110], [340, 110], [330, 110], [320, 110], [310, 110], [300, 110], [290, 110], [280, 110], [270, 110], [260, 110]],
         []
         ]
bombs = [[[500, 20], [510, 20], [520, 20], [500, 30], [510, 30], [520, 30], [500, 40], [510, 40], [520, 40]],
         [[250, 240], [230, 200], [250, 150], [270, 110], [240, 90], [240, 80], [240, 70], [250, 30], [260, 30], [360, 50], [530, 20], [530, 10], [510, 80], [530, 120], [510, 160], [550, 250], [560, 250], [550, 370], [560, 370], [570, 370], [580, 370]],
         [[210, 150], [210, 160], [210, 170], [210, 180], [210, 190], [210, 200], [210, 210], [210, 220], [210, 230], [210, 240], [210, 250], [210, 260], [210, 270], [210, 280], [210, 290], [210, 300], [210, 310], [210, 320], [210, 330], [210, 340], [210, 350], [210, 360], [210, 370], [210, 380], [220, 380], [230, 380], [240, 380], [250, 380], [260, 380], [270, 380], [280, 380], [290, 380], [300, 380], [310, 380], [320, 380], [330, 380], [340, 380], [350, 380], [360, 380], [370, 380], [380, 380], [390, 380], [400, 380], [410, 380], [420, 380], [430, 380], [440, 380], [450, 380], [200, 380], [190, 380], [180, 380], [170, 380], [300, 260], [290, 260], [280, 260], [270, 260], [260, 260], [250, 260], [240, 260], [230, 260], [220, 260], [200, 260], [190, 260], [180, 260], [170, 260], [320, 260], [330, 260], [340, 260], [350, 260], [360, 260], [370, 260], [380, 260], [390, 260], [400, 260], [410, 260], [420, 260], [430, 260], [440, 260], [450, 260], [450, 270], [450, 280], [450, 290], [450, 300], [450, 310], [450, 330], [450, 340], [450, 320], [450, 360], [450, 370], [450, 350], [450, 250], [450, 240], [450, 230], [450, 220], [450, 210], [450, 200], [450, 190], [450, 180], [450, 170], [450, 160], [450, 150], [450, 140], [450, 130], [450, 120], [440, 120], [430, 120], [420, 120], [410, 120], [400, 120], [390, 120], [380, 120], [370, 120], [360, 130], [360, 120], [350, 130], [350, 120], [340, 120], [340, 130], [330, 130], [330, 120], [320, 130], [320, 120], [310, 130], [310, 120], [300, 130], [300, 120], [290, 130], [290, 120], [280, 120], [280, 130], [270, 130], [270, 120], [260, 120], [260, 130], [250, 130], [250, 120], [240, 120], [240, 130], [230, 130], [230, 120], [220, 130], [210, 120], [210, 130], [210, 140], [220, 120], [220, 140], [230, 150], [220, 160], [220, 150], [220, 170], [220, 180], [220, 200], [220, 190], [240, 180], [290, 190], [300, 190], [310, 200], [340, 210], [350, 210], [360, 210], [250, 320], [320, 310], [320, 320], [330, 320], [340, 320], [350, 320], [360, 320], [380, 320], [390, 340], [310, 350], [300, 350], [290, 360], [280, 360], [240, 360], [230, 370], [230, 360], [220, 370], [220, 360], [220, 350], [230, 350], [230, 340], [220, 340], [220, 330], [230, 330], [230, 320], [230, 310], [220, 320], [220, 310], [220, 300], [220, 290], [220, 280], [220, 270], [230, 300], [230, 290], [230, 270], [230, 280], [240, 280], [250, 280], [190, 360], [170, 370], [170, 360], [170, 350], [170, 340], [170, 330], [170, 320], [170, 310], [170, 300], [170, 290], [170, 280], [170, 270], [170, 250], [170, 240], [170, 230], [170, 220], [170, 210], [170, 200], [170, 190], [170, 180], [170, 170], [170, 160], [170, 150], [170, 140], [170, 130], [170, 120], [180, 120], [190, 120], [200, 120], [180, 130], [190, 130], [200, 130], [190, 140], [180, 150], [180, 140], [180, 160], [180, 170], [180, 180], [190, 190], [180, 200], [180, 190], [190, 210], [180, 210], [180, 220], [180, 230], [180, 240], [180, 250], [180, 280], [180, 270], [190, 270], [200, 280], [190, 280], [200, 270], [180, 290], [190, 290], [200, 290], [190, 300], [180, 300], [200, 300], [200, 310], [180, 310], [190, 320], [190, 310], [180, 320], [200, 320], [180, 350], [180, 370], [180, 360], [190, 370], [200, 370], [200, 360], [200, 350], [190, 350], [180, 340], [180, 330], [190, 340], [200, 340], [200, 330], [190, 330], [190, 250], [200, 250], [190, 240], [200, 240], [190, 230], [200, 230], [190, 220], [200, 220], [200, 210], [190, 200], [200, 200], [200, 190], [200, 180], [200, 170], [200, 150], [200, 140], [190, 160], [190, 170], [190, 180], [200, 160], [190, 150], [250, 140], [230, 140], [240, 140], [260, 140], [270, 140], [280, 140], [310, 140], [290, 140], [300, 140], [320, 140], [340, 140], [330, 140], [370, 140], [380, 130], [370, 130], [390, 130], [410, 130], [400, 130], [420, 130], [440, 130], [430, 130], [440, 140], [420, 140], [410, 140], [430, 140], [400, 140], [390, 140], [380, 140], [360, 140], [350, 150], [350, 140], [320, 160], [250, 160], [240, 150], [250, 150], [270, 150], [260, 150], [280, 160], [290, 160], [280, 150], [300, 150], [290, 150], [310, 150], [320, 150], [330, 150], [340, 150], [360, 150], [370, 150], [380, 150], [400, 150], [410, 150], [390, 150], [430, 150], [420, 150], [440, 150], [420, 170], [410, 170], [400, 180], [400, 200], [410, 200], [410, 220], [400, 230], [380, 230], [360, 240], [340, 250], [320, 250], [300, 250], [260, 250], [240, 250], [230, 250], [220, 250], [220, 240], [240, 230], [230, 230], [230, 240], [220, 230], [220, 220], [220, 210], [230, 220], [240, 220], [240, 210], [230, 210], [230, 200], [230, 190], [230, 180], [230, 170], [230, 160], [240, 170], [240, 160], [250, 170], [260, 170], [260, 160], [270, 160], [270, 170], [280, 170], [290, 170], [300, 170], [310, 160], [300, 160], [310, 170], [320, 180], [320, 170], [330, 160], [330, 170], [340, 170], [340, 160], [350, 160], [350, 170], [360, 170], [360, 160], [380, 160], [370, 160], [400, 160], [390, 160], [420, 160], [410, 160], [430, 160], [440, 160], [430, 170], [440, 170], [440, 180], [430, 180], [420, 180], [400, 170], [410, 180], [390, 180], [390, 170], [380, 170], [380, 180], [370, 180], [370, 170], [360, 180], [350, 190], [350, 180], [340, 180], [330, 180], [310, 180], [300, 180], [280, 180], [290, 180], [270, 190], [270, 180], [260, 180], [250, 180], [240, 200], [240, 190], [260, 200], [260, 190], [250, 200], [250, 190], [280, 190], [310, 190], [320, 200], [320, 190], [330, 190], [340, 190], [360, 190], [370, 190], [380, 190], [390, 190], [400, 190], [410, 190], [440, 190], [430, 190], [420, 190], [430, 200], [440, 200], [420, 200], [430, 210], [440, 210], [410, 210], [400, 210], [390, 210], [380, 210], [380, 200], [360, 200], [340, 200], [330, 210], [320, 210], [330, 200], [300, 210], [300, 200], [290, 200], [270, 200], [280, 200], [260, 210], [250, 210], [250, 230], [240, 240], [250, 240], [250, 250], [260, 230], [260, 240], [260, 220], [250, 220], [270, 210], [280, 210], [270, 220], [270, 240], [270, 230], [270, 250], [280, 250], [290, 250], [280, 240], [280, 230], [280, 220], [290, 220], [290, 210], [290, 230], [290, 240], [300, 240], [300, 230], [300, 220], [310, 210], [310, 220], [310, 230], [310, 240], [310, 250], [320, 240], [320, 230], [320, 220], [330, 220], [340, 220], [350, 200], [370, 200], [390, 200], [370, 210], [350, 220], [340, 230], [330, 230], [330, 250], [330, 240], [340, 240], [350, 240], [350, 230], [360, 230], [360, 220], [370, 230], [380, 220], [390, 220], [400, 220], [420, 210], [420, 220], [430, 220], [440, 230], [440, 220], [440, 240], [430, 250], [430, 240], [440, 250], [420, 230], [420, 240], [430, 230], [400, 250], [390, 250], [380, 250], [370, 250], [360, 250], [370, 220], [380, 240], [370, 240], [350, 250], [390, 230], [390, 240], [400, 240], [410, 230], [410, 250], [410, 240], [420, 250], [430, 270], [440, 270], [440, 280], [410, 270], [400, 270], [380, 270], [370, 270], [360, 270], [350, 270], [340, 270], [330, 270], [320, 280], [250, 270], [240, 270], [260, 270], [260, 290], [240, 290], [240, 300], [240, 320], [240, 330], [240, 310], [240, 340], [240, 350], [240, 370], [250, 370], [270, 370], [260, 370], [260, 360], [250, 360], [270, 360], [250, 350], [270, 350], [280, 350], [290, 350], [260, 350], [260, 340], [250, 340], [250, 330], [260, 330], [260, 320], [250, 310], [250, 300], [250, 290], [260, 310], [260, 300], [260, 280], [280, 270], [270, 280], [270, 270], [270, 290], [270, 300], [270, 330], [270, 310], [270, 320], [280, 340], [270, 340], [280, 330], [300, 340], [300, 330], [290, 330], [290, 340], [280, 320], [290, 320], [300, 320], [300, 310], [280, 310], [290, 310], [280, 300], [280, 290], [280, 280], [290, 280], [300, 280], [310, 270], [300, 270], [290, 270], [300, 290], [290, 290], [290, 300], [330, 290], [370, 290], [380, 300], [440, 330], [430, 340], [420, 350], [390, 360], [390, 350], [380, 360], [360, 360], [320, 370], [320, 360], [340, 350], [340, 360], [380, 370], [420, 370], [430, 370], [440, 370], [440, 350], [430, 360], [410, 370], [400, 370], [390, 370], [350, 370], [370, 370], [360, 370], [340, 370], [330, 370], [300, 370], [290, 370], [280, 370], [310, 370], [300, 360], [310, 360], [310, 340], [310, 330], [310, 320], [310, 310], [310, 300], [310, 290], [310, 280], [320, 270], [300, 300], [320, 300], [340, 290], [320, 290], [340, 310], [340, 300], [350, 300], [340, 280], [330, 280], [330, 310], [330, 300], [330, 330], [320, 340], [320, 330], [330, 350], [320, 350], [330, 360], [330, 340], [340, 340], [340, 330], [350, 330], [350, 350], [350, 340], [350, 360], [360, 350], [370, 360], [370, 350], [370, 340], [380, 350], [360, 340], [370, 330], [370, 320], [350, 310], [360, 300], [350, 290], [350, 280], [370, 280], [380, 280], [360, 280], [360, 290], [380, 290], [370, 310], [370, 300], [360, 310], [360, 330], [380, 330], [380, 340], [390, 330], [410, 350], [420, 360], [410, 360], [400, 360], [400, 350], [440, 360], [430, 350], [440, 340], [430, 330], [430, 320], [440, 320], [440, 310], [440, 300], [440, 290], [430, 290], [430, 280], [420, 280], [420, 270], [410, 280], [400, 280], [390, 270], [390, 280], [390, 290], [380, 310], [390, 320], [390, 310], [390, 300], [400, 290], [400, 310], [400, 300], [400, 330], [400, 320], [400, 340], [420, 340], [410, 340], [410, 330], [420, 330], [420, 320], [410, 320], [410, 310], [410, 300], [420, 310], [430, 310], [430, 300], [420, 300], [420, 290], [410, 290]],
         [],
         ]
food=[[210, 50], [200, 50], [190, 50], [180, 50], [170, 50], [160, 50], [160, 60], [160, 70], [160, 80], [170, 80], [180, 80], [190, 80], [200, 80], [210, 80], [210, 90], [210, 100], [210, 110], [210, 120], [210, 130], [200, 130], [190, 130], [180, 130], [170, 130], [160, 130], [230, 130], [230, 120], [230, 110], [230, 100], [230, 90], [240, 90], [250, 100], [250, 90], [250, 110], [250, 120], [250, 130], [270, 120], [270, 110], [270, 100], [280, 90], [290, 90], [280, 130], [290, 130], [300, 100], [300, 110], [300, 120], [310, 130], [330, 130], [330, 120], [330, 110], [330, 100], [330, 90], [340, 110], [350, 100], [360, 90], [350, 120], [360, 130], [380, 90], [380, 100], [380, 110], [380, 120], [380, 130], [390, 130], [400, 130], [410, 130], [390, 110], [400, 110], [410, 110], [380, 80], [390, 90], [400, 90], [410, 90]]

Levels = [
    Level(0, walls=walls[0], win_point=[[100,100]]),
    Level(4, win_point=[[560, 400]],walls=walls[1],food_point2=[210, 590]),
    Level(9,win_point=[[310, 260]]),
    Level(3)
]
