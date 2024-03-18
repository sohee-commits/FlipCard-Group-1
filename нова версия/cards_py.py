from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import login as login
import main as main
import about as about
import menu as menu
import cards_js as cards_js

def cards_py(rootWindow):
    c = Canvas(rootWindow, width=1280, height=720, bg='white')
    c.place()
    o_program = Button(
            rootWindow,
            text='О программе', 
            font=('Roboto', 16, 'bold'),
            foreground='#fdfdfd',
            background='#0047AB',
            width=20,
            height=1, 
            cursor='hand2',
            borderwidth=0,
            command=lambda: eraseAbout(rootWindow, listOfElements)
        )
    o_program.place(relx=.27, y=30, anchor='n');

    themes = Button(
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
    themes.place(relx=.5, y=30, anchor='n');

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

    themes_text = Label(
            rootWindow,
            text='Тема', 
            font=('Roboto', 32, 'bold'),
            foreground='#0047AB',
            background='#fdfdfd'
        )
    themes_text.place(relx=.5, y=100, anchor='n');

    vopros_text = Label(
            rootWindow,
            text='Вопрос', 
            font=('Roboto', 18, 'normal'),
            foreground='#111111',
            background='#fdfdfd'
        )
    vopros_text.place(relx=.3, y=180, anchor='n');

    otvet_text = Label(
            rootWindow,
            text='Ответ', 
            font=('Roboto', 18, 'normal'),
            foreground='#111111',
            background='#fdfdfd'
        )
    otvet_text.place(relx=.7, y=180, anchor='n');

    vopros = Entry(
            rootWindow,
            width=55,
        )
    vopros.place(relx=.3, y=260, anchor='n');

    vopros1 = Entry(
            rootWindow,
            width=55,
        )
    vopros1.place(relx=.7, y=260, anchor='n');

    new_card = Button(
            rootWindow,
            compound=LEFT,
            width=58,
            text='Добавить карточку', 
            font=('Roboto', 24, 'bold'),
            foreground='#fdfdfd',
            background='#0047AB',
            cursor='hand2',
            borderwidth=0,
        )
    new_card.place(relx=.5, y=380, anchor='n');

    vopros_1 = Button(
            rootWindow,
            compound=LEFT,
            width=35,
            height=3,
            text='Важный вопрос', 
            font=('Roboto', 18, 'normal'),
            foreground='#111111',
            background='#e8e8e8',
            cursor='hand2',
            borderwidth=0,
        )
    vopros_1.place(relx=.3, y=480, anchor='n');

    vopros_2 = Button(
            rootWindow,
            compound=LEFT,
            width=35,
            height=3,
            text='Важный вопрос', 
            font=('Roboto', 18, 'normal'),
            foreground='#111111',
            background='#e8e8e8',
            cursor='hand2',
            borderwidth=0,
        )
    vopros_2.place(relx=.3, y=600, anchor='n');

    otvet_1 = Button(
            rootWindow,
            compound=LEFT,
            width=35,
            height=3,
            text='Полезный ответ', 
            font=('Roboto', 17, 'bold'),
            foreground='#111111',
            background='#e8e8e8',
            cursor='hand2',
            borderwidth=0,
        )
    otvet_1.place(relx=.7, y=480, anchor='n');

    otvet_2 = Button(
            rootWindow,
            compound=LEFT,
            width=35,
            height=3,
            text='Полезный ответ', 
            font=('Roboto', 17, 'bold'),
            foreground='#111111',
            background='#e8e8e8',
            cursor='hand2',
            borderwidth=0,
        )
    otvet_2.place(relx=.7, y=600, anchor='n');

    listOfElements = [o_program, otvet_1, otvet_2, vopros_1, vopros_2, vopros1, vopros_text, vopros, new_card, themes, themes_text, logout, otvet_text, c]

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