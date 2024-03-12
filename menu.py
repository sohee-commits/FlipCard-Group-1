from tkinter import *
from PIL import Image, ImageTk
import cards_js
import cards_py
import login 
import about

def openMenu():    
    menu = Toplevel()
    menu.title('FlipCard')
    menu.geometry('1280x720')
    menu.configure(background='#fdfdfd')

    about_program = Button(
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
    about_program.place(relx=.27, y=30, anchor='n');

    topics = Button(
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
    topics.place(relx=.5, y=30, anchor='n');

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

    topics_text = Label(
        menu,
        text='Темы', 
        font=('Roboto', 32, 'bold'),
        foreground='#0047AB',
        background='#fdfdfd'
    )
    topics_text.place(relx=.5, y=100, anchor='n');

    url_js='assets/javascript 1.png'
    url_py='assets/python 1.png'

    # Использование PIL для загрузки изображений
    img_js = Image.open(url_js)
    img_py = Image.open(url_py)

    # Преобразование изображений в формат, подходящий для Tkinter
    img_js = ImageTk.PhotoImage(img_js)
    img_py = ImageTk.PhotoImage(img_py)

    py_topic = Button(
        menu,
        image=img_py,
        compound=LEFT,
        text='Python', 
        font=('Roboto', 24, 'bold'),
        foreground='#000000',
        background='#FFFFFF',
        cursor='hand2',
        borderwidth=0,
        command=cards_py.openCards
    )
    py_topic.image = img_py # Сохранение ссылки на изображение
    py_topic.place(relx=.48, y=175, anchor='n');

    js_topic = Button(
        menu,
        image=img_js,
        compound=LEFT,
        text='JavaScript', 
        font=('Roboto', 24, 'bold'),
        foreground='#000000',
        background='#FFFFFF',
        cursor='hand2',
        borderwidth=0,
        command=cards_js.openCards
    )
    js_topic.image = img_js # Сохранение ссылки на изображение
    js_topic.place(relx=.5, y=225, anchor='n');

    menu.mainloop()
