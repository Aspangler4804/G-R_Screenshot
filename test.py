#test out ttk

#part of standard libray, but use $ brew install python-tk if not in

import tkinter as tk

root = tk.Tk()
root.title("Simple")

def on_click():
    lbl.config(text="ButtonClick")


frame  = tk.Frame(root)
frame.grid(row=0, column=0)

lbl = tk.Label(root, text="Label 1").grid(row = 0, column =0)
btn = tk.Button(root, text="Button 1", command =on_click).grid(row = 0, column = 1)
#root is parent window



root.mainloop()
