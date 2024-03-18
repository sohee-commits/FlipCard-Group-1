import menu
from tkinter import messagebox

def validate(email_value, password_value):
    if email_value == 'admin@example.com' and password_value == 'admin':
        menu.openMenu();
    else:
        messagebox.showerror("Login Failed", "Invalid email or password");