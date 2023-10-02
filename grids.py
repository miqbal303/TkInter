# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Rows and Columns with Grid")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Nested loops to create a grid of buttons
for r in range(10):
    for c in range(10):
        # Create a Button widget with text "R{row}--C{column}" and a yellow background
        tk.Button(root, text="R%s--C%s" % (r, c), bg="yellow").grid(row=r, column=c, padx=3, pady=2)

# Start the main event loop to display the application window
root.mainloop()
