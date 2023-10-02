# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("The Spinbox Application")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Create a Spinbox widget with the following properties:
# - from_: 0 (minimum value)
# - to: 10 (maximum value)
# - values: 5 (initial value)
spinbox = tk.Spinbox(root, from_=0, to=10, values=5)

# Pack the Spinbox to add it to the main window
spinbox.pack()

# Start the main event loop to display the application window
root.mainloop()
