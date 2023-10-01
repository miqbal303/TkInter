# Import the Tkinter library and alias it as 'tk'.
import tkinter as tk

# Create the main application window.
root = tk.Tk()

# Set the title of the application window.
root.title("The Checkbutton Widget")

# Set the minimum size for the application window.
root.minsize(300, 200)

# Create a label widget with the text "Select Your Best Fruit" and display it in the window.
tk.Label(root, text="Select Your Best Fruit").pack()

# Create multiple Checkbutton widgets for different fruit options and display them in the window.
tk.Checkbutton(root, text="Mango").pack()
tk.Checkbutton(root, text="Banana").pack()
tk.Checkbutton(root, text="Apple").pack()
tk.Checkbutton(root, text="Grape").pack()
tk.Checkbutton(root, text="Grapefruit").pack()

# Create a disabled Checkbutton widget with the text "Metabrains" and display it in the window.
tk.Checkbutton(root, text="Metabrains", state="disabled").pack()

# Start the Tkinter main event loop, which keeps the window open and responsive.
root.mainloop()
