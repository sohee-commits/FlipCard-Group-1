from tkinter import *
from tkinter import ttk

import login as login
import main as main
import about as about
import menu as menu

def about(rootWindow):
    # header
    about_program = Button(
          rootWindow,
        text='О программе', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=None
    )
    about_program.place(relx=.27, y=30, anchor='n');

    topics = Button(
          rootWindow,
        text='Темы', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=lambda: eraseMenu(rootWindow, listOfElements)
    )
    topics.place(relx=.5, y=30, anchor='n');

    logout = Button(
          rootWindow,
        text='Выйти', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#AAAAAA',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=lambda: eraseLogin(rootWindow, listOfElements)
    )
    logout.place(relx=.73, y=30, anchor='n');

    topic = Label(
          rootWindow,
        text='О программе', 
        font=('Roboto', 32, 'bold'),
        foreground='#0047AB',
        background='#fdfdfd'
    )
    topic.place(relx=.5, y=235, anchor='n');

    text1 = Label(
          rootWindow,
        text='FlipCard - приложение для обучения с использованием карточек с вопросами и ответами.', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    text1.place(relx=.5, y=310, anchor='n');

    devs = Label(
          rootWindow,
        text='Разработчики:', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    devs.place(relx=.5, y=335, anchor='n');

    dev_1 = Label(
          rootWindow,
        text=' - Черепанова Софья Юрьевна', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    dev_1.place(relx=.5, y=360, anchor='n');

    dev_2 = Label(
          rootWindow,
        text=' - Ипанова Дарья Александровна', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    dev_2.place(relx=.5, y=385, anchor='n');

    text5 = Label(
          rootWindow,
        text=' - Беляева Ксения Евгеньевна', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    text5.place(relx=.5, y=410, anchor='n');

    dev_3 = Label(
          rootWindow,
        text=' - Селина Дарина Сергеевна', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    dev_3.place(relx=.5, y=435, anchor='n');

    group = Label(
          rootWindow,
        text=' группа 1-ИС, 3 курс, 09.02.07 Информационные системы и програиммирование', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    group.place(relx=.5, y=460, anchor='n');

    study = Button(
          rootWindow,
        text='Учиться', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=2, 
        cursor='hand2',
        command=lambda: eraseMenu(rootWindow, listOfElements)
    )
    study.place(relx=.5, y=510, anchor='n');

    logout_2 = Button(
          rootWindow,
        text='Выйти', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#6689BD',
        width=20,
        height=2, 
        cursor='hand2',
        command=lambda: eraseLogin(rootWindow, listOfElements)
    )
    logout_2.place(relx=.5, y=580, anchor='n');

    listOfElements = [about_program, topics, logout, logout_2, topic, text1, dev_1, dev_2, dev_3, devs, study, group, text5]

def eraseLogin(rootWindow, listOfElements):
    login.login(rootWindow)
    for element in listOfElements:
        element.place_forget()

def eraseMenu(rootWindow, listOfElements):
    menu.menu(rootWindow)
    for element in listOfElements:
        element.place_forget()

def eraseAbout(rootWindow, listOfElements):
    about.about()
    for element in listOfElements:
        element.place_forget()