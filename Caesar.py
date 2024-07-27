from tkinter import *
import tkinter as ttk

# Window

root = Tk()
root.title("Caesar Ipher")
root.geometry('1280x720')
root.resizable(False, False)
root.configure(bg='white')
# icon = PhotoImage(file = "logo.png")      This idiot doesn`t see image. But it is in same folder. Yesterday every thing worked fine !!!
# root.iconphoto(False, icon)

# ENG/RUS

def ENG():
    global English

    English = Toplevel()
    English.title("Task")
    English.geometry('1280x720')
    English.resizable(False, False)
    English.configure(bg='white')

    # Buttons

    btn_Encr_ENG = ttk.Button(English, text='Encryption', height=10, width=70, cursor="hand2", command=Encr_ENG)
    btn_Encr_ENG.grid(row=1, column=0, pady=5)
    btn_Encr_ENG.place(relx=0.5, rely=0.5, anchor=CENTER, y=-100)

    btn_Decr_ENG = ttk.Button(English, text='Decryption', height=10, width=70, cursor="hand2", command=Decr_ENG)
    btn_Decr_ENG.grid(row=2, column=0, pady=5)
    btn_Decr_ENG.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

    root.withdraw()

def RUS():
    global Russian

    Russian = Toplevel()
    Russian.title("Задача")
    Russian.geometry('1280x720')
    Russian.resizable(False, False)
    Russian.configure(bg='white')

    # Buttons

    btn_Encr_RUS = ttk.Button(Russian, text='Шифрование', height=10, width=70, cursor="hand2", command=Encr_RUS)
    btn_Encr_RUS.grid(row=1, column=0, pady=5)
    btn_Encr_RUS.place(relx=0.5, rely=0.5, anchor=CENTER, y=-100)

    btn_Decr_RUS = ttk.Button(Russian, text='Дешифрование', height=10, width=70, cursor="hand2", command=Decr_RUS)
    btn_Decr_RUS.grid(row=2, column=0, pady=5)
    btn_Decr_RUS.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

    root.withdraw()

# ENG -> Encryption & Decryption

def Encr_ENG():
    global Encryption_ENG

    Encryption_ENG = Toplevel()
    Encryption_ENG.title("Encryption")
    Encryption_ENG.geometry('1280x720')
    Encryption_ENG.resizable(False, False)
    Encryption_ENG.configure(bg='white')

    English.withdraw()

def Decr_ENG():
    global Decryption_ENG

    Decryption_ENG = Toplevel()
    Decryption_ENG.title("Decryption")
    Decryption_ENG.geometry('1280x720')
    Decryption_ENG.resizable(False, False)
    Decryption_ENG.configure(bg='white')

    English.withdraw()

# RUS -> Encryption & Decryption

def Encr_RUS():
    global Encryption_RUS

    Encryption_RUS = Toplevel()
    Encryption_RUS.title("Шифрование")
    Encryption_RUS.geometry('1280x720')
    Encryption_RUS.resizable(False, False)
    Encryption_RUS.configure(bg='white')

    Russian.destroy()

def Decr_RUS():
    global Decryption_RUS

    Decryption_RUS = Toplevel()
    Decryption_RUS.title("Дешифрование")
    Decryption_RUS.geometry('1280x720')
    Decryption_RUS.resizable(False, False)
    Decryption_RUS.configure(bg='white')

    Russian.destroy()

# Buttons ENG/RUS

btn_ENG = ttk.Button(root, text='ENGLISH', height=10, width=70, cursor="hand2", command=ENG)
btn_ENG.grid(row=1, column=0, pady=5)
btn_ENG.place(relx=0.5, rely=0.5, anchor=CENTER, y=-100)

btn_RUS = ttk.Button(root, text='RUSSIAN', height=10, width=70, cursor="hand2", command=RUS)
btn_RUS.grid(row=2, column=0, pady=5)
btn_RUS.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

# On/Off

root.mainloop()