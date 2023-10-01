# Import the Tkinter library and alias it as 'tk'.
import tkinter as tk

# Create the main application window.
root = tk.Tk()

# Set the title of the application window.
root.title("Menu with Menubutton")

# Set the minimum size for the application window.
root.minsize(300, 200)

# Create a Menubutton widget with the initial text "Select Options."
menubutton = tk.Menubutton(root, text="Select Options")

# Create a Menu widget that will be displayed when the Menubutton is clicked.
menu = tk.Menu(menubutton, tearoff=False)

# Associate the Menu with the Menubutton.
menubutton["menu"] = menu

# Add several menu items to the dropdown menu.
menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menu.add_command(label="Option 3")
menu.add_command(label="Option 4")

# Pack the Menubutton widget to display it in the main window.
menubutton.pack()

# Start the Tkinter main event loop, which keeps the window open and responsive.
root.mainloop()
