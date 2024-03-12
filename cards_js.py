from tkinter import *
import menu
import login 
import about

def openCards():
    cards = Toplevel();
    cards.title('FlipCard');
    cards.geometry('1280x720');
    cards.configure(background='#fdfdfd');

    about_program = Button(
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
    about_program.place(relx=.27, y=30, anchor='n');

    topics = Button(
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
    topics.place(relx=.5, y=30, anchor='n');

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

    topics_text = Label(
        cards,
        text='Тема', 
        font=('Roboto', 32, 'bold'),
        foreground='#0047AB',
        background='#fdfdfd'
    )
    topics_text.place(relx=.5, y=100, anchor='n');

    question_text = Label(
        cards,
        text='Вопрос', 
        font=('Roboto', 18, 'normal'),
        foreground='#111111',
        background='#fdfdfd'
    )
    question_text.place(relx=.3, y=180, anchor='n');

    answer_text = Label(
        cards,
        text='Ответ', 
        font=('Roboto', 18, 'normal'),
        foreground='#111111',
        background='#fdfdfd'
    )
    answer_text.place(relx=.7, y=180, anchor='n');

    question = Entry(
        cards,
        border=5, 
        width=55,
    )
    question.place(relx=.3, y=260, anchor='n');

    question = Entry(
        cards,
        border=5, 
        width=55,
    ).place(relx=.7, y=260, anchor='n');

    new_card = Button(
        cards,
        compound=LEFT,
        width=70,
        height=2, 
        text='Добавить карточку', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        cursor='hand2',
        borderwidth=0,
    )
    new_card.place(relx=.5, y=380, anchor='n');

    question_1 = Button(
        cards,
        compound=LEFT,
        width=35,
        height=3,
        text='Как написать однострочный комментарий?', 
        wraplength=300,
        font=('Roboto', 16, 'normal'),
        foreground='#111111',
        background='#e8e8e8',
        cursor='hand2',
        borderwidth=0,
    )
    question_1.place(relx=.3, y=480, anchor='n');

    question_2 = Button(
        cards,
        compound=LEFT,
        width=35,
        height=3,
        text='Как объявить переменную?', 
        wraplength=300,
        font=('Roboto', 16, 'normal'),
        foreground='#111111',
        background='#e8e8e8',
        cursor='hand2',
        borderwidth=0,
    )
    question_2.place(relx=.3, y=600, anchor='n');

    answer_1 = Button(
        cards,
        compound=LEFT,
        width=35,
        height=4,
        text='Часть строки после // считается комментарием. Такой комментарий может как занимать строку целиком, так и находиться после инструкции.', 
        wraplength=300,
        font=('Roboto', 12, 'bold'),
        foreground='#111111',
        background='#e8e8e8',
        cursor='hand2',
        borderwidth=0,
    )
    answer_1.place(relx=.7, y=480, anchor='n');

    answer_2 = Button(
        cards,
        compound=LEFT,
        width=35,
        height=4,
        text='Приведённая инструкция создаёт (другими словами, объявляет) переменную с именем «message»: let message;', 
        wraplength=300,
        font=('Roboto', 12, 'bold'),
        foreground='#111111',
        background='#e8e8e8',
        cursor='hand2',
        borderwidth=0,
    )
    answer_2.place(relx=.7, y=600, anchor='n');

    cards.mainloop();
