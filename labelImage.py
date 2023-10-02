# Import the tkinter library
import tkinter as tk

# Import the Image and ImageTk modules from the PIL (Pillow) library
from PIL import Image, ImageTk

# Open and resize an image using PIL
image = Image.open("image.jpg")
image = image.resize((500, 300))

# Create the main application window
root = tk.Tk()

# Create an ImageTk object from the resized image
img = ImageTk.PhotoImage(image)

# Create a Label widget and set its image to the ImageTk object
label = tk.Label(root, image=img)

# Pack the Label widget to add it to the main window
label.pack()

# Start the main event loop to display the application window
root.mainloop()
