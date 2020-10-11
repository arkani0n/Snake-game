import tkinter, time

from levels import *


# ============= Functions
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


def change_level():
    global in_game
    global current_level
    curent_level_index=switch_variable.get()
    in_game = False
    current_level = Levels[curent_level_index]
    restart(user_snake, current_level, curent_level_index)
    in_game = True
    play(root, canvas, current_level, user_snake,curent_level_index)


def play(root, canvas, current_level, user_snake,level_index):
    global in_game
    end = 0

    while in_game:
        root.update()
        root.update_idletasks()

        canvas.delete('all')
        for list, color in [[current_level.food, 'green'],
                            [current_level.walls, 'blue'],
                            [current_level.bombs, 'red'],
                            [current_level.win_point, 'yellow'],
                            [user_snake.snake, 'black']]:
            draw(canvas, list, color)
        if len(user_snake.snake) == 0 or (user_snake.eror() or user_snake.snake[0] in current_level.walls):
            in_game = False
        else:
            if user_snake.snake[0] in current_level.win_point:
                progress[str(level_index+1)]='1'
                update_progress()
                place_level_button()
                return
            user_snake.move()
            current_level.spawn_food()
            if user_snake.snake[0] in current_level.food:
                current_level.food.remove(user_snake.snake[0])
                user_snake.grow()

            if user_snake.snake[0] in current_level.bombs:
                current_level.bombs.remove(user_snake.snake[0])
                user_snake.damage(2)

            time.sleep(0.1 if in_game else 0)



# ========================== ROOT WINDOW SETTINGS
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=600, height=600)
root.resizable(width=False, height=False)
root.geometry('800x700')
root.title('SNAKE')
root['bg'] = 'black'

switch_variable = tkinter.IntVar()
switch_variable.set(None)
for_buttons = [("Tutorial", 0.26, 0),
               ("Level  1", 0.30, 1),
               ("Level  2", 0.34, 2),
               ("Level  3", 0.38, 3),
               ]

allready_placed = []
canvas.pack(side=tkinter.BOTTOM)
in_game = False
user_snake = classes.Snake(root)
current_level = None
progress = {}


# ========== Progress

def place_level_button():
    with open('user_progress.txt', 'r+') as file:
        for i in file.readlines():
            i=i.strip().split('=')
            progress[i[0]]=i[1]
        print(progress)
        for i in for_buttons:
            if i[0] in allready_placed:
                continue
            if int(progress[str(i[2])]):
                tkinter.Radiobutton(root, text=i[0], variable=switch_variable,
                            indicatoron=False, value=i[2], width=8,
                            command=change_level).place(anchor=tkinter.NW, rely=i[1])
                allready_placed.append(i[2])

def update_progress():
    with open('user_progress.txt','w') as file:
        for i in progress:
            file.write(i+'='+progress[i])
            file.write('\n')
place_level_button()
# ==========Progres
root.mainloop()
