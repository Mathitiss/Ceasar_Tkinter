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

    alp_ENG =  'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    alp_RUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
    result = ''

    if language == "ENG":
        if operation == "ENCRYPTION":
            for i in txt:
                x = alp_ENG.find(i)
                y = int(x) + int(ind)
                if i in alp_ENG:
                    result += alp_ENG[y]
                else:
                    result += i
        else:
            pass
    else:
        if operation == "ENCRYPTION":
            for i in txt:
                x = alp_RUS.find(i)
                y = int(x) + int(ind)
                if i in alp_RUS:
                    result += alp_RUS[y]
                else:
                    result += i
        else:
            pass

    label = ttk.Label(eeee, text=result, font=("Arial", 18), foreground="black", background="white")
    label.place(relx=0.5, rely=0.5, anchor=CENTER, y=-20)        

    close_btn = ttk.Button(eeee, text='close', height=2, width=25, cursor="hand2", command=eeee.destroy)
    close_btn.grid(row=1, column=0, pady=5)
    close_btn.place(relx=0.5, rely=0.5, anchor=CENTER, y=50)

    eeee.mainloop()