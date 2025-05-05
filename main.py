import tkinter as tk
from tkinter import messagebox
import pyperclip

from generator.genpass import generate_password

def generate():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError

        pwd = generate_password(
            length,
            upper_var.get(),
            lower_var.get(),
            digits_var.get(),
            symbols_var.get()
        )
        result_var.set(pwd)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректную длину (целое число > 0)")

def copy_to_clipboard():
    pwd = result_var.get()
    if pwd:
        pyperclip.copy(pwd)
        messagebox.showinfo("Скопировано", "Пароль скопирован в буфер обмена")


root = tk.Tk()
root.title("Генератор паролей")

tk.Label(root, text="Длина пароля:").grid(row=0, column=0, sticky='w')
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Заглавные буквы", variable=upper_var).grid(row=1, column=0, sticky='w')
tk.Checkbutton(root, text="Строчные буквы", variable=lower_var).grid(row=1, column=1, sticky='w')
tk.Checkbutton(root, text="Цифры", variable=digits_var).grid(row=2, column=0, sticky='w')
tk.Checkbutton(root, text="Символы", variable=symbols_var).grid(row=2, column=1, sticky='w')

tk.Button(root, text="Сгенерировать", command=generate).grid(row=3, column=0, columnspan=2, pady=5)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=40).grid(row=4, column=0, columnspan=2)

tk.Button(root, text="Скопировать", command=copy_to_clipboard).grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()