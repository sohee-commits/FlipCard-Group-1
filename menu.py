from tkinter import *
from tkinter import ttk

menu = Tk()
menu.title('FlipCard')
menu.geometry('1280x720')
menu.configure(background='#fdfdfd')



#верхняя менюшка!!!
nav = Frame(menu, borderwidth=0, border=0, width=20, bg='#fdfdfd', pady=30) 

o_program = Button(
    nav,
    text='О программе', 
    font=('Roboto', 16, 'bold'),
    foreground='#fdfdfd',
    background='#0047AB',
    width=20,
    height=1, 
    cursor='hand2',
    borderwidth=0,
).pack(side=LEFT, padx=20)
#.place(relx=.27, y=30, anchor='n');

themes = Button(
    nav,
    text='Темы', 
    font=('Roboto', 16, 'bold'),
    foreground='#fdfdfd',
    background='#0047AB',
    width=20,
    height=1, 
    cursor='hand2',
    borderwidth=0,
).pack(side=LEFT)
#.place(relx=.5, y=30, anchor='n');


logout = Button(
    nav,
    text='Выйти', 
    font=('Roboto', 16, 'bold'),
    foreground='#fdfdfd',
    background='#AAAAAA',
    width=20,
    height=1, 
    cursor='hand2',
    borderwidth=0,
).pack(side=LEFT, padx=20)
#.place(relx=.73, y=30, anchor='n');

nav.pack(anchor=N, padx=20)
#верхняя менюшка!!!


themes_text = Label(
    text='Темы', 
    font=('Roboto', 30, 'bold'),
    foreground='#0047AB',
    background='#fdfdfd'
).place(relx=.5, y=140, anchor='n');

url_js='assets\javascript.png'
url_py='assets\python.png'

#img_js=PhotoImage(file=r'assets\javascript.png')
#img_py=PhotoImage(file=url_py)
#размещение картинки: compound= bottom, center, left, none, right, or top

py_theme = Button(
    #image=img_py,
    #compound=LEFT,
    text='Python', 
    font=('Roboto', 14, 'bold'),
    foreground='#000000',
    background='#FFFFFF',
    width=20,
    height=1, 
    cursor='hand2',
    borderwidth=0,
).place(relx=.5, y=205, anchor='n');

js_theme = Button(
    #image=img_js,
    text='JavaScript', 
    font=('Roboto', 14, 'bold'),
    foreground='#000000',
    background='#FFFFFF',
    width=20,
    height=1, 
    cursor='hand2',
    borderwidth=0,
).place(relx=.5, y=255, anchor='n');

menu.mainloop()