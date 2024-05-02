import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from Recommender import Recommender


class RecommenderGUI:
    def __init__(self):
        self.recommender = Recommender()

        self.root = tk.Tk()
        self.root.title("Recommender")
        self.root.geometry("1200x800")

        self.notebook = ttk.Notebook(self.root)

        self.movie_tab = self.create_movie_tab()
        self.tv_show_tab = self.create_tv_show_tab()
        self.book_tab = self.create_book_tab()
        self.movie_tv_show_search_tab = self.create_movie_tv_show_search_tab()
        self.book_search_tab = self.create_book_search_tab()
        self.recommendation_tab = self.create_recommendation_tab()

        self.notebook.add(self.movie_tab, text="Movies")
        self.notebook.add(self.tv_show_tab, text="TV Shows")
        self.notebook.add(self.book_tab, text="Books")
        self.notebook.add(self.movie_tv_show_search_tab, text="Movie/TV Show Search")
        self.notebook.add(self.book_search_tab, text="Book Search")
        self.notebook.add(self.recommendation_tab, text="Recommendations")

        self.notebook.pack(expand=1, fill="both")

        self.load_shows_button = tk.Button(self.root, text="Load Shows", command=self.load_shows)
        self.load_books_button = tk.Button(self.root, text="Load Books", command=self.load_books)
        self.load_associations_button = tk.Button(self.root, text="Load Associations", command=self.load_associations)
        self.credit_info_button = tk.Button(self.root, text="Credit Info", command=self.credit_info)
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)

        self.load_shows_button.pack()
        self.load_books_button.pack()
        self.load_associations_button.pack()
        self.credit_info_button.pack()
        self.quit_button.pack()

    def create_movie_tab(self):
        pass

    def load_shows(self):
        self.recommender.loadShows()

    def load_books(self):
        self.recommender.loadBooks()

    def load_associations(self):
        self.recommender.loadAssociations()

    def credit_info(self):
        messagebox.showinfo("Credit Info", "Your team information")

    def run(self):
        self.root.mainloop()

    def loadShows(self):
        self.recommender.loadShows()
        movie_list, movie_stats = self.recommender.getMovieList(), self.recommender.getMovieStats()
        tv_show_list, tv_show_stats = self.recommender.getTVList(), self.recommender.getTVStats()

        self.movie_text.delete('1.0', tk.END)
        self.movie_text.insert(tk.END, movie_list)
        self.movie_text.insert(tk.END, movie_stats)

        self.tv_show_text.delete('1.0', tk.END)
        self.tv_show_text.insert(tk.END, tv_show_list)
        self.tv_show_text.insert(tk.END, tv_show_stats)

    def loadBooks(self):
        self.recommender.loadBooks()
        book_list, book_stats = self.recommender.getBookList(), self.recommender.getBookStats()

        self.book_text.delete('1.0', tk.END)
        self.book_text.insert(tk.END, book_list)
        self.book_text.insert(tk.END, book_stats)

    def loadAssociations(self):
        self.recommender.loadAssociations()

    def creditInfoBox(self):
        messagebox.showinfo("Credit Info", "Your team information")

    def searchShows(self):
        type = self.type_combobox.get()
        title = self.title_entry.get()
        director = self.director_entry.get()
        actor = self.actor_entry.get()
        genre = self.genre_entry.get()

        results = self.recommender.searchTVMovies(type, title, director, actor, genre)

        self.results_text.delete('1.0', tk.END)
        self.results_text.insert(tk.END, results)

    def searchBooks(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()

        results = self.recommender.searchBooks(title, author, publisher)

        self.results_text.delete('1.0', tk.END)
        self.results_text.insert(tk.END, results)

    def getRecommendations(self):
        type = self.type_combobox.get()
        title = self.title_entry.get()

        recommendations = self.recommender.getRecommendations(type, title)

        self.recommendations_text.delete('1.0', tk.END)
        self.recommendations_text.insert(tk.END, recommendations)

    def run(self):
        self.root.mainloop()


def main():
    RecommenderGUI()


main()
