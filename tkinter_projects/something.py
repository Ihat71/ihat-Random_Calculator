import tkinter as tk
from tkinter import ttk
# Function to reverse the string using recursion
def rever(x, n=0):
    if len(x) == 1:
        return x
    elif len(x) == 2:
        x = x[-1] + x[0]
        return x
    else:
        return x[-1] + rever(x[n+1:-1]) + x[0]

# Function to handle button click and display reversed string
def on_button_click():
    user_input = entry.get()  # Get the text from the Entry widget
    reversed_string = rever(user_input)  # Reverse the string
    result_label.config(text=f"Reversed: {reversed_string}")  # Update label with result

# Create the main window
root = tk.Tk()
root.title("String Reverser")

frame=tk.Frame(root)
frame.grid(row=0, column=0)

# Label for input
lbl = tk.Label(root, text="Enter a string:")
lbl.grid(row=0, column=0, columnspan=2)

# Entry widget for user input
entry = tk.Entry(root)
entry.grid(row=1, column=0, sticky='ew')

# Button to trigger string reversal
button = ttk.Button(root, text="Reverse", command=on_button_click)
button.grid(row=1, column=2, columnspan=1, sticky='ew')

# Label to display the reversed string
result_label = tk.Label(root, text="Reversed: ")
result_label.grid(row=2, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()
