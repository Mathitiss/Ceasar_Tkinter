from tkinter import *
import tkinter as ttk
from tkinter import font

# Window

root = Tk()
root.title("Caesar Ipher")
root.geometry('1280x720')
root.resizable(False, False)
root.configure(bg='white')
# icon = PhotoImage(file = "logo.png")      This idiot doesn`t see image. But it is in same folder. Yesterday every thing worked fine !!!
# root.iconphoto(False, icon)

# ENG -> CHOOSE TASK

def ENG():
    global English
    global button_font

    English = Toplevel()
    English.title("Task")
    English.geometry('1280x720')
    English.resizable(False, False)
    English.configure(bg='white')

    # Buttons

    btn_Encr_ENG = ttk.Button(English, text='Encryption', height=4, width=35, cursor="hand2", font=button_font, command=Encr_ENG)
    btn_Encr_ENG.grid(row=1, column=0, pady=5)
    btn_Encr_ENG.place(relx=0.5, rely=0.5, anchor=CENTER, y=-100)

    btn_Decr_ENG = ttk.Button(English, text='Decryption', height=4, width=35, cursor="hand2", font=button_font, command=Decr_ENG)
    btn_Decr_ENG.grid(row=2, column=0, pady=5)
    btn_Decr_ENG.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

    root.withdraw()

def RUS():
    global Russian
    global button_font

    Russian = Toplevel()
    Russian.title("Задача")
    Russian.geometry('1280x720')
    Russian.resizable(False, False)
    Russian.configure(bg='white')

    # Buttons

    btn_Encr_RUS = ttk.Button(Russian, text='Шифрование', height=4, width=35, cursor="hand2", font=button_font, command=Encr_RUS)
    btn_Encr_RUS.grid(row=1, column=0, pady=5)
    btn_Encr_RUS.place(relx=0.5, rely=0.5, anchor=CENTER, y=-100)

    btn_Decr_RUS = ttk.Button(Russian, text='Дешифрование', height=4, width=35, cursor="hand2", font=button_font, command=Decr_RUS)
    btn_Decr_RUS.grid(row=2, column=0, pady=5)
    btn_Decr_RUS.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

    root.withdraw()

# ENG -> WORKING PLACE

def Encr_ENG():
    global Encryption_ENG

    Encryption_ENG = Toplevel()
    Encryption_ENG.title("Encryption") 
    Encryption_ENG.geometry('1280x720')
    Encryption_ENG.resizable(False, False)
    Encryption_ENG.configure(bg='white')

    label_text = ttk.Label(Encryption_ENG, text="Write a word in the first row and a number of indent in the second", font=("Arial", 24), foreground="#808080", background="#FFFFFF")
    label_text.place(relx=0.5, rely=0.5, anchor=CENTER, y=-200)

    Bar_Text = Entry(Encryption_ENG, fg='black', bg='white', border=2, font=28)
    Bar_Text.place(relx=0.5, rely=0.5, anchor=CENTER, y=-80, width=250, height=40)

    Bar_Digit = Entry(Encryption_ENG, fg='black', bg='white', border=2, font=28)
    Bar_Digit.place(relx=0.5, rely=0.5, anchor=CENTER, y=-20, width=250, height=40)

    btn_complite = ttk.Button(Encryption_ENG, text='Accept', height=2, width=35, cursor="hand2") # , command=
    btn_complite.grid(row=1, column=0, pady=5)
    btn_complite.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

    English.withdraw()

def Decr_ENG():
    global Decryption_ENG

    Decryption_ENG = Toplevel()
    Decryption_ENG.title("Decryption")
    Decryption_ENG.geometry('1280x720')
    Decryption_ENG.resizable(False, False)
    Decryption_ENG.configure(bg='white')

    Bar_Text = Entry(Decryption_ENG, fg='black', bg='white', border=2, font=28)
    Bar_Text.place(relx=0.5, rely=0.5, anchor=CENTER, y=-80, width=250, height=40)

    Bar_Digit = Entry(Decryption_ENG, fg='black', bg='white', border=2, font=28)
    Bar_Digit.place(relx=0.5, rely=0.5, anchor=CENTER, y=-20, width=250, height=40)

    btn_complite = ttk.Button(Decryption_ENG, text='Accept', height=2, width=35, cursor="hand2") # , command=
    btn_complite.grid(row=1, column=0, pady=5)
    btn_complite.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

    English.withdraw()

# RUS -> WORKING PLACE

def Encr_RUS():
    global Encryption_RUS

    Encryption_RUS = Toplevel()
    Encryption_RUS.title("Шифрование")
    Encryption_RUS.geometry('1280x720')
    Encryption_RUS.resizable(False, False)
    Encryption_RUS.configure(bg='white')

    Bar_Text = Entry(Encryption_RUS, fg='black', bg='white', border=2, font=28)
    Bar_Text.place(relx=0.5, rely=0.5, anchor=CENTER, y=-80, width=250, height=40)

    Bar_Digit = Entry(Encryption_RUS, fg='black', bg='white', border=2, font=28)
    Bar_Digit.place(relx=0.5, rely=0.5, anchor=CENTER, y=-20, width=250, height=40)

    btn_complite = ttk.Button(Encryption_RUS, text='Подтвердть', height=2, width=35, cursor="hand2") # , command=
    btn_complite.grid(row=1, column=0, pady=5)
    btn_complite.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

    Russian.withdraw()

def Decr_RUS():
    global Decryption_RUS

    Decryption_RUS = Toplevel()
    Decryption_RUS.title("Дешифрование")
    Decryption_RUS.geometry('1280x720')
    Decryption_RUS.resizable(False, False)
    Decryption_RUS.configure(bg='white')

    Bar_Text = Entry(Decryption_RUS, fg='black', bg='white', border=2, font=28)
    Bar_Text.place(relx=0.5, rely=0.5, anchor=CENTER, y=-80, width=250, height=40)

    Bar_Digit = Entry(Decryption_RUS, fg='black', bg='white', border=2, font=28)
    Bar_Digit.place(relx=0.5, rely=0.5, anchor=CENTER, y=-20, width=250, height=40)

    btn_complite = ttk.Button(Decryption_RUS, text='Подтвердть', height=2, width=35, cursor="hand2") # , command=
    btn_complite.grid(row=1, column=0, pady=5)
    btn_complite.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

    Russian.withdraw()

# BUTTONS LANGUAGE CHOOSE

button_font = font.Font(size=20)

btn_ENG = ttk.Button(root, text='ENGLISH', height=4, width=35, cursor="hand2", command=ENG, font=button_font)
btn_ENG.grid(row=1, column=0, pady=5)
btn_ENG.place(relx=0.5, rely=0.5, anchor=CENTER, y=-100)

btn_RUS = ttk.Button(root, text='RUSSIAN', height=4, width=35, cursor="hand2", command=RUS, font=button_font)
btn_RUS.grid(row=2, column=0, pady=5)
btn_RUS.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

# On/Off

root.mainloop()