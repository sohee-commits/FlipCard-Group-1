from tkinter import *
from tkinter import ttk
import cards_nd 
import login 
import menu 
import about 

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
    command=login.openLogin
).place(relx=.5, y=435, anchor='n');

# loop windows
root.mainloop();
