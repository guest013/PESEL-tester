import tkinter as tk
from tkinter import *

root = tk.Tk()
root.config(bd=4)

pesel = IntVar()

def check_pesel():
    const = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    pesel = E.get()
    check = sum(map(lambda x,y: x*y, const, map(int, pesel)))
    if str(check)[-1] == str(pesel)[-1]:
        B.config(text="PESEL jest prawidłowy")
        B.config(fg='green')
    else:
        B.config(text="Podano niewłaściwy PESEL")
        B.config(fg='red')

L = tk.Label(root, text='PESEL: ').grid(row=0, column=0, sticky=W)

E = tk.Entry(root, textvariable=pesel)
E.grid(row=0, column=1)

B = tk.Button(root, text='Sprawdz PESEL', command=check_pesel)
B.grid(row=1, columnspan=2)

root.mainloop()
