from tkinter import *
import tkinter as tk

# Window

root = Tk()
root.title("Caesar Ipher")
root.geometry('1280x720')
root.resizable(False, False)
root.configure(bg='white')
icon = PhotoImage(file = "logo.png")
root.iconphoto(False, icon)

# Buttons

btn1 = tk.Button(root, text='Encryption', height=10, width=70)
btn1.grid(row=1, column=0, pady=5)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER, y=-100)

btn2 = tk.Button(root, text='Decryption', height=10, width=70)
btn2.grid(row=2, column=0, pady=5)
btn2.place(relx=0.5, rely=0.5, anchor=CENTER, y=100)

# On/Off

root.mainloop()