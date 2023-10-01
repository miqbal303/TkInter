# Import the Tkinter library and alias it as 'tk'.
import tkinter as tk

# Create the main application window.
root = tk.Tk()

# Set the title of the application window.
root.title("Drawing with Canvas")

# Set the minimum size for the application window.
root.minsize(300, 200)

# Create a Canvas widget with a blue background, height, and width.
canvas = tk.Canvas(root, bg="blue", height=500, width=500)

# Define coordinates for a green rectangle and create it on the canvas.
rect = 10, 10, 100, 50
canvas.create_rectangle(rect, fill="green")

# Define coordinates for an orange square and create it on the canvas.
sqr = 10, 10, 50, 50
canvas.create_rectangle(sqr, fill="orange")

# Define coordinates for a red line and create it on the canvas.
line = 20, 20, 150, 250, 100, 300
canvas.create_line(line, fill="red")

# Define coordinates for a gray oval and create it on the canvas.
oval = 30, 30, 200, 100
canvas.create_oval(oval, fill="gray")

# Define coordinates for a purple arc and create it on the canvas.
coord = 50, 50, 120, 250
canvas.create_arc(coord, start=0, extent=150, fill="purple")

# Define coordinates for a pink polygon and create it on the canvas.
pol = 45, 10, 200, 350, 100, 240
canvas.create_polygon(pol, fill="pink")

# Pack the canvas widget to display it in the main window.
canvas.pack()

# Start the Tkinter main event loop, which keeps the window open and responsive.
root.mainloop()
