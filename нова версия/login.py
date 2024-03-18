from tkinter import *
from tkinter import ttk
import menu as menu
from tkinter import messagebox

# login

# style = ttk.Style()
# style.configure("styleFrame", background="white", width=1280, height=720)


def login(rootWindow):
    # login = ttk.Frame(rootWindow, style="styleFrame")
    c = Canvas(rootWindow, width=1280, height=720, bg='white')
    c.place()
    topic = Label(
            rootWindow,
            text='Регистрация', 
            font=('Roboto', 32, 'bold'),
            foreground='#0047AB',
            background='#fdfdfd'
        )
    topic.place(relx=.5, y=195, anchor='n');

    emailLabel = Label(
            rootWindow,
            text='Почта', 
            font=('Roboto', 16, 'bold'),
            background='#fdfdfd'
        )
    emailLabel.place(relx=.5, y=265, anchor='n');

    email = Entry(
            rootWindow,
            border=5, 
            background='#fdfdfd', 
            font=('Roboto', 16), 
        )
    email.place(relx=.5, y=295, anchor='n');

    passwordLabel = Label(
            rootWindow,
            text='Пароль', 
            font=('Roboto', 16, 'bold'),
            background='#fdfdfd'
        )
    passwordLabel.place(relx=.5, y=355, anchor='n');

    password = Entry(
            rootWindow,
            border=5, 
            background='#fdfdfd', 
            font=('Roboto', 16), 
        )
    password.place(relx=.5, y=385, anchor='n');

    register = Button(
            rootWindow,
            text='Зарегистрироваться', 
            font=('Roboto', 16, 'bold'),
            foreground='#fdfdfd',
            background='#0047AB',
            width=20,
            height=2, 
            cursor='hand2',
            command=lambda: erase(rootWindow, listOfElements)
            # command=lambda: menu.menu(rootWindow)
        )
    register.place(relx=.5, y=445, anchor='n');

    listOfElements = [topic, emailLabel, email, passwordLabel, password, register, c]

def validate(email_value, password_value, rootWindow):
    isVal = False
    if email_value == 'admin@example.com' and password_value == 'admin':
        isVal= True
        return isVal
    else:
        messagebox.showerror("Login Failed", "Invalid email or password");
        return

def erase(rootWindow, listOfElements):
    if validate(listOfElements[2].get(), listOfElements[4].get(), rootWindow):
        for element in listOfElements:
            element.place_forget()
        menu.menu(rootWindow)


