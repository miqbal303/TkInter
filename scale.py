# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("The Scale Like Thermometer")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Define a function called 'scaleColor' to change the scale's background color based on its value
def scaleColor(value):
    # Convert the value to an integer
    int_value = int(value)
    
    # Check the value and set the background color accordingly
    if int_value <= 20:
        scale.config(bg="blue")
    elif 20 < int_value <= 40:
        scale.config(bg="yellow")
    elif 40 < int_value <= 65:
        scale.config(bg="orange")
    else:
        scale.config(bg="red")

# Create a Scale widget with the specified parameters:
# - length: 250 (vertical length)
# - from_: 0 (minimum value)
# - to: 100 (maximum value)
# - tickinterval: 15 (interval between tick marks)
# - orient: "vertical" (vertical orientation)
# - command: scaleColor (function to call when the scale value changes)
scale = tk.Scale(root, length=250, from_=0, to=100, tickinterval=15, orient="vertical", command=scaleColor)

# Set the initial value of the scale
scale.set(30)

# Pack the scale to add it to the main window
scale.pack()

# Start the main event loop to display the application window
root.mainloop()
