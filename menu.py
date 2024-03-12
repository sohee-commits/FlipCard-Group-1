from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cards
import login 
import about 

def openMenu():    
    menu = Toplevel()
    menu.title('FlipCard')
    menu.geometry('1280x720')
    menu.configure(background='#fdfdfd')

    o_program = Button(
        menu,
        text='О программе', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=about.openAbout
    )
    o_program.place(relx=.27, y=30, anchor='n');

    themes = Button(
        menu,
        text='Темы', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=None
    )
    themes.place(relx=.5, y=30, anchor='n');

    logout = Button(
        menu,
        text='Выйти', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#AAAAAA',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=login.openLogin
    )
    logout.place(relx=.73, y=30, anchor='n');

    themes_text = Label(
        menu,
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
        menu,
        image=img_py,
        compound=LEFT,
        text='Python', 
        font=('Roboto', 24, 'bold'),
        foreground='#000000',
        background='#FFFFFF',
        cursor='hand2',
        borderwidth=0,
        command=cards.openCards
    )
    py_theme.image = img_py # Сохранение ссылки на изображение
    py_theme.place(relx=.48, y=175, anchor='n');

    js_theme = Button(
        menu,
        image=img_js,
        compound=LEFT,
        text='JavaScript', 
        font=('Roboto', 24, 'bold'),
        foreground='#000000',
        background='#FFFFFF',
        cursor='hand2',
        borderwidth=0,
        command=cards.openCards
    )
    js_theme.image = img_js # Сохранение ссылки на изображение
    js_theme.place(relx=.5, y=225, anchor='n');

    menu.mainloop()