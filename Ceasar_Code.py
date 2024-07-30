from tkinter import *
import tkinter as ttk
 
def accept(entry_text1, entry_text2, flag1, flag2):
    eeee = Tk()
    eeee.geometry('300x200')
    eeee.title("Result")
    eeee.geometry(f"+{(eeee.winfo_screenwidth() - 200) // 2}+{(eeee.winfo_screenheight() - 200) // 2}")
    eeee.resizable(False, False)
    eeee.configure(bg='white')

    txt = entry_text1.get()
    ind = entry_text2.get()
    language = flag1
    operation = flag2


    # if language == "ENG":
    #     if operation == "ENCRYPTION":
    #         ...
    #     else:
    #         ...
    # else:
    #     if operation == "ENCRYPTION":
    #         ...
    #     else:
    #         ...


    result = ...

    label = ttk.Label(eeee, text=result, font=("Arial", 18), foreground="black", background="white")
    label.place(relx=0.5, rely=0.5, anchor=CENTER, y=-20)        

    close_btn = ttk.Button(eeee, text='close', height=2, width=25, cursor="hand2", command=eeee.destroy)
    close_btn.grid(row=1, column=0, pady=5)
    close_btn.place(relx=0.5, rely=0.5, anchor=CENTER, y=50)

    eeee.mainloop()