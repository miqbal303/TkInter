# Import the tkinter library and alias it as 'tk'
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("widgets and anchors")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Create a Frame widget and immediately pack it into the main window.
# Note: 'frame' will hold the value 'None' because 'pack()' returns None.
frame = tk.Frame(root).pack()

# Create a Label widget with the text "North" and immediately pack it into the main window.
# The 'anchor' attribute is set to "s" (south), which means the label will be anchored to the south.
tk.Label(root, text="North").pack(anchor="s")

# Start the main event loop to display the application window and handle user interactions
root.mainloop()
