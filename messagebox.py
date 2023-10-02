# Import the tkinter library and the messagebox module
import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Messagebox Application")

# Set the minimum size of the window (width: 300, height: 200)
root.minsize(300, 200)

# Define functions to show different types of message boxes
def show_info():
    # Show an information message box with a message
    messagebox.showinfo("Info", "Learning is fun and practicing is clever")

def show_warning():
    # Show a warning message box with a notice
    messagebox.showwarning("Notice", "Have you practiced today?")

def show_error():
    # Show an error message box with a mistake message
    messagebox.showerror("Mistake", "Failing to practice is practicing to fail")

def show_question():
    # Show a question message box with a question and handle the response
    answer = messagebox.askquestion("Info", "Did you study? ")

    # Depending on the answer, display a label with a message
    if answer == "yes":
        tk.Label(root, text="Good Student!").pack()
    else:
        tk.Label(root, text="Please practice").pack()

# Create buttons to trigger the message boxes when clicked
btninfo = tk.Button(root, text="Click Info", command=show_info).pack()
btnwarning = tk.Button(root, text="Click Warning", command=show_warning).pack()
btnerror = tk.Button(root, text="Click Error", command=show_error).pack()
btnquestion = tk.Button(root, text="Click Question", command=show_question).pack()

# Start the main event loop to display the application window
root.mainloop()
