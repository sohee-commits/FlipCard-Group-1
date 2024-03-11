from tkinter import *
from tkinter import ttk
import cards_nd 
import login 
import menu 
import about 

# cards without database
def openCardsND():
    # define cards_no_db window and options
    cards_no_db = Toplevel();
    cards_no_db.title('FlipCard');
    cards_no_db.iconbitmap(default='assets/cards.ico');
    cards_no_db.geometry('1280x720');
    cards_no_db.configure(background='#fdfdfd');

    about = Button(
        cards_no_db,
        text='О программе', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=about.openAbout
    ).place(relx=.27, y=30, anchor='n');

    topics = Button(
        cards_no_db,
        text='Темы', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=menu.openMenu
    ).place(relx=.5, y=30, anchor='n');

    logout = Button(
        cards_no_db,
        text='Выйти', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#aaaaaa',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=login.openLogin
    ).place(relx=.73, y=30, anchor='n');

    theme = Label(
        cards_no_db,
        text='Тема', 
        font=('Roboto', 32, 'bold'),
        foreground='#0047AB',
        background='#fdfdfd'
    ).place(relx=.5, y=100, anchor='n');

    question_txt = 'Важный вопрос';
    answer_txt = 'Полезный ответ';

    def create_label(parent, text, x, y):
        return Label(
            parent,
            text=text,
            font=('Roboto', 16),
            background='#fdfdfd',
            width=38,
            height=4,
            border=2, 
            relief='solid'
        ).place(relx=x, y=y, anchor='n');

    create_label(cards_no_db, question_txt, .3, 200);
    create_label(cards_no_db, answer_txt, .7, 200);
    create_label(cards_no_db, question_txt, .3, 340);
    create_label(cards_no_db, answer_txt, .7, 340);
    create_label(cards_no_db, question_txt, .3, 480);
    create_label(cards_no_db, answer_txt, .7, 480);

    cards_no_db.mainloop();
