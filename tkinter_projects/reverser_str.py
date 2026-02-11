import tkinter as tk 
import numpy as np
from tkinter.font import Font
from tkinter import ttk
import re

button_list = []
#code for emerald green
black_bg = "Black"
em = '#00FFFF'
button_em = '#ADD8E6'
#reverses a string
def rever(x, n=0):
    if len(x) == 1:
        return x
    elif len(x) == 2:
        x = x[-1] + x[0]
        return x
    else:
        return x[-1] + rever(x[n+1:-1]) + x[0]

#calc function for calc function
def calculator(num=None, lbl=None):
    button_list.append(str(num))
    screen = lbl["text"]
    #if len(button_list) >= 2 and button_list[-2] == '=': [This block of code resets the screen after = is pressed and a button is pressed]
            #lbl.config(text=str(num))
            #return
    if num == 'C':
        lbl.config(text='')
    elif num == '=':
        #changes ^ to ** before eval
        if '^' in screen:  
            expo = re.sub(r'\^', '**', lbl['text'])
            screen = expo
        
        elif screen[0] in ['-', '+', '*', '/', '^', '%'] or screen[-1] in ['-', '+', '*', '/', '^', '%']:
            lbl.config(text="ERROR")
        result = eval(screen)
        round_result = round(result, 3)
        lbl.config(text=str(round_result))
    #clears the screen and replaces it with the num if there is an error and a button is pressed
    elif screen == 'ERROR':
        lbl.config(text=str(num))
    else:
        new_calc_label = screen + str(num)
        lbl.config(text=new_calc_label)
        


#helper function for the rev func
def rev_on_click(event=None):
    input_user = entry_1.get()
    reversed_ = rever(input_user)
    label_1.config(text=f'Reversed string: {reversed_}')


#changes pages
def go_to(frame_idk=None):
    #hiding frames using grid
    frame_idk.tkraise()
    
root = tk.Tk()
root.title('Reverser and More')
root.configure(bg=em)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.geometry('500x500') 

#font
bigFont = Font(
    family='Papyrus',
    size='14',
    weight='bold',
    slant='roman', #can make it italic
    underline=0,
    overstrike=0
)
    
#initialization of the og page
og_page = tk.Frame(root)
og_page.grid(row=0, column=0, sticky='nsew')
og_page.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
og_page.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
og_page.configure(bg=black_bg)

#Reverse page
frame_2 = tk.Frame(root)
frame_2.grid(row=0, column=0, sticky='nsew')
frame_2.grid_columnconfigure((0), weight=1)
frame_2.grid_rowconfigure((0,1,3,4), weight=1)
frame_2.configure(bg=black_bg)

#calc page
calc = tk.Frame(root)
calc.grid(row=0, column=0, sticky='nsew')
calc.grid_columnconfigure((0,1,2,3), weight=1)
calc.grid_rowconfigure((0,1,2,3,5,6), weight=1)
calc.configure(bg=black_bg)

#scientific calculator
sci_calc = tk.Frame(root)
sci_calc.grid(row=0, column=0, sticky='nsew')
sci_calc.grid_columnconfigure((0,1,2,3,4,5), weight=1)
sci_calc.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
sci_calc.configure(bg=black_bg)

#buttons in og page
og_label1 = tk.Label(og_page, text='These are the pages: ', bg="Black", fg="White", font=("Times New Roman", 16))
og_label1.grid(row=0, column=3, sticky='nsew')

go_reverse = tk.Button(og_page, text='Reverse page', font=bigFont, bg=em, command=lambda: go_to(frame_2), width=15, height=2)
go_reverse.grid(row=4, column=0, sticky='nsew', padx=20, pady=20)

go_calc = tk.Button(og_page, text='Calc page', font=bigFont, bg=em, command = lambda: go_to(calc), width=15, height=2)
go_calc.grid(row=4, column=6, sticky='nsew', padx=20, pady=20)

#buttons in frame2
entry_1 = tk.Entry(frame_2, bg=em)
entry_1.grid(sticky='nsew')
entry_1.bind('<Return>', rev_on_click)

rev = tk.Button(frame_2, text='reverse', command=rev_on_click, width=10, height=2)
rev.grid(sticky='ew')

label_1 = ttk.Label(frame_2, text='Reversed string: \n \n', wraplength= 300, width=30)
label_1.grid(sticky='nsew')

back_to_og = tk.Button(frame_2, text="Back", command = lambda xy=og_page: go_to(xy), width=10, height=1)
back_to_og.grid()

#buttons in calc
calc_label = tk.Label(calc, text="", bg=black_bg, fg='Cyan', pady=30)
calc_label.grid(row=0, column=0, columnspan=5)
#function for reusability
def calc_grid(grid, labl):    
    calc_buttons = [
    (1, 1, 0), (2, 1, 1), (3, 1, 2), ('+', 1, 3),
    (4, 2, 0), (5, 2, 1), (6, 2, 2), ('*', 2, 3),
    (7, 3, 0), (8, 3, 1), (9, 3, 2), ('-', 3, 3),
    (0, 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
    ('C', 5, 0), ('%', 5, 1), ('^', 5, 2)
    ]

    for (num, row_, col) in calc_buttons:
        x = tk.Button(grid, text=num, command= lambda num=num, lbl=labl: calculator(num, lbl))
        x.grid(row=row_, column = col, sticky='nsew', padx=1, pady=1)
calc_grid(calc, calc_label)
#button to go to sci_calc
goto_sci = ttk.Button(calc, text='Sci', command = lambda go_sci=sci_calc: go_to(go_sci))
goto_sci.grid(row=5, column=3, sticky='nsew')
#back to og page
back_to_og = tk.Button(calc, text='Back', command=lambda j=og_page: go_to(j))
back_to_og.grid(row=6, column=0, sticky='nsew', columnspan=4)

#buttons in sci_calc
sci_label = tk.Label(sci_calc, text='', bg=em, fg='Green')
sci_label.grid(row=0, column=0, sticky='nsew')

calc_grid(sci_calc, sci_label)

back_to_og = tk.Button(sci_calc, text='Back', command=lambda j=calc: go_to(j))
back_to_og.grid(row=6, column=0, sticky='nsew', columnspan=4)



#starts with og page
go_to(og_page)
root.mainloop()