from tkinter import *
from random import randrange as rnd, choice


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

scoreLabel = Label(root, bg='white', fg='black', width=40)
label = Label(root, bg='white', fg='black', width=40)
label['text'] = 'введите свое имя'
label.pack()
e = Entry(root, width=20)
e.pack()
b = Button(root, text='завершить игру')
b.pack()

global score
score = 0
scoreLabel['text'] = 'score: ' + str(score)
scoreLabel.pack()
colors = ['salmon', 'orange', 'yellow', 'greenyellow', 'plum', 'pink', 'lightblue', 'lightgreen', 'black', 'black']
balls = []  # хранит данные о всех когда-либо существовавших шариках
aliveBalls = set()   # множество номеров всех живых шариков из массива Balls

notfinished = True

def save_result(event):
    global notfinished
    name = e.get()
    file = open('results.txt', 'a')
    file.write(name + ' ' + str(score) + "\n")
    file.close()
    notfinished = False

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

def draw_bamb(x, y, r, color):
    canv.create_oval(x - r, y - r, x + r, y + r, fill=color, width=0)
    canv.create_polygon(x + 2*r//3, y - r, x+r, y - 2*r//3, x + 2*r//3, y - r//3, x + r//3, y - 2*r//3, x + 2*r//3, y - r, fill='black', width=0)
    canv.create_line(x, y, x+r, y-r, x + 4*r//3, y-r, x + 7*r//6, y - r//3, x + 4*r//3, y,  smooth=1, width=2)

def clickOnBall(event):
    '''
    функция определяет кликнули ли мышей по одному из живущих шариков
    если да: убирает его
    иначе: ничего не делает
    '''
    global score
    removedBalls = set()
    for i in aliveBalls:
        x = balls[i][0]
        y = balls[i][1]
        r = balls[i][2]
        color = balls[i][3]
        if (x - event.x)**2 + (y - event.y)**2 <= r**2:
            if color == 'black':
                score = 0
                scoreLabel['text'] = 'score: 0 !!!DO NOT CLICK ON BOMBS!!!'
            else:
                score += 1
                scoreLabel['text'] = 'score: ' + str(score)
            removedBalls.add(i)
    aliveBalls.difference_update(removedBalls)

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
        if color == 'black':
            draw_bamb(x, y, r, 'black')
        else:
            canv.create_oval(x-r, y-r, x+r, y+r, fill=color, width=0)

def main():
    if rnd(0, 20) == 1: new_ball()
    movingFunc()
    if notfinished:
        root.after(50, main)

b.bind('<Button-1>', save_result)
main()
canv.bind('<Button-1>', clickOnBall)
root.mainloop()
