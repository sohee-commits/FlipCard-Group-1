from tkinter import *
from tkinter import ttk
import cards_nd 
import login 
import menu 
import about 

# login
def openLogin():
    login = Toplevel();
    login.title('FlipCard');
    login.iconbitmap(default='assets/cards.ico');
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
        command=menu.openMenu
    ).place(relx=.5, y=445, anchor='n');
