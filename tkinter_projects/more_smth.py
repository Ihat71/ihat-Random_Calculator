import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, filedialog, colorchooser
import customtkinter as ctk
bl = "Black"

root = tk.Tk()
root.title("Training")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.geometry('600x400')

frame_1 = tk.Frame(root)
frame_1.grid(column=0, row=0, sticky='nsew')
frame_1.grid_rowconfigure((0,1,2,3,4,5), weight=1)
frame_1.grid_columnconfigure((0,1,2,3,4,5), weight=1, uniform='a')
'''
TTK Styles:

style = ttk.Style(): Create a style object.
style.theme_use(): Set the theme.
style.configure(): Configure styles for widget classes or specific instances.
style.map(): Change styles based on widget states.
theme_names(): Get available themes.
Set font, border, and relief styles: Customize appearance further.

Font: 

family

Description: Specifies the font family (e.g., "Arial", "Times New Roman", "Helvetica").
Example: font=("Arial", 12)
size

Description: Specifies the font size in points (e.g., 12 for 12-point font).
Example: font=("Arial", 14)
weight

Description: Sets the weight of the font (e.g., normal, bold).
Example: font=("Arial", 12, "bold")
slant

Description: Indicates whether the font is italic or normal (e.g., italic, roman).
Example: font=("Arial", 12, "italic")
underline

Description: Specifies whether the text should be underlined (1 for true, 0 for false).
Example: font=("Arial", 12, "underline")
overstrike

Description: Indicates whether the text should be overstruck (1 for true, 0 for false).
Example: font=("Arial", 12, "overstrike")

Relief: 

Relief styles define the visual effect of the border. There are several types of relief styles you can use:

flat: No border or relief effect. The widget appears flat against the background.
raised: The widget looks as if it is raised above the background. It gives the impression of being pushed away from the surface.
sunken: The widget appears to be sunken into the background, creating a 3D effect that makes it look as if it's pressed down.
groove: Creates a 3D effect with a groove around the widget, appearing as if the edges are carved into the background.
ridge: The opposite of groove, where the edges appear to be raised from the surface.
solid: A simple, solid border without any 3D effects (similar to flat but with a defined border).

'''
# # Create a Style object
# style = ttk.Style()
# style.theme_use('clam')  # Set the theme

# # Configure styles for buttons in frame_1
# style.configure('TButton', background='lightblue', foreground='black', font=('Arial', 12))
# style.map('TButton', background=[('active', 'violet')])  # Change color on hover

# # Create styled buttons in frame_1
# btn1 = tk.Button(frame_1, text='Button 1', relief='groove')
# btn1.grid(pady=10)

# btn2 = ttk.Button(frame_1, text='Button 2')
# btn2.grid(pady=10)

'''
Extra TTK Widgets

ttk.Notebook

Parameters:
width: Width of the notebook.
height: Height of the notebook.
padding: Space around the content inside the notebook tabs.
style: Custom style for the notebook.
Explanation: A notebook widget contains multiple tabs, allowing users to switch between different content views.

ttk.Combobox

Parameters:
values: A list of options for the dropdown.
textvariable: A variable to store the current selection.
state: Sets the state of the combobox (normal, readonly, disabled).
width: The width of the combobox.
Explanation: Combobox is a dropdown list that allows users to select one option from multiple choices.

ttk.Treeview

Parameters:
columns: A tuple defining the columns in the treeview.
show: Specifies what to display (tree, headings, or both).
height: The height of the treeview.
selectmode: The selection mode (single, browse, extended).
Explanation: A treeview widget displays hierarchical data in a tree-like structure, allowing for expandable items.

ttk.Progressbar

Parameters:
orient: Orientation of the progress bar (horizontal or vertical).
length: Length of the progress bar.
mode: The mode of the progress bar (determinate, indeterminate).
maximum: Maximum value of the progress.
value: Current value of the progress.
Explanation: A progress bar visually represents the progress of a task.

ttk.LabelFrame

Parameters:
text: Label displayed on the frame border.
padding: Space around the contents inside the frame.
style: Custom style for the label frame.
Explanation: A label frame groups related widgets and provides a title for that group.

ttk.Message

Parameters:
text: The message to display.
width: Maximum width of the message (text wraps within this width).
anchor: Alignment of the text (n, s, e, w, center).
justify: How to justify the text (left, center, right).
background: Background color of the message.
foreground: Text color of the message.
Explanation: A message widget displays multi-line text, useful for providing information to users.

ttk.Separator

Parameters:
orient: Orientation of the separator (horizontal or vertical).
Explanation: A separator is a thin line that visually divides sections of a user interface.

ttk.Scale

Parameters:
from_: Minimum value of the scale.
to: Maximum value of the scale.
orient: Orientation of the scale (horizontal or vertical).
length: Length of the scale.
variable: A variable to store the current value of the scale.
Explanation: A scale widget allows users to select a numeric value by sliding a handle along a track.


'''



'''
Events: 

mouse->
<Button-1>: Left mouse button click.
<Button-2>: Middle mouse button click (scroll wheel).
<Button-3>: Right mouse button click.
<Double-Button-1>: Double-click with the left mouse button.
<B1-Motion>: Holding down the left mouse button and moving (dragging).
<ButtonRelease-1>: Release of the left mouse button.
<Enter>: Mouse pointer enters the widget area.
<Leave>: Mouse pointer leaves the widget area.
<Motion>: Mouse movement over a widget.

keyboard->
<Key>: Any key press (captures all key presses).
<KeyPress> or <KeyPress-A>: Press of a specific key (e.g., <KeyPress-a> captures only when the "a" key is pressed).
<KeyRelease>: Release of a key.
<Control-KeyPress-c>: Combination of keys like Ctrl+C

window->
<FocusIn>: Widget gains focus (e.g., when a user clicks on an entry field).
<FocusOut>: Widget loses focus (e.g., when a user clicks out of an entry field).
<Configure>: When a widget is resized or moved.
<Destroy>: When a widget is destroyed (e.g., when a window is closed).
<Map>: When a widget is displayed on the screen.
<Unmap>: When a widget is removed from the screen (hidden).

Others->
<Return>: Pressing the Enter key (useful for text fields).
<Escape>: Pressing the Escape key.
<MouseWheel>: Scrolling the mouse wheel (varies across operating systems).
<Visibility>: When a widget becomes visible on the screen.
<Activate>: When a window becomes active.
<Deactivate>: When a window loses focus and becomes inactive.
'''

'''TEXT WIDGET'''
#text_widg = tk.Text(frame_1, height=5, width=30)
#text_widg.grid(column=0, row=0, sticky='nsew')

'''Checkbutton widget'''
#check = tk.Checkbutton(frame_1, text="Check 1")
#check.grid(column=0, row=0, sticky='nsew')
#check2 = tk.Checkbutton(frame_1, text="Check 2")
#check2.grid(column=1, row=0, sticky='nsew')

'''Radio Button'''
# selected = IntVar()
# rButton_1 = tk.Radiobutton(frame_1, text = 'option_1',variable=selected,value=1)
# rButton_1.grid(column=0,row=0,sticky='nsew')
# rButton_2 = tk.Radiobutton(frame_1, text = 'option_1', variable=selected, value=2)
# rButton_2.grid(column=1,row=0,sticky='nsew')

'''Listbox'''
# listbox = tk.Listbox(frame_1)
# listbox.insert(1, "Item 1")
# listbox.insert(2, "Item 2")
# listbox.pack() 

'''Canvas'''
# canvas = tk.Canvas(frame_1, height=200, width=200)
# canvas.create_line(0, 0, 200, 100)
# canvas.pack()

'''
Differences between pack, grid and place

Pack goes top to bottom by default
pack packs widgets rekative to their parent windown, either vertically or horizontally
widget.pack(side='top', fill='x', padx=5, pady=5)
widgets can also be stacked on top of each other if only pack() is used
expand = True makes expansion possible

grid is grid, and it creates a grid

place allows absolute positioning of widgets using x or y
widget.place(x=50, y=100)
'''
# button = tk.Button(frame_1, text='click me')
# #button.pack(side='top', padx=5, pady=5)
# button.pack(anchor='nw', padx=5, pady=5, expand=True)

'''Menu'''
#they are nested but it is all one widget in reality
# menu = tk.Menu(frame_1)
# file_menu = tk.Menu(menu, tearoff = False)
# file_menu.add_command(label = 'New', command = lambda: print('New file'))
# file_menu.add_command(label = 'Open', command = lambda: print('Open file'))
# file_menu.add_separator()
# #use tutorialpoint for full tkinter syntax
# menu.add_cascade(label = "File", menu = file_menu)

# help_menu = tk.Menu(menu, tearoff = False)
# help_menu.add_command(label = 'Help', command = lambda: print('help...'))
# menu.add_cascade(label = "Help", menu = help_menu) 
# help_check_string = tk.StringVar()
# help_menu.add_checkbutton(label = 'Check', onvalue='on',offvalue='off',variable=help_check_string)

# # sub menu with sub menues:

# exercise_menu = tk.Menu(menu, tearoff=False)
# exercise_menu.add_command(label = 'exercise test 1')
# menu.add_cascade(label = 'Exercise', menu = exercise_menu)

# exercise_sub_menu = tk.Menu(exercise_menu, tearoff=False)
# exercise_sub_menu.add_command(label = 'More stuff')
# exercise_menu.add_cascade(label='Sub Exercise', menu=exercise_sub_menu)


# root.configure(menu = menu)

# #menu button, seperate widget
# menu_button = ttk.Menubutton(frame_1, text = 'Menu Button')
# menu_button.pack()

# buttom_sub_menu = tk.Menu(menu_button, tearoff = False)
# buttom_sub_menu.add_command(label='entry 1', command=lambda: print('test 1'))
# menu_button.configure(menu = buttom_sub_menu)

'''You can use pack grid and place together, and you should do so by packing frames together and having one frame in grid and the other in place or others.'''

'''
Tkinter variables, used to make widgets interact with each other

StringVar(), IntVar(), DoubleVar(), BooleanVar()

These variables are useful and can be used instead of get

There is also .trace('w') to watch for changes
'''

# def button_func():
#     print(string_var.get())
#     string_var.set('button pressed')

# string_var = tk.StringVar()

# label = ttk.Label(master=frame_1, text = 'label', textvariable=string_var)
# label.pack()

# entry = ttk.Entry(master=frame_1, textvariable=string_var)
# entry.pack()

# button = ttk.Button(master=frame_1, text = 'button', command = button_func)
# button.pack()

# exercise_var = tk.StringVar(value = 'test')

# entry1 = ttk.Entry(master=frame_1, textvariable=exercise_var)
# entry1.pack()
# entry2 = ttk.Entry(master=frame_1, textvariable=exercise_var)
# entry2.pack()

# label_ex = ttk.Label(master=frame_1, textvariable=exercise_var)
# label_ex.pack()

# #validation

# def correct(s, v, d, inp):
#     if inp.isdigit():
#         print(v)
#         return True
#     elif inp == '':
#         return True
#     else:
#         print(s)
#         print(f'Rejected: {d}')
#         return False
    
# e = tk.Entry(frame_1)
# e.grid()
# reg = frame_1.register(correct)
# e.config(validate='key', validatecommand=(reg, '%s', '%v', '%S', '%P'))
# # %P is a specifier which is the new value of the entry after the edit (the value that the entry will have if the edit is allowed)
# # Other specifiers: check em out later pal


'''Dialog Boxes, File dialogs, Color Picker

File dialogs:
askopenfilename(): For selecting a single file.
askopenfilenames(): For selecting multiple files.
asksaveasfilename(): For selecting a location and name for saving a file.
askdirectory(): For selecting a directory.

other args:
multiple: if True then multiple files can be selected
default textension: adds a default file extension if the user does not specify one

for asksavefilename -> initialfile: a default file name that appears in the dialog
'''
# #Message box

# #messagebox.showinfo('Question', 'How are you')
# #there is also showerror and showwarning

# if messagebox.askyesno('Question', 'Are you good', icon='info') == True:
#     print('yes')
# else:
#     print('no')

#File dialog

#the initialdir starts at C:

# frame_1.filename = filedialog.askopenfilename(initialdir='/gif', title = 'Select a file', filetypes=(('png files', '*.png'),('all files', '*.*')))
# label = tk.Label(frame_1, text=frame_1.filename)
# label.grid()
# my_image = ImageTk.PhotoImage(Image.open(frame_1.filename))
# image_label = tk.Label(image=my_image)
# image_label.grid()

# def open():
#     global my_image
#     #you can open any file yuh
#     frame_1.filename = filedialog.askopenfilename(initialdir='/gif', title = 'Select a file', filetypes=(('png files', '*.png'),('all files', '*.*')))
#     label = tk.Label(frame_1, text=frame_1.filename)
#     label.grid()
#     my_image = ImageTk.PhotoImage(Image.open(frame_1.filename))
#     image_label = tk.Label(image=my_image)
#     image_label.grid()

# my_btn = tk.Button(frame_1, text='Open file', command=open)
# my_btn.grid()

# #color picker
# def color():
#     # my color becomes a list consisting of the rgb and the hexa code for the color
#     my_color = colorchooser.askcolor()[1]
#     my_label = ttk.Label(frame_1, text=my_color)
#     my_label.pack()
#     label_2 = ttk.Label(frame_1, text="You picked this color", background=my_color)
#     label_2.pack()


# button_color = ttk.Button(frame_1, text='Pick a color', command=color)
# button_color.pack()

'''
Standalone executable:

Download pyinstaller

$pyinstaller.exe --onefile --icon=(put in the icon) (... put in the file here ...)

'''


root.mainloop()
