# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Grouping Widgets with Labelframe")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Create a LabelFrame widget with the label "Login"
labelframe = tk.LabelFrame(root, text="Login")

# Pack the LabelFrame to add it to the main window
labelframe.pack()

# Create Label widgets for "Email" and "Password" labels
label_Email = tk.Label(labelframe, text="Email: ")
label_password = tk.Label(labelframe, text="Password: ")

# Create Entry widgets for email and password input fields
email_entry = tk.Entry(labelframe)
password_entry = tk.Entry(labelframe)

# Use the grid geometry manager to organize the labels and entry fields in rows and columns
label_Email.grid(column=0, row=0)
email_entry.grid(column=1, row=0)
label_password.grid(column=0, row=1)
password_entry.grid(column=1, row=1)

# Start the main event loop to display the application window
root.mainloop()
