import time
import random

#root = Tk()



eaten=0
snake_=[[10,10],[10,20],[10,30]]
move_count=0
dirrection='r'
food=[]


#bind
def up(event):
    global dirrection
    if dirrection!='d':
        dirrection='u'
def down(event):
    global dirrection
    if  dirrection!='u':
        dirrection='d'
def right(event):
    global dirrection
    if  dirrection!='l':
        dirrection='r'
def left(event):
    global dirrection
    if  dirrection!='r':
        dirrection='l'


#displaying
def Print(canvas):
    canvas.delete('all')
    for i in range(len(snake_)):
        canvas.create_rectangle(snake_[i][0],snake_[i][1],snake_[i][0]+10,snake_[i][1]+10,fill='black')
    for i in range(len(food)):
        canvas.create_rectangle(food[i][0],food[i][1],food[i][0]+10,food[i][1]+10,fill='green')
def Eror():
    if snake_[0][1] < 0:
        return True
    if snake_[0][0] < 0 :
        return True
    if snake_[0][1] > 600:
        return True
    if snake_[0][0] > 600:
        return True
    if snake_[0] in snake_[1::]:
        return True
#snake
def Move():
    global eaten
    global move_count
    move_count+=1
    head=snake_[0].copy()
    if dirrection=='r':
        snake_[0][0]+=10
    if dirrection=='l':
        snake_[0][0]-=10
    if dirrection=='d':
        snake_[0][1]+=10
    if dirrection=='u':
        snake_[0][1]-=10

    if head in food:
        got_food=True
        food.remove(head)
        eaten+=1
    else: got_food=False

    if got_food==False:
        for i in range(len(snake_)):
            if i==len(snake_)-1:
                snake_[1]=head.copy()
                break
            snake_[-i-1]=snake_[-i-2].copy()
    else:
        snake_.insert(1,head.copy())


#food
def Score():
    global eaten
    return eaten
def Spawn_food():
    x=random.randint(0,60)*10
    y=random.randint(0,60)*10
    food.append([x,y])
#restart
def Restart():
    global food
    global eaten
    global snake_
    global move_count
    global dirrection
    food = []
    eaten = 0
    snake_ = [[10, 10], [10, 20], [10, 30]]
    move_count = 0
    dirrection = 'r'


