import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        
        self.expression = ""
        
        # Display frame
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(expand=True, fill="both")
        
        self.display = tk.Entry(self.display_frame, font=("Arial", 24), justify="right", bd=10, insertwidth=2)
        self.display.pack(expand=True, fill="both")
        
        # Button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(expand=True, fill="both")
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('AC', 5, 0), ('C', 5, 1), ('(', 5, 2), (')', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.button_frame, text=text, font=("Arial", 18), bd=1, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Make the buttons expand and fill the space
        for i in range(6):
            self.button_frame.rowconfigure(i, weight=1)
            self.button_frame.columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.parse_expression(self.expression)))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        elif char == 'AC':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == 'C':
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
    
    def parse_expression(self, expression):
        # Add multiplication symbol where needed
        new_expression = ""
        for i in range(len(expression)):
            if (expression[i] == '(' and i > 0 and expression[i-1].isdigit()) or (expression[i] == ')' and i < len(expression) - 1 and expression[i+1].isdigit()):
                new_expression += '*'
            new_expression += expression[i]
        return new_expression

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
