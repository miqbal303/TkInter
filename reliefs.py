# Import the tkinter library and the random module
import tkinter as tk
import random

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Widgets with Reliefs")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Define a function called 'relief' to change the button's relief style randomly
def relief():
    # List of possible relief styles
    rel = ["raised", "sunken", "flat", "groove", "ridge"]
    
    # Check if the current relief style of the button is in the 'rel' list
    if btn['relief'] in rel:
        # Generate a random index to select a new relief style from the list
        i = random.randint(0, 4)
        
        # Configure the button's relief style and text with the randomly selected values
        btn.config(relief=rel[i])
        btn.config(text=rel[i])

# Create a Button widget with the initial text "Raised" and relief style "raised"
btn = tk.Button(root, text="Raised", relief="raised", command=relief)

# Pack the button to add it to the main window
btn.pack()

# Start the main event loop to display the application window
root.mainloop()
