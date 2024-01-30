from tkinter import *

def openAbout():
    pass;

# menu window
def openMenu():
    menu = Toplevel();
    menu.title('FlipCard');
    menu.iconbitmap(default='assets/cards.ico');
    menu.geometry('1280x720');
    menu.configure(background='#fdfdfd');

    about = Button(
        menu,
        text='О программе', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=openAbout
    ).place(relx=.27, y=30, anchor='n');

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
        command=openMenu
    ).place(relx=.5, y=30, anchor='n');

    logout = Button(
        menu,
        text='Выйти', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#aaaaaa',
        width=20,
        height=1, 
        cursor='hand2',
        borderwidth=0,
        command=openLogin
    ).place(relx=.73, y=30, anchor='n');

    topics_text = Label(
        menu,
        text='Темы', 
        font=('Roboto', 32, 'bold'),
        foreground='#0047AB',
        background='#fdfdfd'
    ).place(relx=.5, y=100, anchor='n');

    url_js='assets\javascript.png';
    url_py='assets\python.png';

    img_js=PhotoImage(file=url_js);
    img_py=PhotoImage(file=url_py);

    py_theme = Button(
        menu,
        image=img_py,
        compound='left',
        text='Python', 
        font=('Roboto', 24, 'bold'),
        background='#fdfdfd',
        cursor='hand2',
        borderwidth=0,
        command=openCardsNoDb
    ).place(relx=.48, y=175, anchor='n');

    js_theme = Button(
        menu,
        image=img_js,
        compound='left',
        text='JavaScript', 
        font=('Roboto', 24, 'bold'),
        background='#fdfdfd',
        cursor='hand2',
        borderwidth=0,
        command=openCardsNoDb
    ).place(relx=.5, y=225, anchor='n');

    menu.mainloop();

# cards without database
def openCardsNoDb():
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
        command=openAbout
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
        command=openMenu
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
        command=openLogin
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
        command=openMenu
    ).place(relx=.5, y=445, anchor='n');

# root
# define root window and options
root = Tk();
root.title('FlipCard');
root.iconbitmap(default='assets/cards.ico');
root.geometry('1280x720');
root.configure(background='#fdfdfd');

# root widgets
logo = Label(
    root,
    text='FlipCard', 
    font=('Roboto', 48, 'bold'),
    foreground='#0047AB',
    background='#fdfdfd'
).place(relx=.5, y=235, anchor='n');

description = Label(
    root,
    text='Сервис для запоминания информации с помощью карточек', 
    font=('Roboto', 16),
    background='#fdfdfd'
).place(relx=.5, y=335, anchor='n');

register = Button(
    root,
    text='Зарегистрироваться', 
    font=('Roboto', 16, 'bold'),
    foreground='#fdfdfd',
    background='#0047AB',
    width=20,
    height=2, 
    cursor='hand2',
    command=openLogin
).place(relx=.5, y=435, anchor='n');

# loop windows
root.mainloop();
