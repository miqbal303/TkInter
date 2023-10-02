# Import the tkinter library and the Font class from tkinter.font
import tkinter as tk
from tkinter.font import Font

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Change text Appearance with Fonts")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Create a new Font object (font1) with custom properties
font1 = Font(
    family="calibri",
    size=14,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0
)

# Create another new Font object (font2) with different custom properties
font2 = Font(
    family="courier",
    size=14,
    weight="bold",
    slant="roman",
    underline=1,
    overstrike=0
)

# Create a Label widget with the text "hello tkinter" and apply font1 to it
tk.Label(root, text="hello tkinter", font=font1).pack()

# Create another Label widget with the text "hello tkinter" and apply font2 to it
tk.Label(root, text="hello tkinter", font=font2).pack()

# Start the main event loop to display the application window
root.mainloop()
