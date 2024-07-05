import tkinter as tk
from tkinter import messagebox
import random

choices = ['rock', 'paper', 'scissors']

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x400")
        self.root.config(bg="lightblue")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:", bg="lightblue", font=("Arial", 16))
        self.label.pack(pady=20)
        
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("rock"), bg="orange", font=("Arial", 14), width=10)
        self.rock_button.pack(pady=10)
        
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("paper"), bg="green", font=("Arial", 14), width=10)
        self.paper_button.pack(pady=10)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("scissors"), bg="purple", font=("Arial", 14), width=10)
        self.scissors_button.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="", bg="lightblue", font=("Arial", 16))
        self.result_label.pack(pady=20)
        
        self.score_label = tk.Label(self.root, text="Score - You: 0, Computer: 0", bg="lightblue", font=("Arial", 16))
        self.score_label.pack(pady=20)
        
    def play(self, user_choice):
        computer_choice = random.choice(choices)
        winner = determine_winner(user_choice, computer_choice)
        
        result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"
        
        if winner == 'tie':
            result_text += "It's a tie!"
        elif winner == 'user':
            result_text += "You win!"
            self.user_score += 1
        else:
            result_text += "Computer wins!"
            self.computer_score += 1
        
        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
