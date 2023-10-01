# Import the Tkinter library and alias it as 'tk'.
import tkinter as tk

# Create the main application window.
root = tk.Tk()

# Set the title of the application window.
root.title("Let's Make a Menu")

# Set the minimum size for the application window.
root.minsize(300, 200)

# Create the main menu bar.
mainmenu = tk.Menu(root)

# Create a "File" menu.
filemenu = tk.Menu(mainmenu, tearoff=0)

# Add various commands and separators to the "File" menu.
filemenu.add_command(label="New Text File")
filemenu.add_command(label="New File")
filemenu.add_command(label="New Window")
filemenu.add_separator()
filemenu.add_command(label="Open File")
filemenu.add_command(label="Open Folder")

# Create a submenu for "Open Recent" items.
openrecent = tk.Menu(mainmenu)
openrecent.add_command(label="File 1 12/11/23")
openrecent.add_command(label="File 2 11/11/23")
openrecent.add_command(label="File 3 22/11/23")
openrecent.add_command(label="File 4 16/11/23")

# Add the "Open Recent" submenu to the "File" menu.
filemenu.add_cascade(label="Open Recent", menu=openrecent)

filemenu.add_separator()

# Add an "Exit" command to the "File" menu that quits the application.
filemenu.add_command(label="Exit", command=root.quit)

# Add the "File" menu to the main menu bar.
mainmenu.add_cascade(label="File", menu=filemenu)

# Create an "Edit" menu.
editmenu = tk.Menu(mainmenu, tearoff=0)

# Add various commands and separators to the "Edit" menu.
editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_separator()
editmenu.add_command(label="Copy")
editmenu.add_command(label="Cut")
editmenu.add_command(label="Paste")
editmenu.add_separator()
editmenu.add_command(label="Find")
editmenu.add_command(label="Replace")

# Add the "Edit" menu to the main menu bar.
mainmenu.add_cascade(label="Edit", menu=editmenu)

# Create a "View" menu.
viewmenu = tk.Menu(mainmenu, tearoff=0)

# Add checkbuttons and radiobuttons to the "View" menu.
viewmenu.add_checkbutton(label="Terminal")
viewmenu.add_checkbutton(label="Explorer")
viewmenu.add_separator()
viewmenu.add_radiobutton(label="Menu")
viewmenu.add_radiobutton(label="Panel")
viewmenu.add_radiobutton(label="Output")
viewmenu.add_separator()
viewmenu.add_command(label="Problems")
viewmenu.add_command(label="Debug Console")

# Add the "View" menu to the main menu bar.
mainmenu.add_cascade(label="View", menu=viewmenu)

# Configure the main window to use the main menu bar.
root.config(menu=mainmenu)

# Start the Tkinter main event loop, which keeps the window open and responsive.
root.mainloop()
