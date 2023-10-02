# Import the tkinter library
import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the title of the main window
root.title("My Toplevel Application")

# Set the minimum size of the main window (width: 300, height: 200)
root.minsize(300, 200)

# Initialize a global variable to store the top-level window
toplevel = None

# Function to create and display the top-level window with terms and conditions
def top():
    global toplevel
    toplevel = tk.Toplevel(root)
    
    # Create a label with the text "Terms And Conditions!" in the top-level window
    label = tk.Label(toplevel, text="Terms And Conditions!").pack()
    
    # Create a Message widget with terms and conditions text in the top-level window
    terms = tk.Message(toplevel, text="This is an agreement that stands as the terms and conditions of the metabrains. Here you promise to learn consistently in order to become a world-changing engineer tomorrow. Set yourself a daily goal to advance step by step; this will be a forward move toward your dreams.", width=300).pack()
    
    # Create radio buttons for "I agree" and "I disagree" in the top-level window
    radio = tk.Radiobutton(toplevel, text="I agree", command=agree, state="normal", value=1).pack()
    radio = tk.Radiobutton(toplevel, text="I disagree", command=root.quit, state="normal").pack()

# Function to handle the "I agree" radio button selection
def agree():
    global toplevel
    # Display a label in the main window indicating a good choice
    tk.Label(root, text="Good Choice").pack()
    # Destroy the top-level window
    toplevel.destroy()

# Create a button in the main window that triggers the 'top' function
btn = tk.Button(root, text="Install", command=top).pack()

# Start the main event loop to display the application window
root.mainloop()
