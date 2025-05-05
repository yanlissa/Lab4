from ttkbootstrap import Window
from tkinter import BooleanVar, StringVar
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.widgets import Entry, Checkbutton, Button, Label, Notebook, Frame
import pyperclip

from checker.checkpass import check_password_strength
from generator.genpass import generate_password

def check_pass():
    try:
        pwd = password_entry.get()
        res = check_password_strength(pwd)
        result_check.set(res)
    except ValueError as e:
        Messagebox.show_error(str(e), "Ошибка")

def generate():
    try:
        length = int(length_entry.get())
        if length < 1 or length > 25:
            raise ValueError("Неверная длина")

        pwd = generate_password(
            length,
            upper_var.get(),
            lower_var.get(),
            digits_var.get(),
            symbols_var.get()
        )
        result_var.set(pwd)
    except ValueError as e:
        msg = str(e)
        if msg == "Нужно выбрать хотя бы один тип символов":
            Messagebox.show_error(msg, "Ошибка")
        elif msg == "Неверная длина":
            Messagebox.show_error("Введите длину пароля от 1 до 25", "Ошибка")
        else:
            Messagebox.show_error("Проверьте введённые данные", "Ошибка")
        
def copy_to_clipboard():
    pwd = result_var.get()
    if pwd:
        pyperclip.copy(pwd)
        Messagebox.show_info("Скопировано", "Пароль скопирован в буфер обмена")

app = Window(themename="flatly")
app.title("Passcheck")
app.geometry("420x380")

notebook = Notebook(app)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

gen_frame = Frame(notebook)
notebook.add(gen_frame, text="Passwork")

Label(gen_frame, text="Длина пароля:").pack(pady=10)
length_entry = Entry(gen_frame)
length_entry.pack()

upper_var = BooleanVar(value=False)
lower_var = BooleanVar(value=False)
digits_var = BooleanVar(value=False)
symbols_var = BooleanVar(value=False)

Checkbutton(gen_frame, text="Заглавные буквы", variable=upper_var).pack(anchor='w', padx=20)
Checkbutton(gen_frame, text="Строчные буквы", variable=lower_var).pack(anchor='w', padx=20)
Checkbutton(gen_frame, text="Цифры", variable=digits_var).pack(anchor='w', padx=20)
Checkbutton(gen_frame, text="Символы", variable=symbols_var).pack(anchor='w', padx=20)

Button(gen_frame, text="Сгенерировать", command=generate, bootstyle="success").pack(pady=10)

result_var = StringVar()
Entry(gen_frame, textvariable=result_var, width=30).pack(pady=5)

Button(gen_frame, text="Скопировать", command=copy_to_clipboard, bootstyle="secondary").pack(pady=5)

check_frame = Frame(notebook)
notebook.add(check_frame, text="Passcheck")

Label(check_frame, text="Введите пароль:").pack(pady=10)
password_entry = Entry(check_frame)
password_entry.pack()

Button(check_frame, text="Проверка", command=check_pass, bootstyle="success").pack(pady=10)

result_check = StringVar()
Label(check_frame, textvariable=result_check, width=15).pack(pady=5)

app.mainloop()