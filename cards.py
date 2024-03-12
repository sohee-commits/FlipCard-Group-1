from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import menu
import login 
import about 

def openCards():
    cards = Toplevel()
    cards.title('FlipCard')
    cards.geometry('1280x720')
    cards.configure(background='#fdfdfd')

    o_program = Button(
        cards,
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
        cards,
        text='Темы', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=menu.openMenu
    )
    themes.place(relx=.5, y=30, anchor='n');

    logout = Button(
        cards,
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
        cards,
        text='Тема', 
        font=('Roboto', 32, 'bold'),
        foreground='#0047AB',
        background='#fdfdfd'
    )
    themes_text.place(relx=.5, y=100, anchor='n');

    vopros_text = Label(
        cards,
        text='Вопрос', 
        font=('Roboto', 18, 'normal'),
        foreground='#111111',
        background='#fdfdfd'
    )
    vopros_text.place(relx=.3, y=180, anchor='n');

    otvet_text = Label(
        cards,
        text='Ответ', 
        font=('Roboto', 18, 'normal'),
        foreground='#111111',
        background='#fdfdfd'
    )
    otvet_text.place(relx=.7, y=180, anchor='n');

    vopros = Entry(
        cards,
        width=55,
    )
    vopros.place(relx=.3, y=260, anchor='n');

    vopros = Entry(
        cards,
        width=55,
    ).place(relx=.7, y=260, anchor='n');

    new_card = Button(
        cards,
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
        cards,
        compound=LEFT,
        width=35,
        height=3,
        text='Важный вопрос', 
        font=('Roboto', 18, 'normal'),
        foreground='#111111',
        background='#e8e8e8',
        cursor='hand2',
        borderwidth=0,
    ).place(relx=.3, y=480, anchor='n');

    vopros_2 = Button(
        cards,
        compound=LEFT,
        width=35,
        height=3,
        text='Важный вопрос', 
        font=('Roboto', 18, 'normal'),
        foreground='#111111',
        background='#e8e8e8',
        cursor='hand2',
        borderwidth=0,
    ).place(relx=.3, y=600, anchor='n');

    otvet_1 = Button(
        cards,
        compound=LEFT,
        width=35,
        height=3,
        text='Полезный ответ', 
        font=('Roboto', 17, 'bold'),
        foreground='#111111',
        background='#e8e8e8',
        cursor='hand2',
        borderwidth=0,
    ).place(relx=.7, y=480, anchor='n');

    otvet_2 = Button(
        cards,
        compound=LEFT,
        width=35,
        height=3,
        text='Полезный ответ', 
        font=('Roboto', 17, 'bold'),
        foreground='#111111',
        background='#e8e8e8',
        cursor='hand2',
        borderwidth=0,
    ).place(relx=.7, y=600, anchor='n');

    cards.mainloop()
