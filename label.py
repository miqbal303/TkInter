# Import the Tkinter library and alias it as 'tk'.
import tkinter as tk

# Create the main application window.
root = tk.Tk()

# Set the title of the application window.
root.title("Label")

# Create a label widget with specified text, background color, font, and wrap length.
label = tk.Label(root, text="Label in tkinter is used to display text and images. It is widely used throughout Tkinter applications, and I advise all developers to use this widget.", bg="lightgreen", font="calibri", wraplength=500)

# Pack the label widget inside the main window to display it.
label.pack()

# Start the Tkinter main event loop, which keeps the window open and responsive.
root.mainloop()
