# Import the tkinter library
import tkinter as tk

# Import the random module to generate random numbers
import random

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Cursor Appearance on Widget")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Define a function called 'on_click' that will be called when the button is clicked
def on_click():
    # List of cursor appearances
    cursors = ["arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart", "man", "mouse"]
    
    # Check if the current cursor appearance on the button is in the 'cursors' list
    if btn['cursor'] in cursors:
        # Generate a random index to select a new cursor appearance from the list
        i = random.randint(0, len(cursors) - 1)
        
        # Configure the button's cursor with the randomly selected cursor appearance
        btn.config(cursor=cursors[i])
        
        # Update the label text to show the selected cursor appearance in uppercase
        label.config(text=cursors[i].upper())

# Create a Label widget with the initial text "ARROW"
label = tk.Label(root, text="ARROW")

# Create a Button widget with text "Raised", relief "raised", initial cursor "arrow",
# and set the command to call the 'on_click' function when clicked
btn = tk.Button(root, text="Raised", relief="raised", cursor="arrow", command=on_click)

# Pack the label and button widgets to add them to the window
label.pack()
btn.pack()

# Start the main event loop to display the application window and handle user interactions
root.mainloop()
