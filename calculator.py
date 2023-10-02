# Import the tkinter library and alias it as 'tk'
import tkinter as tk

# Import the math module for mathematical calculations
import math

# Create a class called 'Calculator' that inherits from 'tk.Tk'
class Calculator(tk.Tk):
    # Constructor method for initializing the calculator
    def __init__(self):
        # Call the constructor of the parent class (tk.Tk)
        super().__init__()

        # Change the icon of the calculator window
        self.iconbitmap('calc.png')

        # Set the title of the calculator window
        self.title("Calculator")

        # Create a StringVar to hold the text in the input field
        self.input_text = tk.StringVar()

        # Create an Entry widget for user input, set its properties, and place it in the grid
        self.input_field = tk.Entry(self, textvariable=self.input_text, justify='right', width=30)
        self.input_field.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Define a list of buttons to create
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', 'sqrt',
        ]

        # Create buttons from the list and add them to the grid
        row = 1
        col = 0
        for button in buttons:
            button_action = lambda x=button: self.button_click(x)
            tk.Button(self, text=button, width=5, command=button_action).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Add memory-related buttons to the grid
        tk.Button(self, text='M+', width=5, command=self.memory_add).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self, text='M-', width=5, command=self.memory_subtract).grid(row=5, column=1, padx=5, pady=5)
        tk.Button(self, text='MR', width=5, command=self.memory_recall).grid(row=5, column=2, padx=5, pady=5)
        tk.Button(self, text='MC', width=5, command=self.memory_clear).grid(row=5, column=3, padx=5, pady=5)

        # Add clear and delete buttons to the grid
        clear_button = tk.Button(self, text='C', width=5, command=self.clear_input)
        clear_button.grid(row=6, column=0, padx=5, pady=5)
        delete_button = tk.Button(self, text='DEL', width=5, command=self.delete_char)
        delete_button.grid(row=6, column=1, padx=5, pady=5)

        # Create a Text widget for displaying the history log
        self.history_text = tk.Text(self, width=25, height=5)
        self.history_text.grid(row=1, column=5, rowspan=5, padx=5, pady=5)

        # Bind keyboard events to the calculator window
        self.bind('<Key>', self.keyboard_input)

        # Initialize memory to 0
        self.memory = 0

    # Method to handle button clicks
    def button_click(self, button):
        # Handle various button actions
        if button == '=':
            try:
                result = eval(self.input_text.get())
                self.input_text.set(result)
                self.history_text.insert(tk.END, self.input_text.get() + '\n')
            except:
                self.input_text.set('ERROR')
        elif button == 'C':
            self.clear_input()
        elif button == 'DEL':
            self.delete_char()
        elif button == 'sin':
            self.input_text.set(math.sin(math.radians(float(self.input_text.get()))))
        elif button == 'cos':
            self.input_text.set(math.cos(math.radians(float(self.input_text.get()))))
        elif button == 'tan':
            self.input_text.set(math.tan(math.radians(float(self.input_text.get()))))
        elif button == 'sqrt':
            self.input_text.set(math.sqrt(float(self.input_text.get())))
        else:
            current_text = self.input_text.get()
            new_text = current_text + button
            self.input_text.set(new_text)

    # Method to clear the input field
    def clear_input(self):
        self.input_text.set('')

    # Method to delete the last character from the input field
    def delete_char(self):
        current_text = self.input_text.get()
        new_text = current_text[:-1]
        self.input_text.set(new_text)

    # Method to handle keyboard input
    def keyboard_input(self, event):
        if event.char in '0123456789+-*/.()':
            self.button_click(event.char)
        elif event.keysym == 'Return':
            self.button_click('=')
        elif event.keysym == 'BackSpace':
            self.delete_char()

    # Method to add the current input to memory
    def memory_add(self):
        current_input = self.input_text.get()
        try:
            current_input = float(current_input)
            self.memory += current_input
        except:
            pass

    # Method to subtract the current input from memory
    def memory_subtract(self):
        current_input = self.input_text.get()
        try:
            current_input = float(current_input)
            self.memory -= current_input
        except:
            pass

    # Method to recall the value from memory and display it in the input field
    def memory_recall(self):
        self.input_text.set(str(self.memory))

    # Method to clear the value in memory
    def memory_clear(self):
        self.memory = 0

# Create an instance of the Calculator class
calc = Calculator()

# Start the main event loop to run the calculator application
calc.mainloop()
