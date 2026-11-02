import tkinter as tk
from tkinter import ttk, messagebox
import random

# ---------------------------------------------------------
# MOVIE RECOMMENDATION SYSTEM
# Improved version: search, genre filters, sorting, favorites
# ---------------------------------------------------------

MOVIES = [
    {"name": "Inception", "genre": "Action", "year": 2010},
    {"name": "War", "genre": "Action", "year": 2019},
    {"name": "Pathaan", "genre": "Action", "year": 2023},
    {"name": "Jawan", "genre": "Action", "year": 2023},
    {"name": "Dhoom 2", "genre": "Action", "year": 2006},
    {"name": "Avengers: Endgame", "genre": "Action", "year": 2019},
    {"name": "John Wick", "genre": "Action", "year": 2014},
    {"name": "Mission Impossible", "genre": "Action", "year": 1996},
    {"name": "KGF Chapter 2", "genre": "Action", "year": 2022},
    {"name": "Singham", "genre": "Action", "year": 2011},
    {"name": "3 Idiots", "genre": "Comedy", "year": 2009},
    {"name": "Hera Pheri", "genre": "Comedy", "year": 2000},
    {"name": "The Hangover", "genre": "Comedy", "year": 2009},
    {"name": "Welcome", "genre": "Comedy", "year": 2007},
    {"name": "Bhagam Bhag", "genre": "Comedy", "year": 2006},
    {"name": "Dhamaal", "genre": "Comedy", "year": 2007},
    {"name": "Chup Chup Ke", "genre": "Comedy", "year": 2006},
    {"name": "Golmaal", "genre": "Comedy", "year": 2006},
    {"name": "Housefull", "genre": "Comedy", "year": 2010},
    {"name": "Munna Bhai M.B.B.S.", "genre": "Comedy", "year": 2003},
    {"name": "Titanic", "genre": "Romance", "year": 1997},
    {"name": "Jab We Met", "genre": "Romance", "year": 2007},
    {"name": "Dilwale Dulhania Le Jayenge", "genre": "Romance", "year": 1995},
    {"name": "Aashiqui 2", "genre": "Romance", "year": 2013},
    {"name": "Veer-Zaara", "genre": "Romance", "year": 2004},
    {"name": "Yeh Jawaani Hai Deewani", "genre": "Romance", "year": 2013},
    {"name": "Rockstar", "genre": "Romance", "year": 2011},
    {"name": "Kal Ho Naa Ho", "genre": "Romance", "year": 2003},
    {"name": "The Notebook", "genre": "Romance", "year": 2004},
    {"name": "Sita Ramam", "genre": "Romance", "year": 2022},
    {"name": "The Conjuring", "genre": "Horror", "year": 2013},
    {"name": "Bhool Bhulaiyaa", "genre": "Horror", "year": 2007},
    {"name": "The Exorcist", "genre": "Horror", "year": 1973},
    {"name": "Annabelle", "genre": "Horror", "year": 2014},
    {"name": "IT", "genre": "Horror", "year": 2017},
    {"name": "Insidious", "genre": "Horror", "year": 2010},
    {"name": "Stree", "genre": "Horror", "year": 2018},
    {"name": "Bhoot", "genre": "Horror", "year": 2003},
    {"name": "The Nun", "genre": "Horror", "year": 2018},
    {"name": "Tumbbad", "genre": "Horror", "year": 2018},
    {"name": "Dangal", "genre": "Drama", "year": 2016},
    {"name": "Taare Zameen Par", "genre": "Drama", "year": 2007},
    {"name": "The Shawshank Redemption", "genre": "Drama", "year": 1994},
    {"name": "Forrest Gump", "genre": "Drama", "year": 1994},
    {"name": "12th Fail", "genre": "Drama", "year": 2023},
    {"name": "Chak De! India", "genre": "Drama", "year": 2007},
    {"name": "Swades", "genre": "Drama", "year": 2004},
    {"name": "Super 30", "genre": "Drama", "year": 2019},
    {"name": "The Pursuit of Happyness", "genre": "Drama", "year": 2006},
    {"name": "Bhaag Milkha Bhaag", "genre": "Drama", "year": 2013},
    {"name": "Interstellar", "genre": "Sci-Fi", "year": 2014},
    {"name": "The Matrix", "genre": "Sci-Fi", "year": 1999},
    {"name": "Avatar", "genre": "Sci-Fi", "year": 2009},
    {"name": "The Martian", "genre": "Sci-Fi", "year": 2015},
    {"name": "Gravity", "genre": "Sci-Fi", "year": 2013},
    {"name": "Drishyam", "genre": "Thriller", "year": 2015},
    {"name": "Andhadhun", "genre": "Thriller", "year": 2018},
    {"name": "Shutter Island", "genre": "Thriller", "year": 2010},
    {"name": "Gone Girl", "genre": "Thriller", "year": 2014},
    {"name": "Kahaani", "genre": "Thriller", "year": 2012},
    {"name": "Toy Story", "genre": "Animation", "year": 1995},
    {"name": "Finding Nemo", "genre": "Animation", "year": 2003},
    {"name": "Coco", "genre": "Animation", "year": 2017},
    {"name": "Inside Out", "genre": "Animation", "year": 2015},
    {"name": "Zootopia", "genre": "Animation", "year": 2016},
]

GENRES = ["All Genres"] + sorted({movie["genre"] for movie in MOVIES})


class MovieRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CineMatch | Movie Recommendation System")
        self.root.geometry("900x680")
        self.root.minsize(760, 600)
        self.root.configure(bg="#101827")
        self.favorites = set()
        self.current_results = []

        self.setup_styles()
        self.build_interface()
        self.show_movies(MOVIES, "Explore all movies")

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TCombobox",
            fieldbackground="#202d40",
            background="#202d40",
            foreground="#ffffff",
            arrowcolor="#f5c518",
            padding=8
        )
        style.map("TCombobox", fieldbackground=[("readonly", "#202d40")])
        style.configure(
            "Treeview",
            background="#172337",
            foreground="#f3f4f6",
            fieldbackground="#172337",
            rowheight=34,
            borderwidth=0,
            font=("Segoe UI", 10)
        )
        style.configure(
            "Treeview.Heading",
            background="#26364d",
            foreground="#f5c518",
            font=("Segoe UI", 10, "bold"),
            padding=9,
            relief="flat"
        )
        style.map("Treeview", background=[("selected", "#344b68")])

    def build_interface(self):
        header = tk.Frame(self.root, bg="#101827")
        header.pack(fill="x", padx=28, pady=(22, 8))

        tk.Label(
            header, text="CINEMATCH", bg="#101827", fg="#f5c518",
            font=("Segoe UI", 25, "bold")
        ).pack(anchor="w")
        tk.Label(
            header, text="Find your next favourite movie.",
            bg="#101827", fg="#b8c4d6", font=("Segoe UI", 11)
        ).pack(anchor="w", pady=(2, 0))

        filter_card = tk.Frame(self.root, bg="#1a2638", padx=18, pady=16)
        filter_card.pack(fill="x", padx=28, pady=14)

        tk.Label(filter_card, text="GENRE", bg="#1a2638", fg="#d7dfeb",
                 font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="w")
        self.genre_var = tk.StringVar(value="All Genres")
        self.genre_box = ttk.Combobox(
            filter_card, textvariable=self.genre_var, values=GENRES,
            state="readonly", width=18
        )
        self.genre_box.grid(row=1, column=0, padx=(0, 14), pady=(6, 0), sticky="ew")

        tk.Label(filter_card, text="SEARCH MOVIE", bg="#1a2638", fg="#d7dfeb",
                 font=("Segoe UI", 9, "bold")).grid(row=0, column=1, sticky="w")
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(
            filter_card, textvariable=self.search_var, bg="#202d40",
            fg="white", insertbackground="white", relief="flat",
            font=("Segoe UI", 10), width=28
        )
        self.search_entry.grid(row=1, column=1, padx=(0, 14), pady=(6, 0), ipady=9, sticky="ew")
        self.search_entry.insert(0, "")

        tk.Label(filter_card, text="SORT BY", bg="#1a2638", fg="#d7dfeb",
                 font=("Segoe UI", 9, "bold")).grid(row=0, column=2, sticky="w")
        self.sort_var = tk.StringVar(value="Name (A-Z)")
        self.sort_box = ttk.Combobox(
            filter_card, textvariable=self.sort_var,
            values=["Name (A-Z)", "Year (Newest)", "Year (Oldest)"],
            state="readonly", width=16
        )
        self.sort_box.grid(row=1, column=2, pady=(6, 0), sticky="ew")

        filter_card.grid_columnconfigure(1, weight=1)

        actions = tk.Frame(self.root, bg="#101827")
        actions.pack(fill="x", padx=28, pady=(0, 12))

        self.make_button(actions, "Find Movies", self.recommend_movies,
                         "#f5c518", "#101827").pack(side="left", padx=(0, 8))
        self.make_button(actions, "Surprise Me", self.surprise_me,
                         "#2e8bce", "white").pack(side="left", padx=8)
        self.make_button(actions, "Show Favourites", self.show_favorites,
                         "#344b68", "white").pack(side="left", padx=8)
        self.make_button(actions, "Reset", self.reset_filters,
                         "#344052", "white").pack(side="right")

        results_header = tk.Frame(self.root, bg="#101827")
        results_header.pack(fill="x", padx=28, pady=(8, 8))
        tk.Label(results_header, text="MOVIE LIBRARY", bg="#101827",
                 fg="white", font=("Segoe UI", 13, "bold")).pack(side="left")
        self.count_label = tk.Label(results_header, text="", bg="#101827",
                                    fg="#9eacc0", font=("Segoe UI", 9))
        self.count_label.pack(side="right")

        table_frame = tk.Frame(self.root, bg="#172337")
        table_frame.pack(fill="both", expand=True, padx=28, pady=(0, 10))

        columns = ("name", "genre", "year", "favorite")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings",
                                 selectmode="browse")
        self.tree.heading("name", text="MOVIE")
        self.tree.heading("genre", text="GENRE")
        self.tree.heading("year", text="YEAR")
        self.tree.heading("favorite", text="FAVOURITE")
        self.tree.column("name", width=430, anchor="w")
        self.tree.column("genre", width=150, anchor="center")
        self.tree.column("year", width=100, anchor="center")
        self.tree.column("favorite", width=110, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True, padx=(8, 0), pady=8)
        scrollbar.pack(side="right", fill="y", padx=(0, 8), pady=8)
        self.tree.bind("<Double-1>", self.toggle_selected_favorite)

        footer = tk.Frame(self.root, bg="#101827")
        footer.pack(fill="x", padx=28, pady=(0, 15))
        self.status_label = tk.Label(
            footer, text="Tip: Double-click a movie to add or remove it from favourites.",
            bg="#101827", fg="#9eacc0", font=("Segoe UI", 9)
        )
        self.status_label.pack(side="left")

    def make_button(self, parent, text, command, bg, fg):
        return tk.Button(
            parent, text=text, command=command, bg=bg, fg=fg,
            activebackground=bg, activeforeground=fg, relief="flat",
            bd=0, padx=16, pady=10, cursor="hand2",
            font=("Segoe UI", 9, "bold")
        )

    def show_movies(self, movie_list, heading):
        self.current_results = list(movie_list)
        for item in self.tree.get_children():
            self.tree.delete(item)

        for movie in movie_list:
            fav_mark = "★ Saved" if movie["name"] in self.favorites else "☆ Add"
            self.tree.insert(
                "", "end",
                values=(movie["name"], movie["genre"], movie["year"], fav_mark)
            )

        self.count_label.config(text=f"{len(movie_list)} movie(s) • {heading}")
        self.status_label.config(
            text="Double-click a movie row to toggle its favourite status."
        )

    def recommend_movies(self):
        selected_genre = self.genre_var.get()
        keyword = self.search_var.get().strip().lower()

        results = [
            movie for movie in MOVIES
            if (selected_genre == "All Genres" or movie["genre"] == selected_genre)
            and keyword in movie["name"].lower()
        ]

        sort_choice = self.sort_var.get()
        if sort_choice == "Year (Newest)":
            results.sort(key=lambda movie: movie["year"], reverse=True)
        elif sort_choice == "Year (Oldest)":
            results.sort(key=lambda movie: movie["year"])
        else:
            results.sort(key=lambda movie: movie["name"].lower())

        self.show_movies(results, "matching results")
        if not results:
            self.status_label.config(text="No movies found. Try another genre or search term.")

    def surprise_me(self):
        selected_genre = self.genre_var.get()
        pool = [m for m in MOVIES if selected_genre == "All Genres" or m["genre"] == selected_genre]
        if not pool:
            messagebox.showinfo("CineMatch", "No movies available for this genre.")
            return
        movie = random.choice(pool)
        messagebox.showinfo(
            "Your movie pick",
            f"Tonight's recommendation:\n\n{movie['name']}\n{movie['genre']} • {movie['year']}"
        )
        self.show_movies([movie], "surprise pick")

    def show_favorites(self):
        favorites = [movie for movie in MOVIES if movie["name"] in self.favorites]
        self.show_movies(favorites, "favourites")
        if not favorites:
            self.status_label.config(text="You have not saved any favourites yet. Double-click a movie to save it.")

    def toggle_selected_favorite(self, event=None):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        movie_name = values[0]
        if movie_name in self.favorites:
            self.favorites.remove(movie_name)
            message = f"Removed {movie_name} from favourites."
        else:
            self.favorites.add(movie_name)
            message = f"Added {movie_name} to favourites."
        self.status_label.config(text=message)
        self.recommend_movies()

    def reset_filters(self):
        self.genre_var.set("All Genres")
        self.search_var.set("")
        self.sort_var.set("Name (A-Z)")
        self.show_movies(MOVIES, "all movies")
        self.status_label.config(text="Filters have been reset.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MovieRecommendationApp(root)
    root.mainloop()
