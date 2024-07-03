import tkinter as tk
from tkinter import ttk, messagebox

# Expanded dataset for demonstration
items = {
    # Movies
    'The Shawshank Redemption': {'Type': 'Movie', 'Genre': 'Drama', 'Rating': 4.9},
    'The Godfather': {'Type': 'Movie', 'Genre': 'Drama', 'Rating': 4.8},
    'The Dark Knight': {'Type': 'Movie', 'Genre': 'Action', 'Rating': 4.7},
    'Pulp Fiction': {'Type': 'Movie', 'Genre': 'Crime', 'Rating': 4.6},
    'Forrest Gump': {'Type': 'Movie', 'Genre': 'Drama', 'Rating': 4.5},
    'Mad Max: Fury Road': {'Type': 'Movie', 'Genre': 'Action', 'Rating': 4.3},
    'Inception': {'Type': 'Movie', 'Genre': 'Sci-Fi', 'Rating': 4.6},
    'The Matrix': {'Type': 'Movie', 'Genre': 'Sci-Fi', 'Rating': 4.7},
    'Fight Club': {'Type': 'Movie', 'Genre': 'Drama', 'Rating': 4.5},
    'The Lion King': {'Type': 'Movie', 'Genre': 'Animation', 'Rating': 4.4},
    
    # Books
    '1984': {'Type': 'Book', 'Genre': 'Dystopian', 'Rating': 4.5},
    'To Kill a Mockingbird': {'Type': 'Book', 'Genre': 'Drama', 'Rating': 4.6},
    'The Great Gatsby': {'Type': 'Book', 'Genre': 'Classic', 'Rating': 4.4},
    'Moby Dick': {'Type': 'Book', 'Genre': 'Adventure', 'Rating': 4.1},
    'War and Peace': {'Type': 'Book', 'Genre': 'Historical', 'Rating': 4.2},
    'Brave New World': {'Type': 'Book', 'Genre': 'Dystopian', 'Rating': 4.3},
    'The Catcher in the Rye': {'Type': 'Book', 'Genre': 'Classic', 'Rating': 4.0},
    'Harry Potter and the Sorcerer\'s Stone': {'Type': 'Book', 'Genre': 'Fantasy', 'Rating': 4.7},
    'The Hobbit': {'Type': 'Book', 'Genre': 'Fantasy', 'Rating': 4.8},
    'The Da Vinci Code': {'Type': 'Book', 'Genre': 'Thriller', 'Rating': 4.3},
    
    # Songs
    'Bohemian Rhapsody': {'Type': 'Song', 'Genre': 'Rock', 'Rating': 4.9},
    'Stairway to Heaven': {'Type': 'Song', 'Genre': 'Rock', 'Rating': 4.8},
    'Hotel California': {'Type': 'Song', 'Genre': 'Rock', 'Rating': 4.7},
    'Blinding Lights': {'Type': 'Song', 'Genre': 'Pop', 'Rating': 4.6},
    'Shape of You': {'Type': 'Song', 'Genre': 'Pop', 'Rating': 4.5},
    'Bad Guy': {'Type': 'Song', 'Genre': 'Pop', 'Rating': 4.4},
    'Lose Yourself': {'Type': 'Song', 'Genre': 'Hip-Hop', 'Rating': 4.8},
    'Sicko Mode': {'Type': 'Song', 'Genre': 'Hip-Hop', 'Rating': 4.7},
    'Old Town Road': {'Type': 'Song', 'Genre': 'Country', 'Rating': 4.5},
    'Jolene': {'Type': 'Song', 'Genre': 'Country', 'Rating': 4.4}
}

class RecommendationSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recommendation System")
        self.root.geometry("600x500")
        
        # Title Label
        self.title_label = tk.Label(self.root, text="Recommendation System", font=('Helvetica', 24, 'bold'))
        self.title_label.pack(pady=20)
        
        # User Input Frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Select Type:").grid(row=0, column=0, padx=10, pady=10)
        self.type_var = tk.StringVar()
        self.type_combobox = ttk.Combobox(input_frame, textvariable=self.type_var, values=['Movie', 'Book', 'Song'], state='readonly')
        self.type_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.type_combobox.current(0)  # Default selection
        
        tk.Label(input_frame, text="Select Genre:").grid(row=1, column=0, padx=10, pady=10)
        self.genre_var = tk.StringVar()
        self.genre_combobox = ttk.Combobox(input_frame, textvariable=self.genre_var, values=['Drama', 'Action', 'Crime', 'Sci-Fi', 'Animation', 'Dystopian', 'Classic', 'Adventure', 'Historical', 'Fantasy', 'Thriller', 'Rock', 'Pop', 'Hip-Hop', 'Country'], state='readonly')
        self.genre_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.genre_combobox.current(0)  # Default selection
        
        tk.Label(input_frame, text="Minimum Rating:").grid(row=2, column=0, padx=10, pady=10)
        self.rating_var = tk.DoubleVar()
        self.rating_scale = tk.Scale(input_frame, from_=0, to=5, resolution=0.1, orient=tk.HORIZONTAL, variable=self.rating_var)
        self.rating_scale.grid(row=2, column=1, padx=10, pady=10)
        
        # Recommendation Button
        self.recommend_button = tk.Button(self.root, text="Get Recommendations", command=self.get_recommendations, bg="#FFD700", fg="#2E2E2E", font=('Arial', 14, 'bold'))
        self.recommend_button.pack(pady=10)
        
        # Result Frame
        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(pady=20)
        
        self.result_label = tk.Label(self.result_frame, text="", justify='left', anchor='nw', font=('Arial', 12))
        self.result_label.pack()

    def get_recommendations(self):
        item_type = self.type_var.get()
        genre = self.genre_var.get()
        min_rating = self.rating_var.get()
        
        recommendations = []
        for title, info in items.items():
            if info['Type'] == item_type and info['Genre'] == genre and info['Rating'] >= min_rating:
                recommendations.append(f"{title} ({info['Type']}, {info['Genre']}, Rating: {info['Rating']})")
        
        if recommendations:
            self.result_label.config(text="\n".join(recommendations))
        else:
            messagebox.showinfo("No Recommendations", f"No {item_type}s in {genre} genre with rating >= {min_rating}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecommendationSystemApp(root)
    root.mainloop()

