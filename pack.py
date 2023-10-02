# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("The Packer")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Create a Button with the default packing position (top)
tk.Button(root, text="Default Position").pack()

# Create a Button with custom packing attributes:
# - side: "right" (pack to the right side of the window)
# - anchor: "center" (center the widget within its packing space)
# - fill: "x" (expand horizontally to fill available space)
# - expand: 1 (allow expansion within the packing space)
tk.Button(root, text="default Position attibutes").pack(side="right", anchor="center", fill="x", expand=1)

# Start the main event loop to display the application window
root.mainloop()
