import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        
        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
        self.entry.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        for button in buttons:
            if button == '=':
                tk.Button(root, text=button, width=4, height=2, font=('Arial', 18), command=self.calculate).grid(row=row_val, column=col_val, columnspan=4, sticky="nsew")
                row_val += 1
                col_val = 0
            else:
                tk.Button(root, text=button, width=4, height=2, font=('Arial', 18), command=lambda x=button: self.on_button_click(x)).grid(row=row_val, column=col_val)
                col_val += 1
                if col_val > 3:
                    col_val = 0
                    row_val += 1
        
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        
    def on_button_click(self, char):
        self.entry.insert(tk.END, char)
    
    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, 'Error')

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

