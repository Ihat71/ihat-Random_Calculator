import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# Define the selection function to toggle between the two entries
# Define the validation function to check integer or string input
def validation(Int_or_Str, input_value):
    if input_value=="":
        return True
    if Int_or_Str == "Int":
        if input_value[0] == "-":  # If it starts with a negative sign
            return True
        return input_value.replace('.','',1).lstrip('-').isdigit()  # Only digits are allowed for integers
    elif Int_or_Str == "Str":
        return input_value.isalpha() # Non-empty strings
    return False  # Return False if neither condition is met

def entering(event):
    global param, cloud_tk
    if label_1["text"] == "Enter City":
        param['q'] = choice.get()
    else:
        param['q'] = f'{choice_2_lat.get()},{choice_2_long.get()}'
    #print(param['q'])
    weather.place_forget()
    weathering.tkraise()
    cloud = Image.open(r"C:\Users\MIQDAD\OneDrive\cloud_2.jpg").resize((40,40))
    cloud_tk = ImageTk.PhotoImage(cloud)
    weather_label_1.grid(row=0, column=0,sticky='NSEW')
    weather_label_1.config(image=cloud_tk, text=f"Weather in {param['q']}", compound='left')


    
def selection():
    selection_text = drop_down.get()
    if selection_text == "Choose a method":
        label_1.config(text="Please select an option")
        return
    if selection_text == "City":
        label_1.config(text="Enter City")
        choice.grid(row=1, column=0)
        choice_2_long.grid_forget()
        choice_2_lat.grid_forget()  # Hide 'choice_2' entry widget
        reg = weather.register(validation)
        choice.config(validate='key', validatecommand=(reg, 'Str', '%P'))
    elif selection_text == "Co-ordinates":
        label_1.config(text="Enter Coordinates (lat,long)")
        choice_2_lat.grid(row=1, column=0)
        choice_2_long.grid(row=1, column=1)
        choice.grid_forget()  # Hide 'choice' entry widget
        reg = weather.register(validation)
        choice_2_lat.config(validate='key', validatecommand=(reg, 'Int', '%P'))
        choice_2_long.config(validate='key', validatecommand=(reg, 'Int', '%P'))




    choose_method.grid_forget()
    drop_down.grid_forget()
    enter.grid(row=3, column=0)

# Set up the main application window
root = tk.Tk()
root.title("Is The Sun Shining?")
root.configure(bg="light blue")
root.geometry('600x600')

options = ['City', 'Co-ordinates']

# Create a frame to hold the widgets
weather = ttk.Frame(root, padding=20)
weather.place(x=225, y=250)
weather.grid_columnconfigure(0, weight=1)
weather.grid_rowconfigure((0, 1, 2, 3), weight=1)

#create a frame to have the actual weather app in
weathering = ttk.Frame(root, padding=20)
weathering.grid()
weathering.grid_columnconfigure((0,1,2,3,4,5), weight=1)
weathering.grid_rowconfigure((0,1,2,3,4,5), weight=1)


weather.tkraise()

'''--------------------------------------------------------------------------------'''

# Define variables
string = tk.StringVar()
integ = tk.IntVar()

# Create widgets
label_1 = ttk.Label(weather, text=" ")
label_1.grid(row=0, column=0)

# Entry widgets for City and Coordinates
choice = ttk.Entry(weather)
choice.bind('<Return>', entering)
choice_2_lat = ttk.Entry(weather)
choice_2_long = ttk.Entry(weather)


# Dropdown selection for choosing input type, using StringVar for reliable retrieval
selection_var = tk.StringVar()
drop_down = ttk.Combobox(weather, values=options, state="readonly", textvariable=selection_var)
drop_down.set("Choose a method")
drop_down.grid(row=2, column=0)

# Button to trigger selection function
choose_method = ttk.Button(weather, text="Choose", command=selection)
choose_method.grid(row=3, column=0)

enter = ttk.Button(weather, text="Enter", command=lambda event='': entering(event))


param = {
    'key':'e872f19aad18480b88994727242108',
    'q':f'{string}'
}
# cloud = Image.open(r"C:\Users\MIQDAD\OneDrive\cloud_1.jpg").resize((40,40))
# cloud_tk = ImageTk.PhotoImage(cloud)
cloud_tk=None
weather_label_1 = ttk.Label(weathering, background='light blue', relief='solid')
weather_label_1.grid(row=0, column=0, sticky='nsew')
weather_label_1.grid_forget()
root.mainloop()
