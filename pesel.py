import tkinter as tk
from tkinter import *

root = tk.Tk()
root.config(bd=4)

pesel = IntVar()

def check_pesel():
    e = E.get()
    first_10 = 1*int(e[0])+3*int(e[1])+7*int(e[2])+9*int(e[3])+1*int(e[4])+3*int(e[5])+7*int(e[6])+9*int(e[7])+1*int(e[8])+3*int(e[9])
    last = 10 - int(str(first_10)[-1])
    if str(last)[-1] == str(e)[-1]:
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
