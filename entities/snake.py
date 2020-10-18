
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
        self.wait_until_next_move=False

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
        self.wait_until_next_move=False
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
        if event.keysym == 'w' and self.direction != 'down' and self.wait_until_next_move==False:
            self.direction = 'up'
        if event.keysym == 's' and self.direction != 'up' and self.wait_until_next_move==False:
            self.direction = 'down'
        if event.keysym == 'd' and self.direction != 'left' and self.wait_until_next_move==False:
            self.direction = 'right'
        if event.keysym == 'a' and self.direction != 'right' and self.wait_until_next_move==False:
            self.direction = 'left'
        self.wait_until_next_move=True

    def grow(self):
        self.snake.append(self.snake[-1].copy())

    def damage(self, num):
        for i in range(num if len(self.snake) > num else len(self.snake)):
            self.snake.remove(self.snake[0])

    def is_error(self):
        if len(self.snake) == 0 or \
                self.snake[0][1] < 0 or \
                self.snake[0][0] < 0 or \
                self.snake[0][1] > 600 or \
                self.snake[0][0] > 600 or \
                self.snake[0] in self.snake[2::]:
            return True

    def head(self):
        return self.snake[0]

