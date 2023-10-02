# Import the tkinter library
import tkinter as tk
from PIL import Image, ImageTk

# Open and resize an image
image = Image.open("image.jpg")
image = image.resize((500, 300))

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("The Text Widget")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Convert the image to a PhotoImage object using PIL's ImageTk
img = ImageTk.PhotoImage(image)

# Create a Text widget within the main window
text = tk.Text(root)

# Insert text into the Text widget
text.insert("insert", "The First line In the text widget..\n")
text.insert("end", "The Second line In the text widget...")

# Embed the image at the end of the text
text.image_create("end", image=img)

# Pack the Text widget to add it to the main window
text.pack()

# Define and apply tags to specific text ranges
text.tag_add("here", "1.0", "1.36")  # Tag for the first line
text.tag_add("next", "2.0", "2.36")  # Tag for the second line

# Configure the appearance of tagged text
text.tag_config("here", background="orange", font="times")
text.tag_config("next", background="yellow", font="calibri")

# Start the main event loop to display the application window
root.mainloop()
