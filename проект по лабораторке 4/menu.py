from tkinter import *
from tkinter import ttk

menu = Tk()
menu.title('FlipCard')
menu.geometry('1280x720')
menu.configure(background='#fdfdfd')



#верхняя менюшка!!!

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
).place(relx=.27, y=30, anchor='n');

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
).place(relx=.5, y=30, anchor='n');


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
).place(relx=.73, y=30, anchor='n');


#верхняя менюшка!!!


themes_text = Label(
    text='Темы', 
    font=('Roboto', 32, 'bold'),
    foreground='#0047AB',
    background='#fdfdfd'
).place(relx=.5, y=100, anchor='n');

url_js='assets\javascript 1.png'
url_py='assets\python 1.png'

img_js=PhotoImage(file=url_js)
img_py=PhotoImage(file=url_py)

py_theme = Button(
    image=img_py,
    compound=LEFT,
    text='Python', 
    font=('Roboto', 24, 'bold'),
    foreground='#000000',
    background='#FFFFFF',
    cursor='hand2',
    borderwidth=0,
).place(relx=.48, y=175, anchor='n');

js_theme = Button(
    image=img_js,
    compound=LEFT,
    text='JavaScript', 
    font=('Roboto', 24, 'bold'),
    foreground='#000000',
    background='#FFFFFF',
    cursor='hand2',
    borderwidth=0,
).place(relx=.5, y=225, anchor='n');

menu.mainloop()