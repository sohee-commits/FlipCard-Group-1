from tkinter import *
from tkinter import ttk

# login
def openLogin():
    login = Tk();
    login.title('FlipCard');
    login.geometry('1280x720');
    login.configure(background='#fdfdfd');

    topic = Label(
        login,
        text='Регистрация', 
        font=('Roboto', 32, 'bold'),
        foreground='#0047AB',
        background='#fdfdfd'
    ).place(relx=.5, y=195, anchor='n');

    emailLabel = Label(
        login,
        text='Почта', 
        font=('Roboto', 16, 'bold'),
        background='#fdfdfd'
    ).place(relx=.5, y=265, anchor='n');

    email = Entry(
        login,
        border=5, 
        background='#fdfdfd', 
        font=('Roboto', 16), 
    ).place(relx=.5, y=295, anchor='n');

    passwordLabel = Label(
        login,
        text='Пароль', 
        font=('Roboto', 16, 'bold'),
        background='#fdfdfd'
    ).place(relx=.5, y=355, anchor='n');

    password = Entry(
        login,
        border=5, 
        background='#fdfdfd', 
        font=('Roboto', 16), 
    ).place(relx=.5, y=385, anchor='n');

    register = Button(
        login,
        text='Зарегистрироваться', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=2, 
        cursor='hand2',
        command=openMenu
    ).place(relx=.5, y=445, anchor='n');

# menu
def openMenu():
    menu = Tk();
    menu.title('FlipCard');
    menu.geometry('1280x720');
    menu.configure(background='#fdfdfd');

# root
# define root window and options
root = Tk();
root.title('FlipCard');
root.iconbitmap(default='assets/cards.ico');
root.geometry('1280x720');
root.configure(background='#fdfdfd');

# root widgets
logo = Label(
    text='FlipCard', 
    font=('Roboto', 48, 'bold'),
    foreground='#0047AB',
    background='#fdfdfd'
).place(relx=.5, y=235, anchor='n');

description = Label(
    text='Сервис для запоминания информации с помощью карточек', 
    font=('Roboto', 16),
    background='#fdfdfd'
).place(relx=.5, y=335, anchor='n');

register = Button(
    text='Зарегистрироваться', 
    font=('Roboto', 16, 'bold'),
    foreground='#fdfdfd',
    background='#0047AB',
    width=20,
    height=2, 
    cursor='hand2',
    command=openLogin
).place(relx=.5, y=435, anchor='n');

# loop windows
root.mainloop();
