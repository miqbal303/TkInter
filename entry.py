# Import the Tkinter library and alias it as 'tk'.
import tkinter as tk

# Create the main application window.
root = tk.Tk()

# Set the title of the application window.
root.title("Entry Widget")

# Create a label widget with the text "Name: ".
label = tk.Label(root, text="Name: ")

# Create an entry widget (text input field).
entry = tk.Entry(root)

# Insert a default value ("The Metabrains!") into the entry widget.
entry.insert(0, "The Metabrains!")

# Disable the entry widget, making it read-only.
entry.config(state="disabled")

# Pack the label and entry widgets to display them in the main window.
label.pack()
entry.pack()

# Start the Tkinter main event loop, which keeps the window open and responsive.
root.mainloop()
