import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("500x500")
        self.root.config(bg="#1E1E1E")
        
        self.user_score = 0
        self.computer_score = 0
        
        # Title Label
        self.title_label = tk.Label(root, text="Rock-Paper-Scissors", font=('Helvetica', 24, 'bold'), fg="#FFD700", bg="#1E1E1E")
        self.title_label.pack(pady=20)
        
        # Instructions Label
        self.instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:", font=('Arial', 16), fg="#FFFFFF", bg="#1E1E1E")
        self.instruction_label.pack(pady=10)
        
        # Buttons for user choices
        button_frame = tk.Frame(root, bg="#1E1E1E")
        button_frame.pack(pady=10)
        
        self.rock_button = tk.Button(button_frame, text="Rock", command=lambda: self.play("rock"), font=('Arial', 14), bg="#FF6347", fg="#FFFFFF", width=10)
        self.rock_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.paper_button = tk.Button(button_frame, text="Paper", command=lambda: self.play("paper"), font=('Arial', 14), bg="#4682B4", fg="#FFFFFF", width=10)
        self.paper_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: self.play("scissors"), font=('Arial', 14), bg="#32CD32", fg="#FFFFFF", width=10)
        self.scissors_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Label to display the result
        self.result_label = tk.Label(root, text="", font=('Arial', 16, 'bold'), fg="#FFD700", bg="#1E1E1E")
        self.result_label.pack(pady=10)
        
        # Label to display the scores
        self.score_label = tk.Label(root, text="Scores\nUser: 0\nComputer: 0", font=('Arial', 16, 'bold'), fg="#FFFFFF", bg="#1E1E1E")
        self.score_label.pack(pady=10)
        
    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        result = ""
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1
        
        self.result_label.config(text=f"User: {user_choice.capitalize()}, Computer: {computer_choice.capitalize()}\n{result}")
        self.score_label.config(text=f"Scores\nUser: {self.user_score}\nComputer: {self.computer_score}")
        
        play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
        if not play_again:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

