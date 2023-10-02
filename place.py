# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Placing Widget")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Create a Button widget with the text "MY PLACE"
btn = tk.Button(root, text="MY PLACE")

# Use the place geometry manager to specify the position (x=20, y=20),
# height (50), and width (25) of the button within the window
btn.place(x=20, y=20, height=50, width=25)

# Start the main event loop to display the application window
root.mainloop()
