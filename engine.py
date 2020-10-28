from levels import *
import settings

# progress

def restart(snake, level, num):
    snake.snake = [[10, 10], [10, 20], [10, 30]]
    snake.eaten = 0
    snake.direction = 'right'
    level.food = food.copy() if num==0 else [[-10,-10]]
    level.bombs = bombs[num].copy()

def draw(canvas, list, color):
    for i in range(len(list)):
        canvas.create_rectangle(
            list[i][0], list[i][1], list[i][0] + 10, list[i][1] + 10, fill=(color))


a='dasda'
a.replace(' ','=')
# PROGRESS

def update_progress(progress):
    with open(settings.USER_PROGRESS_FILE,'w') as file:
        for i in progress:
            file.write(i+'='+progress[i])
            file.write('\n')

def update_data(data):
    with open(settings.HIGHSCORE_FILE, 'w') as file:
        for i in data:
            file.write(i.replace('=',' '))
            if data.index(i)!=len(data)-1:
                file.write('\n')

def read_data(mode):

    data = {}

    with open(settings.USER_PROGRESS_FILE if mode=='progress'
            else settings.HIGHSCORE_FILE,'r') as file:
        for i in file.readlines():
            i = i.strip().split('=' if mode=='progress' else ' ')
            if i==[]:
                break
            if mode=='progress':
                data[i[0]]=i[1]
            else: data[int(i[0])]=i[1]
        return data

