# Import the Tkinter library and alias it as 'tk'.
import tkinter as tk

# Create the main application window.
root = tk.Tk()

# Set the title of the application window.
root.title("The Button widget")

# Create a Button widget with the label "Click Me!", a raised relief style, and set it to a disabled state.
tk.Button(root, text="Click Me!", relief="raised", state="disabled").pack()

# Start the Tkinter main event loop, which keeps the window open and responsive.
root.mainloop()
