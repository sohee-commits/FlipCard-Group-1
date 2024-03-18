from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import login as login
import main as main
import about as about
import cards_js as cards_js
import cards_py as cards_py

def menu(rootWindow):
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
            text='Темы', 
            font=('Roboto', 32, 'bold'),
            foreground='#0047AB',
            background='#fdfdfd'
        )
    themes_text.place(relx=.5, y=100, anchor='n');

    url_js='assets/javascript 1.png'
    url_py='assets/python 1.png'

        # Использование PIL для загрузки изображений
    img_js = Image.open(url_js)
    img_py = Image.open(url_py)

        # Преобразование изображений в формат, подходящий для Tkinter
    img_js = ImageTk.PhotoImage(img_js)
    img_py = ImageTk.PhotoImage(img_py)

    py_theme = Button(
              rootWindow,
            image=img_py,
            compound=LEFT,
            text='Python', 
            font=('Roboto', 24, 'bold'),
            foreground='#000000',
            background='#FFFFFF',
            cursor='hand2',
            borderwidth=0,
            command=lambda: eraseCards_py(rootWindow, listOfElements)
        )
    py_theme.image = img_py # Сохранение ссылки на изображение
    py_theme.place(relx=.48, y=175, anchor='n');

    js_theme = Button(
              rootWindow,
            image=img_js,
            compound=LEFT,
            text='JavaScript', 
            font=('Roboto', 24, 'bold'),
            foreground='#000000',
            background='#FFFFFF',
            cursor='hand2',
            borderwidth=0,
            command=lambda: eraseCards_js(rootWindow, listOfElements)
        )
    js_theme.image = img_js # Сохранение ссылки на изображение
    js_theme.place(relx=.5, y=225, anchor='n');

    listOfElements =[o_program, themes, themes_text, logout, js_theme, py_theme, c]

def eraseLogin(rootWindow, listOfElements):
    login.login(rootWindow)
    for element in listOfElements:
        element.place_forget()

def eraseCards_js(rootWindow, listOfElements):
    cards_js.cards_js(rootWindow)
    for element in listOfElements:
        element.place_forget()

def eraseCards_py(rootWindow, listOfElements):
    cards_py.cards_py(rootWindow)
    for element in listOfElements:
        element.place_forget()

def eraseAbout(rootWindow, listOfElements):
    about.about(rootWindow)
    for element in listOfElements:
        element.place_forget()