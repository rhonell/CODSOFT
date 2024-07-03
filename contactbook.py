import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x400")
        self.root.config(bg="#2E2E2E")
        
        self.contacts = {}
        
        # Title Label
        self.title_label = tk.Label(root, text="Contact Book", font=('Helvetica', 24, 'bold'), fg="#FFD700", bg="#2E2E2E")
        self.title_label.pack(pady=20)
        
        # Add Contact Button
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, font=('Arial', 14), bg="#32CD32", fg="#FFFFFF")
        self.add_button.pack(pady=10)
        
        # View Contact List Button
        self.view_button = tk.Button(root, text="View Contact List", command=self.view_contacts, font=('Arial', 14), bg="#4682B4", fg="#FFFFFF")
        self.view_button.pack(pady=10)
        
        # Search Contact Button
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact, font=('Arial', 14), bg="#FF6347", fg="#FFFFFF")
        self.search_button.pack(pady=10)
        
        # Update Contact Button
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, font=('Arial', 14), bg="#FFD700", fg="#2E2E2E")
        self.update_button.pack(pady=10)
        
        # Delete Contact Button
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, font=('Arial', 14), bg="#FF4500", fg="#FFFFFF")
        self.delete_button.pack(pady=10)
        
    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:", parent=self.root)
        phone = simpledialog.askstring("Input", "Enter phone number:", parent=self.root)
        email = simpledialog.askstring("Input", "Enter email address:", parent=self.root)
        address = simpledialog.askstring("Input", "Enter address:", parent=self.root)
        
        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and phone number are required!")
    
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available!")
            return
        
        contacts_str = "Contacts:\n"
        for name, info in self.contacts.items():
            contacts_str += f"{name} - {info['phone']}\n"
        
        messagebox.showinfo("Contact List", contacts_str)
    
    def search_contact(self):
        search_term = simpledialog.askstring("Input", "Enter name or phone number to search:", parent=self.root)
        
        if search_term:
            found_contacts = {name: info for name, info in self.contacts.items() if search_term in name or search_term in info['phone']}
            
            if found_contacts:
                contacts_str = "Search Results:\n"
                for name, info in found_contacts.items():
                    contacts_str += f"{name} - {info['phone']}\n"
                
                messagebox.showinfo("Search Results", contacts_str)
            else:
                messagebox.showinfo("Info", "No contacts found!")
        else:
            messagebox.showerror("Error", "Search term is required!")
    
    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to update:", parent=self.root)
        
        if name in self.contacts:
            phone = simpledialog.askstring("Input", f"Enter new phone number (current: {self.contacts[name]['phone']}):", parent=self.root)
            email = simpledialog.askstring("Input", f"Enter new email address (current: {self.contacts[name]['email']}):", parent=self.root)
            address = simpledialog.askstring("Input", f"Enter new address (current: {self.contacts[name]['address']}):", parent=self.root)
            
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address
            
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")
    
    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:", parent=self.root)
        
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

