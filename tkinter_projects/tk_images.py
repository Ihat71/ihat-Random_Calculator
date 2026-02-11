import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, filedialog, colorchooser
import customtkinter as ctk
bl = "Black"

def stretch_image(event):
    global resized_tk
    #size
    width = event.width
    height= event.height
    # print(width)
    # print(height)
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0,0, image=resized_tk, anchor='nw')
# this function instead cuts the image and changes the aspect ratio to fill the canvas
def fill_canvas(event):
    global resized_tk
    canvas_ratio = event.width/event.height
    #get cords
    if canvas_ratio > image_ratio:
        #tkinter always wants int
        width = int(event.width)
        height = int(width / image_ratio)
    else: #canvas is narrower than the image
        width = int(event.height * image_ratio)
        height = int(event.height)
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width/2),(int(event.height/2)), anchor='center', image=resized_tk)
#this func makes the aspect ratio stay the same
def show_full_image(event):
    global resized_tk
    canvas_ratio = event.width/event.height

    if canvas_ratio > image_ratio:
        #tkinter always wants int
        width = int(event.height * image_ratio)
        height = int(event.height)
    else: #canvas is narrower than the image
        width = int(event.width)
        height = int(width/image_ratio)
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width/2),(int(event.height/2)), anchor='center', image=resized_tk)

root = tk.Tk()
root.title("Training")
root.grid_columnconfigure((0,1,2,3), weight=1, uniform='a')
root.grid_rowconfigure(0, weight=1, uniform='a')
root.geometry('600x400')

frame_1 = ttk.Frame(root)
'''Images'''
# import an image
image_original = Image.open(r'C:\Users\MIQDAD\OneDrive\racoon.jpeg').resize((600,400))
# this is important information for scaling
image_ratio = image_original.size[0]/image_original.size[1]
image_tk = ImageTk.PhotoImage(image_original)
#widgets
# label = ttk.Label(frame_1, text = 'raccoon', image = image_tk)
# label.pack()
python_dark = Image.open(r"C:\Users\MIQDAD\OneDrive\python_dark.png").resize((40,40))
python_dark_tk = ImageTk.PhotoImage(python_dark)

booton = ttk.Button(frame_1, text='Python', image=python_dark_tk, compound='left')
booton.grid()
frame_1.grid(column=0, row=0, sticky='nsew')


# images do not scale by themselves, we need canvas
canvas = tk.Canvas(root, background = 'black', bd=0, highlightthickness=0, relief = 'ridge')
canvas.grid(column=1, columnspan=3, row=0, sticky='nsew')

#runs everytime the size of the canvas changes
canvas.bind('<Configure>', show_full_image)

root.mainloop()
