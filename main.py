from ttkbootstrap.widgets import Entry, Checkbutton, Button
import ttkbootstrap as ttk
import pyperclip

from generator.genpass import generate_password

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
            ttk.dialogs.Messagebox.show_error(msg, "Ошибка")
        elif msg == "Неверная длина":
            ttk.dialogs.Messagebox.show_error("Введите длину пароля от 1 до 25", "Ошибка")
        else:
            ttk.dialogs.Messagebox.show_error("Проверьте введённые данные", "Ошибка")
        
def copy_to_clipboard():
    pwd = result_var.get()
    if pwd:
        pyperclip.copy(pwd)
        ttk.dialogs.Messagebox.show_info("Скопировано", "Пароль скопирован в буфер обмена")


app = ttk.Window(themename="flatly")
app.title("Passwork")
app.geometry("400x300")

ttk.Label(app, text="Длина пароля:").pack(pady=10)
length_entry = Entry(app)
length_entry.pack()

upper_var = ttk.BooleanVar(value=False)
lower_var = ttk.BooleanVar(value=False)
digits_var = ttk.BooleanVar(value=False)
symbols_var = ttk.BooleanVar(value=False)

Checkbutton(app, text="Заглавные буквы", variable=upper_var).pack(anchor='w', padx=20)
Checkbutton(app, text="Строчные буквы", variable=lower_var).pack(anchor='w', padx=20)
Checkbutton(app, text="Цифры", variable=digits_var).pack(anchor='w', padx=20)
Checkbutton(app, text="Символы", variable=symbols_var).pack(anchor='w', padx=20)

Button(app, text="Сгенерировать", command=generate, bootstyle="success").pack(pady=10)

result_var = ttk.StringVar()
Entry(app, textvariable=result_var, width=30).pack(pady=5)

Button(app, text="Скопировать", command=copy_to_clipboard, bootstyle="secondary").pack(pady=5)

app.mainloop()