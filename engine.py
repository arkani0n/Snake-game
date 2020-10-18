from levels import *
import settings

# progress

def restart(snake, level, num):
    snake.snake = [[10, 10], [10, 20], [10, 30]]
    snake.eaten = 0
    snake.direction = 'right'
    level.food = [[-10, -10]]
    level.bombs = bombs[num].copy()

def draw(canvas, list, color):
    for i in range(len(list)):
        canvas.create_rectangle(
            list[i][0], list[i][1], list[i][0] + 10, list[i][1] + 10, fill=(color))



# PROGRESS

def update_progress(progress):
    with open(settings.USER_PROGRESS_FILE,'w') as file:
        for i in progress:
            file.write(i+'='+progress[i])
            file.write('\n')

def read_progress():
    progress = {}
    with open(settings.USER_PROGRESS_FILE,'r') as file:
        for i in file.readlines():
            i = i.strip().split('=')
            progress[i[0]]=i[1]
    return progress

