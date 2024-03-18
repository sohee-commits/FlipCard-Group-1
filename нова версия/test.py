from tkinter import *
from tkinter import ttk

root = Tk();
root.title('FlipCard');
root.iconbitmap(default='assets/cards.ico');
root.geometry('1280x720');
root.configure(background='#fdfdfd');

def erase(rootWindow, listOfElements):
    for element in listOfElements:
        element.destroy()
    login.login(rootWindow)

def main(rootWindow):
    logo = Label(
        rootWindow,
        text='FlipCard', 
        font=('Roboto', 48, 'bold'),
        foreground='#0047AB',
        background='#fdfdfd'
    )
    logo.place(relx=.5, y=235, anchor='n');

    description = Label(
        rootWindow,
        text='Сервис для запоминания информации с помощью карточек', 
        font=('Roboto', 16),
        background='#fdfdfd'
    )
    description.place(relx=.5, y=335, anchor='n');

    register = Button(
        rootWindow,
        text='Зарегистрироваться', 
        font=('Roboto', 16, 'bold'),
        foreground='#fdfdfd',
        background='#0047AB',
        width=20,
        height=2, 
        cursor='hand2',
        command=lambda: erase(rootWindow, listOfElements)
    )
    register.place(relx=.5, y=435, anchor='n');

    listOfElements = [logo, description, register]

main(root)

root.mainloop();