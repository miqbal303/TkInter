# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Colors")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Create a Button with a red background
tk.Button(root, text="Colors", bg="green").pack()

# Create a Button with red text color (foreground)
tk.Button(root, text="Colors", fg="red").pack()

# Create a Button with red background color when active (clicked)
tk.Button(root, text="Colors", activebackground="red").pack()

# Create a Button with red text color when active (clicked)
tk.Button(root, text="Colors", activeforeground="red").pack()

# Create a disabled Button with red text color and in a disabled state
tk.Button(root, text="Colors", disabledforeground="red", state="disabled").pack()

# Start the main event loop to display the application window
root.mainloop()
