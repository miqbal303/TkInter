# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Dimension Measurement!")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Create and display a Message widget with text and a width specified in millimeters
tk.Message(root, text="Dolor elit amet do magna veniam aliqua aute elit consequat qui.", width="5m").pack()

# Create and display another Message widget with text, a width specified in points, and a background color
tk.Message(root, text="Dolor elit amet do magna veniam aliqua aute elit consequat qui. Qui pariatur qui pariatur sunt culpa. Ullamco dolor nostrud do deserunt excepteur quis excepteur. Tempor reprehenderit adipisicing esse elit tempor proident.",
            width="5p", bg="#00ff55").pack()

# Start the main event loop to display the application window
root.mainloop()
