from levels import *
import settings
import random
import tkinter
import operator

# TUTORIAL
def show_tutorial(window):
    tutorial_text = tkinter.Label(window, text=settings.for_tutorial, bg='black', fg='white', font='Calibri 13')
    tutorial_text.pack(side=tkinter.TOP, fill=tkinter.Y)
    return tutorial_text

 # SURVAIVAL

def show_highscore(label,window):
    if label != None:
        label.destroy()
    top10 = []
    stats = read_data('highscore')
    stats=sorted(stats.items(), key=operator.itemgetter(0), reverse=True)
    for i in stats:
        if len(top10) == 10:
            break
        top10.append(str(i[0]) + ' ' + i[1])
    all_scores=top10.copy()
    lowest_score=int(top10[-1].split()[0])
    top10_list = ''
    for i in top10:
        top10_list += i + '\n'

    label = tkinter.Label(window, text=top10_list, bg='black', fg='white')
    label.place(anchor=tkinter.SE,rely=0.5, relx=1)
    return lowest_score, all_scores,label

def add_piace(level,player):
    num= random.randint(0,len(settings.pieces)-1)
    x_cord=random.randint(0,50)
    y_cord=random.randint(0,50)
    piece=settings.pieces[num]
    for i in range(len(piece)):
        piece[i]=[piece[i][0]+x_cord*10,piece[i][1]+y_cord*10]
        if piece[i][0] >600:
            piece[i][0]-=piece[i][0]//600*600
        if piece[i][1] > 600:
            piece[i][1] -= piece[i][1]//600*600
        if piece[i] in player.snake:
            piece = None
            print('agin',piece)
            add_piace(level,player)
            return
    level.walls.extend(piece.copy())


# GUI

def place_level_button(placed_buttons, swich_variable, function,window):
    progress = read_data('progress')

    # draw buttons
    for button in settings.buttons:

        if button.value in placed_buttons:
            continue

        elif progress[str(button.value)] == '1':
            tkinter.Radiobutton(window, text=button.name, variable=swich_variable,
                                indicatoron=False, value=button.value, width=8,
                                command=function).place(anchor=tkinter.NW, rely=button.relY)
            placed_buttons.append(button.value)

#

def restart(snake, level, num):
    snake.snake = [[10, 10], [10, 20], [10, 30]]
    snake.eaten = 0
    snake.direction = 'right'
    level.food = food.copy() if num==0 else [[-10,-10]]
    level.bombs = bombs[num].copy()
    level.walls=walls[num].copy()

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
