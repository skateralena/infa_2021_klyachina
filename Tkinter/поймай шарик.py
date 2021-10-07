from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

l = Label(root, bg='white', fg='black', width=40)
global score
score = 0
l['text'] = 'score: ' + str(score)
l.pack()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'lightblue', 'lightgreen', 'brown', 'black']
balls = set()
removedBalls = set()

def new_ball():
    """функция отрисовывает шарик
    x, y - координаты центра шарика"""
    global balls
    #canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    color = choice(colors)
    dx = rnd(-30, 30)
    dy = rnd(-30, 30)
    circle = canv.create_oval(x-r, y-r, x+r, y+r, fill=color, width=0)
    balls.add((circle, x, y, r, color))
    #canv.move(circle, 10, 20)
    root.after(1000, new_ball)

def clickOnBall(event):
    global score
    for ball in balls:
        x = ball[1]
        y = ball[2]
        r = ball[3]
        color = ball[4]
        if (x - event.x)**2 + (y - event.y)**2 <= r**2:
            if color == 'black':
                score = 0
                l['text'] = 'score: 0 !!!DO NOT CLICK ON BOMBS!!!'
            else:
                score += 1
                l['text'] = 'score: ' + str(score)
            removedBalls.add(ball)
            canv.create_oval(x-r, y-r, x+r, y+r, fill='white', width=0)
    balls.difference_update(removedBalls)
    removedBalls.clear()



for i in range(rnd(1, 2)):
    new_ball()
canv.bind('<Button-1>', clickOnBall)


print('kek')
root.mainloop()




#new_ball()
#canv.bind('<Button-1>', clickOnBall)
#root.mainloop()




