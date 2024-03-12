from tkinter import *
from tkinter import ttk


# о программе
# def openAbout():
about = Tk();
about.title('FlipCard');
about.geometry('1280x720');
about.configure(background='#fdfdfd');

# header
o_program = Button(
    about,
    text='О программе', 
    font=('Roboto', 16, 'bold'),
    foreground='#fdfdfd',
    background='#0047AB',
    width=20,
    height=1, 
    cursor='hand2',
    borderwidth=0,
).place(relx=.27, y=30, anchor='n');

themes = Button(
    about,
    text='Темы', 
    font=('Roboto', 16, 'bold'),
    foreground='#fdfdfd',
    background='#0047AB',
    width=20,
    height=1, 
    cursor='hand2',
    borderwidth=0,
).place(relx=.5, y=30, anchor='n');


logout = Button(
    about,
    text='Выйти', 
    font=('Roboto', 16, 'bold'),
    foreground='#fdfdfd',
    background='#6689BD',
    width=20,
    height=1, 
    cursor='hand2',
    borderwidth=0,
).place(relx=.73, y=30, anchor='n');
# header

topic = Label(
    about,
    text='О программе', 
    font=('Roboto', 32, 'bold'),
    foreground='#0047AB',
    background='#fdfdfd'
).place(relx=.5, y=235, anchor='n');

text1 = Label(
    about,
    text='FlipCard - приложение для обучения с использованием карточек с вопросами и ответами.', 
    font=('Roboto', 16),
    foreground='#000000',
    background='#fdfdfd'
).place(relx=.5, y=310, anchor='n');

text2 = Label(
    about,
    text='Разработчики:', 
    font=('Roboto', 16),
    foreground='#000000',
    background='#fdfdfd'
).place(relx=.5, y=335, anchor='n');

text3 = Label(
    about,
    text=' - Черепанова Софья Юрьевна', 
    font=('Roboto', 16),
    foreground='#000000',
    background='#fdfdfd'
).place(relx=.5, y=360, anchor='n');

text4 = Label(
    about,
    text=' - Ипанова Дарья Александровна', 
    font=('Roboto', 16),
    foreground='#000000',
    background='#fdfdfd'
).place(relx=.5, y=385, anchor='n');

text5 = Label(
    about,
    text=' - Беляева Ксения Евгеньевна', 
    font=('Roboto', 16),
    foreground='#000000',
    background='#fdfdfd'
).place(relx=.5, y=410, anchor='n');

text6 = Label(
    about,
    text=' - Селина Дарина Сергеевна', 
    font=('Roboto', 16),
    foreground='#000000',
    background='#fdfdfd'
).place(relx=.5, y=435, anchor='n');

text7 = Label(
    about,
    text=' группа 1-ИС, 3 курс, 09.02.07 Информационные системы и програиммирование', 
    font=('Roboto', 16),
    foreground='#000000',
    background='#fdfdfd'
).place(relx=.5, y=460, anchor='n');

study = Button(
    about,
    text='Учиться', 
    font=('Roboto', 16, 'bold'),
    foreground='#fdfdfd',
    background='#0047AB',
    width=20,
    height=2, 
    cursor='hand2',
).place(relx=.5, y=510, anchor='n');

exit = Button(
    about,
    text='Выйти', 
    font=('Roboto', 16, 'bold'),
    foreground='#fdfdfd',
    background='#6689BD',
    width=20,
    height=2, 
    cursor='hand2',
).place(relx=.5, y=580, anchor='n');

about.mainloop()