import tkinter as tk

root = tk.Tk()
root.title("ADebit")
root.geometry("500x400")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Доходы", width=15).grid(row=0, column=0, padx=5)
tk.Label(frame_top, text="Расходы", width=15).grid(row=0, column=1, padx=5)
tk.Label(frame_top, text="Баланс", width=15).grid(row=0, column=2, padx=5)

# ПОЛЕ С НАДПИСЬЮ "Привет введи команду"
label_command = tk.Label(root, text="Привет введи команду")
label_command.pack(pady=10)

# Список команд (пример)
menu_text = """1. Добавить доход
2. Добавить расход
3. Показать баланс
4. Выход"""

tk.Label(root, text=menu_text).pack()

# Поле ввода команды
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Кнопка "Применить"
button = tk.Button(root, text="Применить")
button.pack(pady=10)

# Запуск главного цикла
root.mainloop()

# Задачи грядущего захода - меню по примеру учителя, работа с полем ввода - нужно сохранять доходы и расходы в файл.csv