from ttkbootstrap.widgets import Entry, Checkbutton, Button
import ttkbootstrap as ttk

from checker.checkpass import check_password_strength

def check_pass():
    try:
        pwd = password_entry.get()
        res = check_password_strength(pwd)
        result_check.set(res)
    except ValueError as e:
        ttk.dialogs.Messagebox.show_error(str(e), "Ошибка")
        
app = ttk.Window(themename="flatly")
app.title("Passcheck")
app.geometry("400x190")

ttk.Label(app, text="Введите пароль:").pack(pady=10)
password_entry = Entry(app)
password_entry.pack()

Button(app, text="Проверка", command=check_pass, bootstyle="success").pack(pady=10)

result_check = ttk.StringVar()
ttk.Label(app, textvariable=result_check, width=15).pack(pady=5)

app.mainloop()