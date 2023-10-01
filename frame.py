# Import the Tkinter library and alias it as 'tk'.
import tkinter as tk

# Create the main application window.
root = tk.Tk()

# Set the title of the application window.
root.title("Widgets in Window with Frame")

# Set the minimum size for the application window.
root.minsize(300, 200)

# Create a frame widget with a pink background, height, and width.
frame = tk.Frame(root, bg="pink", height=400, width=400)

# Create a label widget within the frame with specified text, background color, font, and wrap length.
# The label is packed into the frame.
label = tk.Label(frame, text="Label in tkinter is used to display text and images. It is widely used throughout Tkinter applications, and I advise all developers to use this widget.", bg="lightgreen", font="calibri", wraplength=300).pack()

# Use a loop to create Radiobutton widgets with different text, values, and a custom width.
# These Radiobuttons are packed into the frame.
for text, value in [("Apple", 1), ("Banana", 2), ("Grape", 3), ("Strawberry", 4), ("Olive", 5)]:
    tk.Radiobutton(frame, text=text, value=value, indicatoron=0, width=20).pack()

# Pack the frame widget to display it in the main window.
frame.pack()

# Start the Tkinter main event loop, which keeps the window open and responsive.
root.mainloop()
