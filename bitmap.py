# Import the tkinter library and alias it as 'tk'
import tkinter as tk

# Import the random module to generate random numbers
import random

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Bitmaps")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Define a function called 'on_click' that will be called when the button is clicked
def on_click():
    # List of bitmap names
    bmp = ["error", "gray25", "gray50", "gray75", "gray12", "hourglass", "questhead", "info", "warning", "question"]
    
    # Check if the current bitmap on the button is in the 'bmp' list
    if btn['bitmap'] in bmp:
        # Generate a random index to select a new bitmap from the list
        i = random.randint(0, len(bmp) - 1)
        
        # Configure the button's bitmap with the randomly selected bitmap
        btn.config(bitmap=bmp[i])
        
        # Update the label text to show the selected bitmap name in uppercase
        label.config(text=bmp[i].upper())

# Create a Label widget with the initial text "ERROR"
label = tk.Label(root, text="ERROR")

# Create a Button widget with text "Raised", relief "raised", initial bitmap "error",
# and set the command to call the 'on_click' function when clicked
btn = tk.Button(root, text="Raised", relief="raised", bitmap="error", command=on_click)

# Pack the label and button widgets to add them to the window
label.pack()
btn.pack()

# Start the main event loop to display the application window and handle user interactions
root.mainloop()
