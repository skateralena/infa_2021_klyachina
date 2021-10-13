from tkinter import *
from random import randrange as rnd, choice


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

label = Label(root, bg='white', fg='black', width=40)
global score
score = 0
label['text'] = 'score: ' + str(score)
label.pack()
colors = ['salmon', 'orange', 'yellow', 'greenyellow', 'plum', 'pink', 'lightblue', 'lightgreen', 'black', 'black']
balls = []  # хранит данные о всех когда-либо существовавших шариках
aliveBalls = set()   # множество номеров всех живых шариков из массива Balls

def new_ball():
    """функция создает новый шарик
    x, y - координаты центра шарика
    r - radius
    color - ball's color
    dx, dy - проекции вектора перемещения"""
    global balls
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    color = choice(colors)
    dx = rnd(-5, 5)
    dy = rnd(-5, 5)
    balls.append([x, y, r, color, dx, dy])
    aliveBalls.add(len(balls)-1)

def clickOnBall(event):
    '''
    функция определяет кликнули ли мышей по одному из живущих шариков
    если да: убирает его
    иначе: ничего не делает
    '''
    global score
    for i in aliveBalls:
        x = balls[i][0]
        y = balls[i][1]
        r = balls[i][2]
        color = balls[i][3]
        if (x - event.x)**2 + (y - event.y)**2 <= r**2:
            if color == 'black':
                score = 0
                label['text'] = 'score: 0 !!!DO NOT CLICK ON BOMBS!!!'
            else:
                score += 1
                label['text'] = 'score: ' + str(score)
            aliveBalls.remove(i)

def movingFunc():
    '''
    функция отрисовывает все шарики
    пересчитывает координаты каждого, в зависимости от его положения и вектора скорости
    '''
    global balls
    canv.delete(ALL)
    for i in aliveBalls:
        dx = balls[i][4]
        dy = balls[i][5]
        balls[i][0] += dx
        balls[i][1] += dy
        x = balls[i][0]
        y = balls[i][1]
        r = balls[i][2]
        if y - r <= 5 or y + r >= 575:
            balls[i][5] = -dy
        if x - r <= 5 or x + r >= 795:
            balls[i][4] = -dx
        color = balls[i][3]
        canv.create_oval(x-r, y-r, x+r, y+r, fill=color, width=0)

def main():
    if rnd(0, 20) == 1: new_ball()
    movingFunc()
    root.after(50, main)


main()
canv.bind('<Button-1>', clickOnBall)
root.mainloop()






