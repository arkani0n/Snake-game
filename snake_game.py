import tkinter
import operator
import time
import random

import settings
from entities.snake import Snake
import engine
import levels
from tkinter import messagebox


# ============= Functions

def add_piace(level,player):
    num= random.randint(0,3)
    x_cord=random.randint(0,60)
    y_cord=random.randint(0,60)
    piece=settings.pieces[num]
    for i in range(len(piece)):
        piece[i]=[piece[i][0]+x_cord*10,piece[i][1]+y_cord*10]
        if piece[i] in player.snake:
            add_piace(level,player)
            return

    level.walls.extend(piece.copy())



def show_tutorial():
    global for_labels
    for_labels = tkinter.Label(root, text=settings.for_tutorial, bg='black', fg='white', font='Calibri 13')
    for_labels.pack(side=tkinter.TOP, fill=tkinter.Y)


def show_highscore():
    global for_labels
    if for_labels != None:
        for_labels.destroy()
    top10 = []
    stats = engine.read_data('highscore')
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

    for_labels = tkinter.Label(root, text=top10_list, bg='black', fg='white')
    for_labels.place(anchor=tkinter.SE,rely=0.5, relx=1)
    return lowest_score, all_scores


root = tkinter.Tk()
root.resizable(width=False, height=False)
root.geometry(settings.ROOT_SIZE)
root.title(settings.GAME_TITLE)
root['bg'] = settings.ROOT_BG
canvas = tkinter.Canvas(root, width=600, height=600)

# ???
level_switch_variable = tkinter.IntVar()
level_switch_variable.set(None)

# ???
for_labels = None
already_placed_buttons = []

is_show_massagebox = True
user_name = None
user_snake = Snake(root)
current_level = None


# ??

def change_level():
    global current_level

    current_level_index = level_switch_variable.get()

    current_level = levels.Levels[current_level_index]
    engine.restart(user_snake, current_level, current_level_index)

    play(root, canvas, current_level, user_snake, current_level_index,)


def play(root, canvas, current_level, user_snake, level_index):
    global for_labels
    global is_show_massagebox
    is_show_massagebox=True
    move_counter=0


    if level_index == 3:
        lowest,all_scores=show_highscore()
    elif level_index == 0:
        show_tutorial()
    while is_show_massagebox:
        root.update()
        root.update_idletasks()



        # logic
        if user_snake.is_error() or (user_snake.head() in current_level.walls):
            #in_game = False
            if level_index==3:
                if user_snake.eaten >= lowest:
                    all_scores.append(str(user_snake.eaten)+'='+user_name)
                engine.update_data(all_scores)
            if is_show_massagebox:
                is_show_massagebox=False
                is_again = tkinter.messagebox.askquestion(
                'game over', 'Игра окончена \n Набрано:' + str(user_snake.eaten) + ' очков \n Начать заново?')
                if is_again == 'yes':
                    is_show_massagebox=True
                    if level_index==3:
                        show_highscore()
                    engine.restart(user_snake, current_level, level_index)
            else:
                break
        else:
            if user_snake.head() in current_level.win_point:
                progress = engine.read_data('progress')
                progress[str(level_index + 1)] = '1'
                engine.update_progress(progress)
                place_level_button(already_placed_buttons)
                return

            user_snake.move()
            move_counter+=1

            current_level.spawn_food()
            if user_snake.head() in current_level.food:
                current_level.food.remove(user_snake.head())
                user_snake.grow()
                user_snake.eaten += 1

            if user_snake.head() in current_level.bombs:
                current_level.bombs.remove(user_snake.head())
                user_snake.damage(settings.DAMAGE_BOMB)

            if move_counter==50 and level_index==3:
                add_piace(current_level,user_snake)
                move_counter=0

            # draw objects
            if is_show_massagebox:
                canvas.delete('all')
                for list, color in [[current_level.food, settings.COLOR_FOOD],
                                    [current_level.walls, settings.COLOR_WALL],
                                    [current_level.bombs, settings.COLOR_BOMB],
                                    [current_level.win_point, settings.COLOR_WIN_POINT],
                                    [user_snake.snake, settings.COLOR_SNAKE]]:
                    engine.draw(canvas, list, color)


            time.sleep(0.1 if is_show_massagebox else 0)


def place_level_button(placed_buttons):
    progress = engine.read_data('progress')

    # draw buttons
    for button in settings.buttons:

        if button.value in placed_buttons:
            continue

        elif progress[str(button.value)] == '1':
            tkinter.Radiobutton(root, text=button.name, variable=level_switch_variable,
                                indicatoron=False, value=button.value, width=8,
                                command=change_level).place(anchor=tkinter.NW, rely=button.relY)
            placed_buttons.append(button.value)


def start():
    global user_name
    global for_labels
    if for_labels != None:
        for_labels.destroy()
    else: user_name_label.destroy()
    user_name = user_name_entery.get()
    if user_name=='':
        for_labels = tkinter.Label(text='Enter your name please', bg='red')
        for_labels.place(rely=0.37, relx=0.4)
        return
    for i in settings.NOT_ALLOWED_SIMMONS:
        if i in user_name:
            if for_labels != None:
                for_labels.destroy()
            for_labels=tkinter.Label(text='Not allowed symbol')
            for_labels.place(rely=0.37, relx=0.4)

            return

    start_game_button.destroy()
    user_name_entery.destroy()

    canvas.pack(side=tkinter.BOTTOM)
    place_level_button(already_placed_buttons)

user_name_entery = tkinter.Entry(root)
start_game_button = tkinter.Button(text='Start', command=start)
user_name_label = tkinter.Label(text='Enter your name')
user_name_label.place(rely=0.37, relx=0.4)
user_name_entery.place(rely=0.4, relx=0.4)
start_game_button.place(relx=0.45, rely=0.43)
root.mainloop()


