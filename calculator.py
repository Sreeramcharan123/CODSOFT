import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator')

frame = tk.Frame(master=window, bg='black', padx=20)
frame.pack()

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=4, width=35)
entry.grid(row=0, column=0, columnspan=4, ipady=3, padx=3)

def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tk.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)
button_1 = tk.Button(frame, text='1', padx=20, pady=6, width=4, command=lambda: myclick(1))
button_2 = tk.Button(frame, text='2', padx=20, pady=6, width=4, command=lambda: myclick(2))
button_3 = tk.Button(frame, text='3', padx=20, pady=6, width=4, command=lambda: myclick(3))
button_4 = tk.Button(frame, text='4', padx=20, pady=6, width=4, command=lambda: myclick(4))
button_5 = tk.Button(frame, text='5', padx=20, pady=6, width=4, command=lambda: myclick(5))
button_6 = tk.Button(frame, text='6', padx=20, pady=6, width=4, command=lambda: myclick(6))
button_7 = tk.Button(frame, text='7', padx=20, pady=6, width=4, command=lambda: myclick(7))
button_8 = tk.Button(frame, text='8', padx=20, pady=6, width=4, command=lambda: myclick(8))
button_9 = tk.Button(frame, text='9', padx=20, pady=6, width=4, command=lambda: myclick(9))
button_0 = tk.Button(frame, text='0', padx=20, pady=6, width=4, command=lambda: myclick(0))
button_add = tk.Button(frame, text='+', padx=20, pady=6, width=4, command=lambda: myclick('+'))
button_subtract = tk.Button(frame, text='-', padx=20, pady=6, width=4, command=lambda: myclick('-'))
button_multiply = tk.Button(frame, text='*', padx=20, pady=6, width=4, command=lambda: myclick('*'))
button_division = tk.Button(frame, text='/', padx=20, pady=6, width=4, command=lambda: myclick('/'))
button_clear = tk.Button(frame, text='Clear', padx=20, pady=6, width=4, command=clear)
button_equal = tk.Button(frame, text='=', padx=20, pady=6, width=4, command=equal)
button_1.grid(row=1, column=0, pady=3)
button_2.grid(row=1, column=1, pady=3)
button_3.grid(row=1, column=2, pady=3)
button_4.grid(row=2, column=0, pady=3)
button_5.grid(row=2, column=1, pady=3)
button_6.grid(row=2, column=2, pady=3)
button_7.grid(row=3, column=0, pady=3)
button_8.grid(row=3, column=1, pady=3)
button_9.grid(row=3, column=2, pady=3)
button_0.grid(row=4, column=1, pady=3)
button_add.grid(row=5, column=0, pady=3)
button_subtract.grid(row=5, column=1, pady=3)
button_multiply.grid(row=5, column=2, pady=3)
button_division.grid(row=6, column=0, pady=3)
button_clear.grid(row=6, column=1, columnspan=1, pady=3)
button_equal.grid(row=6, column=2, columnspan=3, pady=3)

window.mainloop()
