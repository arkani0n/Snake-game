import random

class Level:
    def __init__(self, rate, walls=[], bombs=[], food_point1=[0, 0],
                 food_point2=[600, 600], win_point=[], food_from_start=[[-10, -10]]):

        self.win_point = win_point
        self.walls = walls
        self.bombs = bombs.copy()
        self.food = food_from_start
        self.area = [food_point1, food_point2]
        self.rate = rate  # higher the rate -- higher the probability of food spawn

    def spawn_food(self):

        if random.randint(0, 11) < self.rate:
            x_for_spawn = -10
            y_for_spawn = -10
            while [x_for_spawn, y_for_spawn] in self.food:
                x_for_spawn = random.randint(self.area[0][0] / 10, self.area[1][0] / 10) * 10
                y_for_spawn = random.randint(self.area[0][1] / 10, self.area[1][1] / 10) * 10
            self.food.append([x_for_spawn, y_for_spawn])
