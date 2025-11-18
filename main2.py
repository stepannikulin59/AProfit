from tkinter import *

def _click(color):
    lab1['bg'] = color

def set_lab1():
    text = name.get()
    lab1['text'] = text

def clear():
    name.delete(0, 'end')

root = Tk()
root.geometry('400x400')
root.title('Моё первое окно')
root.resizable(width=False, height=False)
root.config(bg='#B0E0E6')

font_ = 'Arial 23'

lab1 = Label(
    root,
    text='1',
    bg='yellow',
    font=font_
)
lab1.grid(column=1, row=1, columnspan=2)

but1 = Button(root, text='Зелёный', font=font_, fg='#4B0082', bd=10,
              command=lambda: _click('green'))
but1.grid(row=2, column=1)

but2 = Button(root, text='Красный', font=font_, fg='#4B0082', bd=10,
              command=lambda: _click('red'))
but2.grid(row=2, column=2)

name = Entry(root, font=font_)
name.grid(row=3, column=1, columnspan=2)

but3 = Button(root, text='Отправить', font=font_, fg='#4B0082', bd=10,
              command=set_lab1)
but3.grid(row=4, column=1)

but4 = Button(root, text='Clear', font=font_, fg='#4B0082', bd=10,
              command=clear)
but4.grid(row=4, column=2)

root.mainloop()

# https://habr.com/ru/companies/piter/articles/674234/ Лямбда-функция в Python простыми словами