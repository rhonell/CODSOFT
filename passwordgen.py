import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.config(bg="#2E2E2E")
        
        # Title Label
        self.title_label = tk.Label(root, text="Password Generator", font=('Helvetica', 18, 'bold'), fg="#FFD700", bg="#2E2E2E")
        self.title_label.pack(pady=20)
        
        # Labels and Entry for password length
        self.length_label = tk.Label(root, text="Password Length:", font=('Arial', 14), fg="#FFFFFF", bg="#2E2E2E")
        self.length_label.pack(pady=5)
        
        self.length_entry = tk.Entry(root, width=10, font=('Arial', 14))
        self.length_entry.pack(pady=5)
        
        # Checkbuttons for character options
        self.uppercase_var = tk.IntVar()
        self.lowercase_var = tk.IntVar()
        self.digits_var = tk.IntVar()
        self.special_var = tk.IntVar()
        
        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=self.uppercase_var, font=('Arial', 12), fg="#FFFFFF", bg="#2E2E2E", selectcolor="#4B4B4B")
        self.uppercase_check.pack(pady=2)
        
        self.lowercase_check = tk.Checkbutton(root, text="Include Lowercase", variable=self.lowercase_var, font=('Arial', 12), fg="#FFFFFF", bg="#2E2E2E", selectcolor="#4B4B4B")
        self.lowercase_check.pack(pady=2)
        
        self.digits_check = tk.Checkbutton(root, text="Include Digits", variable=self.digits_var, font=('Arial', 12), fg="#FFFFFF", bg="#2E2E2E", selectcolor="#4B4B4B")
        self.digits_check.pack(pady=2)
        
        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.special_var, font=('Arial', 12), fg="#FFFFFF", bg="#2E2E2E", selectcolor="#4B4B4B")
        self.special_check.pack(pady=2)
        
        # Button to generate password
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=('Arial', 14), bg="#FFD700", fg="#2E2E2E")
        self.generate_button.pack(pady=20)
        
        # Label to display the generated password
        self.password_label = tk.Label(root, text="", font=('Arial', 14, 'bold'), fg="#FFD700", bg="#2E2E2E")
        self.password_label.pack(pady=10)
        
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError
            
            characters = ""
            if self.uppercase_var.get():
                characters += string.ascii_uppercase
            if self.lowercase_var.get():
                characters += string.ascii_lowercase
            if self.digits_var.get():
                characters += string.digits
            if self.special_var.get():
                characters += string.punctuation
            
            if not characters:
                messagebox.showwarning("Warning", "Please select at least one character type.")
                return
            
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text=f"Generated Password: {password}")
        
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for the password length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

