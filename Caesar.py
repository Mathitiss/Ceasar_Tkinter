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

# Encryption & Decryption

def click1():
    Encryption = Tk()
    Encryption.title("Encryption")
    Encryption.geometry('1280x720')
    Encryption.resizable(False, False)
    Encryption.configure(bg='white')
    root.destroy()

def click2():
    Decryption = Tk()
    Decryption.title("Decryption")
    Decryption.geometry('1280x720')
    Decryption.resizable(False, False)
    Decryption.configure(bg='white')
    root.destroy()

# Buttons

btn1 = ttk.Button(root, text='Encryption', height=10, width=70, cursor="hand2", command=click1)
btn1.grid(row=1, column=0, pady=5)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER, y=-100)

btn2 = ttk.Button(root, text='Decryption', height=10, width=70, cursor="hand2", command=click2)
btn2.grid(row=2, column=0, pady=5)
btn2.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

# On/Off

root.mainloop()