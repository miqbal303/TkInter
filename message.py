# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Multiple Lines with Message")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Create a Message widget with the specified text, background color, width, justification, and relief
tk.Message(
    root,
    text="we can say that a Message widget is just like the label widget just that it displays long text by default in multiple lines, it is kind of obsolete now but can still help in some cases",
    bg="royalblue",
    width=200,
    justify="center",
    relief="raised"
).pack()

# Start the main event loop to display the application window
root.mainloop()
