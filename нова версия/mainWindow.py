from tkinter import *
from tkinter import ttk
import login as login
import main as main


root = Tk();
root.title('FlipCard');
root.iconbitmap(default='assets/cards.ico');
root.geometry('1280x720');
root.configure(background='#fdfdfd');

main.main(root)

root.mainloop();