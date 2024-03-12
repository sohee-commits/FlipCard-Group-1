from tkinter import *
import login 
import menu 

def openAbout():
    about = Toplevel();
    about.title('FlipCard');
    about.iconbitmap(default='assets/cards.ico');
    about.geometry('1280x720');
    about.configure(background='#fdfdfd');
    
    # header
    about_program = Button(
        about,
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
        about,
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
        about,
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

    topic = Label(
        about,
        text='О программе', 
        font=('Roboto', 32, 'bold'),
        foreground='#0047AB',
        background='#fdfdfd'
    )
    topic.place(relx=.5, y=235, anchor='n');

    text1 = Label(
        about,
        text='FlipCard - приложение для обучения с использованием карточек с вопросами и ответами.', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    text1.place(relx=.5, y=310, anchor='n');

    devs = Label(
        about,
        text='Разработчики:', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    devs.place(relx=.5, y=335, anchor='n');

    dev_1 = Label(
        about,
        text=' - Черепанова Софья Юрьевна', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    dev_1.place(relx=.5, y=360, anchor='n');

    dev_2 = Label(
        about,
        text=' - Ипанова Дарья Александровна', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    dev_2.place(relx=.5, y=385, anchor='n');

    text5 = Label(
        about,
        text=' - Беляева Ксения Евгеньевна', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    ).place(relx=.5, y=410, anchor='n');

    dev_3 = Label(
        about,
        text=' - Селина Дарина Сергеевна', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    dev_3.place(relx=.5, y=435, anchor='n');

    group = Label(
        about,
        text=' группа 1-ИС, 3 курс, 09.02.07 Информационные системы и програиммирование', 
        font=('Roboto', 16),
        foreground='#000000',
        background='#fdfdfd'
    )
    group.place(relx=.5, y=460, anchor='n');

    study = Button(
        about,
        text='Учиться', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=2, 
        cursor='hand2',
        command=menu.openMenu
    )
    study.place(relx=.5, y=510, anchor='n');

    logout_2 = Button(
        about,
        text='Выйти', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#6689BD',
        width=20,
        height=2, 
        cursor='hand2',
        command=login.openLogin
    )
    logout_2.place(relx=.5, y=580, anchor='n');

    about.mainloop()
