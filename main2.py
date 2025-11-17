from tkinter import *

def _click(color):
    lab1['bg'] = color

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
lab1.grid(column=1, row=1)

but = Button(
    root,
    text='Зелёный',
    font=font_,
    fg='#4B0082',
    bd=10,
    command=lambda: _click('green')
)
but.grid(row=2, column=1)

but2 = Button(
    root,
    text='Красный',
    font=font_,
    fg='#4B0082',
    bd=10,
    command=lambda: _click('red')
)
but2.grid(row=2, column=2)

root.mainloop()