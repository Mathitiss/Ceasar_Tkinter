from tkinter import *
import tkinter as ttk
 
def accept():  # txt
    eeee = Tk()
    eeee.geometry('300x200')
    eeee.geometry(f"+{(eeee.winfo_screenwidth() - 200) // 2}+{(eeee.winfo_screenheight() - 200) // 2}")
    eeee.resizable(False, False)
    eeee.configure(bg='white')

    label = ttk.Label(eeee, text='I AM RETARDED', font=("Arial", 18), foreground="black", background="white")
    label.place(relx=0.5, rely=0.5, anchor=CENTER, y=-20)        

    close_btn = ttk.Button(eeee, text='close', height=2, width=25, cursor="hand2", command=eeee.destroy)
    close_btn.grid(row=1, column=0, pady=5)
    close_btn.place(relx=0.5, rely=0.5, anchor=CENTER, y=50)

    eeee.mainloop()