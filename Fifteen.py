import os
from tkinter import * 
from tkinter.ttk import Combobox 
import random

def Check():
    check = True
    for i in range(size[0]):
        for j in range(size[0]):
            if str(field[i][j]) != button_field[i][j]['text']:
                check = False
                button_field[i][j]['bg'] = '#e3cccc'
            else:
                button_field[i][j]['bg'] = '#11ed27'
    if check == False:
        return
    congrat_lbl['text'] = "Поздравляем!!! Ваш счёт: " + str(score[0])
    congrat_lbl.grid(row = size[0] + 1, column = 0, columnspan = size[0])   

def MoveUp(event):
    if curr_pos[0] == size[0] - 1:
        return
    button_field[curr_pos[0]][curr_pos[1]]['text'], button_field[curr_pos[0] + 1][curr_pos[1]]['text'] = button_field[curr_pos[0] + 1][curr_pos[1]]['text'], button_field[curr_pos[0]][curr_pos[1]]['text']
    curr_pos[0] += 1;
    score[0] += 1
    Check()

def MoveLeft(event):
    if curr_pos[1] == size[0] - 1:
        return
    button_field[curr_pos[0]][curr_pos[1]]['text'], button_field[curr_pos[0]][curr_pos[1] + 1]['text'] = button_field[curr_pos[0]][curr_pos[1] + 1]['text'], button_field[curr_pos[0]][curr_pos[1]]['text']
    curr_pos[1] += 1;
    score[0] += 1
    Check()

def MoveRight(event):
    if curr_pos[1] == 0:
        return
    button_field[curr_pos[0]][curr_pos[1]]['text'], button_field[curr_pos[0]][curr_pos[1] - 1]['text'] = button_field[curr_pos[0]][curr_pos[1] - 1]['text'], button_field[curr_pos[0]][curr_pos[1]]['text']
    curr_pos[1] -= 1;
    score[0] += 1
    Check()

def MoveDown(event):
    if curr_pos[0] == 0:
        return
    button_field[curr_pos[0]][curr_pos[1]]['text'], button_field[curr_pos[0] - 1][curr_pos[1]]['text'] = button_field[curr_pos[0] - 1][curr_pos[1]]['text'], button_field[curr_pos[0]][curr_pos[1]]['text']
    curr_pos[0] -= 1;
    score[0] += 1
    Check()

def Init(event):
    size[0] = int(combo.get())
    lbl.destroy()
    combo.destroy()
    button.destroy()
    for i in range(size[0]):
        field.append([])
        button_field.append([])
    for i in range(size[0]):
        field[0].append(i + 1)
        button_field[0].append(Button(window, text=str(i + 1), height = "2", width = "5", font="Arial 20", bg = '#e3cccc', state="disabled"))
        button_field[0][i].grid(column = i, row=0)
    for i in range(size[0] - 1):
        for j in range(size[0]):
            field[i + 1].append(field[i][j] + size[0])
            button_field[i + 1].append(Button(window, text=str(field[i + 1][j]), height = "2", width = "5", font="Arial 20", bg = '#e3cccc', state="disabled"))
            button_field[i + 1][j].grid(column = j, row=i + 1)
    button_field[size[0] - 1][size[0] - 1]['text'] = "*"
    field[size[0] - 1][size[0] - 1] = "*"
    curr_pos[0] = size[0] - 1;
    curr_pos[1] = size[0] - 1;

    string = str(size[0] * 100 + 30)
    string += "x" + string
    window.geometry(string)
    shuffle_button.grid(row = size[0], column = 0, columnspan = size[0])
    Shuffle(event)
    Check()
    return

def Shuffle(event):
    for i in range(size[0] * 100):
        choice = random.choice([1, 2, 3, 4])
        if choice == 1:
            MoveUp(event)
        if choice == 2:
            MoveDown(event)
        if choice == 3:
            MoveLeft(event)
        if choice == 4:
            MoveRight(event)
        score[0] = 0    
    congrat_lbl.grid_remove()

random.seed()
button_field = []
field = []
size = [0]
curr_pos = [0, 0]
score = [0]
window = Tk()
window.title("Пятнашки")
window.geometry('500x150')
congrat_lbl = Label(window, font="Arial 10")

lbl = Label(window, text="Выберите размер поля")
lbl.grid(column = 0, row = 0)
combo = Combobox(window)
combo.grid(column=1, row=0)
combo['values'] = (3, 4, 5, 6)
combo.current(1)
button = Button(window, text="Выбрать")
button.grid(column=3, row=0)
button.bind("<Button-1>", Init)
shuffle_button = Button(window, text="Перемешать")
shuffle_button.bind("<Button-1>", Shuffle)
window.bind("<w>", MoveUp)
window.bind("<s>", MoveDown)
window.bind("<a>", MoveLeft)
window.bind("<d>", MoveRight)
window.mainloop()
