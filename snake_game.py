import tkinter
import operator
import time
import settings
from entities.snake import Snake
import engine
import levels
from tkinter import messagebox


# ============= Functions
def show_tutorial():
    global for_labels
    for_labels = tkinter.Label(root, text=settings.for_tutorial, bg='black', fg='white',font='Calibri 13')
    for_labels.pack(side=tkinter.TOP, fill=tkinter.Y)
def show_highscore():
    global for_labels
    stats = {}
    top10 = []
    with open('high_score.txt', 'r') as file:
        first_line = True
        for i in file.readlines():
            if i == []:
                break
            i = i.strip().split()

            stats[int(i[0])] = i[1]
            if first_line:
                first_line = False
                record = i[0]
        for i in sorted(stats.items(), key=operator.itemgetter(0), reverse=True):
            if len(top10) == 10:
                record = int(i[1])
                break
            top10.append(str(i[0]) + ' ' + i[1])
        top10_list = ''
        for i in top10:
            top10_list += i + '\n'
    for_labels = tkinter.Label(root, text=top10_list, bg='black', fg='white')
    for_labels.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    return record


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

in_game = False
user_snake = Snake(root)
current_level = None


# ??

def change_level():
    global in_game
    global current_level

    current_level_index = level_switch_variable.get()
    in_game = False

    current_level = levels.Levels[current_level_index]
    engine.restart(user_snake, current_level, current_level_index)

    in_game = True
    play(root, canvas, current_level, user_snake, current_level_index)


def play(root, canvas, current_level, user_snake, level_index):
    global in_game
    global for_labels

    if for_labels != None:
        for_labels.destroy()
    if level_index==3:
        show_highscore()
    elif level_index==0:
        show_tutorial()

    while True:
        root.update()
        root.update_idletasks()

        canvas.delete('all')

        # draw objects
        for list, color in [[current_level.food, settings.COLOR_FOOD],
                            [current_level.walls, settings.COLOR_WALL],
                            [current_level.bombs, settings.COLOR_BOMB],
                            [current_level.win_point, settings.COLOR_WIN_POINT],
                            [user_snake.snake, settings.COLOR_SNAKE]]:
            engine.draw(canvas, list, color)

        # logic
        if user_snake.is_error() or (user_snake.head() in current_level.walls):
            is_again = tkinter.messagebox.askquestion(
                'game over', 'Игра окончена \n Набрано:' + str(user_snake.eaten) + ' очков \n Начать заново?')
            if is_again == 'yes':
                engine.restart(user_snake, current_level, level_index)
            else:
                break
        else:
            if user_snake.head() in current_level.win_point:
                progress = engine.read_progress()
                progress[str(level_index + 1)] = '1'
                engine.update_progress(progress)

                place_level_button(already_placed_buttons)
                return
            user_snake.move()
            current_level.spawn_food()
            if user_snake.head() in current_level.food:
                current_level.food.remove(user_snake.head())
                user_snake.grow()
                user_snake.eaten+=1

            if user_snake.head() in current_level.bombs:
                current_level.bombs.remove(user_snake.head())
                user_snake.damage(settings.DAMAGE_BOMB)

            time.sleep(0.05)  


def place_level_button(placed_buttons):
    progress = engine.read_progress()

    # draw buttons
    for button in settings.buttons:

        if button.value in placed_buttons:
            continue

        if progress[str(button.value)] == '1':
            tkinter.Radiobutton(root, text=button.name, variable=level_switch_variable,
                                indicatoron=False, value=button.value, width=8,
                                command=change_level).place(anchor=tkinter.NW, rely=button.relY)
            placed_buttons.append(button.value)


place_level_button(already_placed_buttons)
canvas.pack(side=tkinter.BOTTOM)
root.mainloop()

