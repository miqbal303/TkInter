# Import the Tkinter library and alias it as 'tk'.
import tkinter as tk

# Create the main application window.
root = tk.Tk()

# Set the title of the application window.
root.title("Displaying a List of Items")

# Set the minimum size for the application window.
root.minsize(300, 200)

# Create a Listbox widget with specified width, height, justification, selection background color, and selection mode.
l = tk.Listbox(root, width=15, height=5, justify="right", selectbackground="red", selectmode="extended")

# Populate the Listbox with items from 0 to 14 using a loop.
for item in range(15):
    l.insert("end", item)

# Pack the Listbox widget to display it in the main window.
l.pack()

# Start the Tkinter main event loop, which keeps the window open and responsive.
root.mainloop()
