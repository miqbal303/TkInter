# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Dividing with Panes")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Create a PanedWindow widget with a yellow background, oriented vertically, and a width of 200
panedwindow = tk.PanedWindow(root, bg="yellow", orient="vertical", width=200)

# Pack the PanedWindow widget to add it to the main window
panedwindow.pack()

# Create Label widgets to represent the panes within the PanedWindow
l1 = tk.Label(panedwindow, text="Pane 1")
panedwindow.add(l1)

l2 = tk.Label(panedwindow, text="Pane 2")
panedwindow.add(l2)

l3 = tk.Label(panedwindow, text="Pane 3")
panedwindow.add(l3)

# Start the main event loop to display the application window
root.mainloop()
