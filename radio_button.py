# Import the Tkinter library and alias it as 'tk'.
import tkinter as tk

# Create the main application window.
root = tk.Tk()

# Set the title of the application window.
root.title("The Radiobutton Widget")

# Set the minimum size for the application window.
root.minsize(300, 200)

# Use a loop to create Radiobutton widgets with different text and values.
# These Radiobuttons will allow users to select one option out of a set.
for text, value in [("Apple", 1), ("Banana", 2), ("Grape", 3), ("Strawberry", 4), ("Olive", 5)]:
    # Create a Radiobutton with the specified text, value, and no indicator.
    tk.Radiobutton(root, text=text, value=value, indicatoron=0).pack()

# Start the Tkinter main event loop, which keeps the window open and responsive.
root.mainloop()
