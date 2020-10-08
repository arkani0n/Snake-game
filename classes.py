import random


class Snake:
    def __init__(self, root):
        self.snake = [[10, 10], [10, 20], [10, 30]]
        self.eaten = 0
        self.direction = 'right'
        self.root = root
        self.root.bind('<w>', self.change_direction)
        self.root.bind('<s>', self.change_direction)
        self.root.bind('<d>', self.change_direction)
        self.root.bind('<a>', self.change_direction)

    def move(self):
        # head move
        head = self.snake[0].copy()
        if self.direction == 'right':
            self.snake[0][0] += 10
        if self.direction == 'left':
            self.snake[0][0] -= 10
        if self.direction == 'down':
            self.snake[0][1] += 10
        if self.direction == 'up':
            self.snake[0][1] -= 10
            # body move
        if len(self.snake) == 1:
            return
        for i in range(len(self.snake)):
            if i == len(self.snake) - 1:  # if next part is head
                self.snake[1] = head.copy()
                break
            self.snake[-i - 1] = self.snake[
                -i - 2].copy()  # replasing every part coordinates to coordinates of next part

    def change_direction(self, event):
        if event.keysym == 'w' and self.direction != 'down':
            self.direction = 'up'
        if event.keysym == 's' and self.direction != 'up':
            self.direction = 'down'
        if event.keysym == 'd' and self.direction != 'left':
            self.direction = 'right'
        if event.keysym == 'a' and self.direction != 'right':
            self.direction = 'left'

    def grow(self):
        self.snake.append(self.snake[-1].copy())

    def damage(self, num):
        for i in range(num if len(self.snake) > num else len(self.snake)):
            self.snake.remove(self.snake[0])

    def eror(self):
        if self.snake[0][1] < 0:
            return True
        if self.snake[0][0] < 0:
            return True
        if self.snake[0][1] > 600:
            return True
        if self.snake[0][0] > 600:
            return True
        if self.snake[0] in self.snake[2::]:
            return True


class Level:
    def __init__(self, rate, walls=[], bombs=[], food_point1=[0, 0],
                 food_point2=[600, 600], win_point=None, food_from_start=[[-10, -10]]):

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
