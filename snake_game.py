from  tkinter import *
from game_window import *
import operator
import tkinter.messagebox
def record_rewtite(list):
    with open('record.txt','w') as f:
        f.write(list)
def Start1():
    canvas.pack()
    Play(root)
    #root.mainloop()

def Play(root):
    global top10_list
    global user_name
    while True:
        root.update()
        Move()
        if random.randint(0,11)>0:
            Spawn_food()
        Print(canvas)
        time.sleep(0.2-Score()*0.01 if Score()*0.01<0.16 else 0.04)
        if Eror():
            if Score()>=antirecord or len(top10)<10:
                top10_list+=str(Score())+' '+str(user_name.get())+'\n'
                record_rewtite(top10_list)
            again=tkinter.messagebox.askquestion(
                'game over','Игра окончена \n Набрано:'+str(Score())+' очков \n Начать заново?')
            if again=='yes':
                Restart()
            else: break


#settings
root=Tk()
canvas = Canvas(root, width=600, height=600)
root.resizable(width=False,height=False)
root.geometry('600x700')
root.title('SNAKE')
root['bg']='black'
root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<Right>', right)
root.bind('<Left>', left)
#record
stats={}
top10=[]
antirecord=0
file=open('record.txt','r')
for i in file.readlines():
    i=i.strip().split()
    if i==[]:
        break
    stats[str(i[0])]=i[1]
file.close()
for i in sorted(stats.items(),key=operator.itemgetter(0),reverse=True):
    if int(i[0])<antirecord:
        record=int(i[1])
    if len(top10)==10:
        break
    top10.append(str(i[0]+' '+i[1]))
top10_list=''
for i in top10:
    top10_list+=i+'\n'
#start

great=Label(root,text='Welcom to the snake game \n to begin press \'START\'',bg='black',fg='white').pack()
high_score=Label(root,text=top10_list,bg='black',fg='white')
high_score.pack(side=RIGHT,fill=Y)

start_button=Button(root,text='START',command=Start1).pack()
###entry,entry.get()
user_name=Entry(root)
user_name.pack()

root.mainloop()
