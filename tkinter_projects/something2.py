import tkinter as tk
from tkinter import ttk #ttk is themed tk, which makes the thignies look better

root = tk.Tk()

root.title("simple app")

def add_to_list(even=None): #we need to put event as a default value to allow for bindings
    text = entry.get()
    if text:
        text_list.insert(tk.END, text) #tk.END tells you where to insert the input
        entry.delete(0, tk.END)

frame = tk.Frame(root) #frame acts as a container for the widgets

frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5) #pads pad the window

frame.columnconfigure(0, weight=1) #weight lets you control at what rate the column/row expands 

frame.rowconfigure(1, weight=1)

entry = tk.Entry(frame)

entry.grid(row=0, column=0, sticky='ew')

entry.bind('<Return>', add_to_list) #this will introduce keyboard action in the gui

#can also use lambda, ex: entry.bind(”<Return>”, lambda event: add_to_list

entry_btn = ttk.Button(frame, text='Add', command=add_to_list)

entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame)

text_list.grid(row=1, column=0, columnspan=2, sticky='ew') #sticky tells the object where to stick, ew stands for east and west

root.mainloop()