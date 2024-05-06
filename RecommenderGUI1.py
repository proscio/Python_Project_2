import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from Recommender import Recommender
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RecommenderGUI:
    def __init__(self, main):
        """
        This class creates a GUI for a Media Recommender system.
        It uses the tkinter library for the GUI and a Recommender object for the recommendation logic.
        """
        self.main = main
        self.main.title("Media Recommender")
        self.main.geometry("1200x800")

        self.recommender = Recommender()

        self.button_frame = tk.Frame(self.main)
        self.button_frame.pack(side="bottom", pady=5)
        self.button1 = tk.Button(self.button_frame, text='Load Shows', command=self.load_shows)
        self.button1.pack(side="left", padx=70)
        self.button2 = tk.Button(self.button_frame, text='Load Books' , command=self.load_books)
        self.button2.pack(side="left", padx=70)
        self.button3 = tk.Button(self.button_frame, text='Load Recommendations', command=self.load_associations)
        self.button3.pack(side="left", padx=70)
        self.button4 = tk.Button(self.button_frame, text='Information', command=self.info)
        self.button4.pack(side="left", padx=70)
        self.button5 = tk.Button(self.button_frame, text='Quit', command=main.destroy)
        self.button5.pack(side="left", padx=70)

        self.notebook = ttk.Notebook(self.main)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)
        self.tab5 = ttk.Frame(self.notebook)
        self.tab6 = ttk.Frame(self.notebook)
        self.tab7 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Movies")
        self.notebook.add(self.tab2, text="TV Shows")
        self.notebook.add(self.tab3, text="Books")
        self.notebook.add(self.tab4, text="Search Movies/TV")
        self.notebook.add(self.tab5, text="Search Books")
        self.notebook.add(self.tab6, text="Recommendations")
        self.notebook.add(self.tab7, text="Ratings")

        self.notebook.pack(expand=1, fill="both")

        # Call the function to create tabs initially
        self.update_tabs()


    def update_tabs(self):
        """
        Updates the tabs by creating them and loading the data.

        :return: None
        """
        try:
            self.create_tab(self.tab1, "Movies", self.recommender.getMovieList(), self.recommender.getMovieStats())
        except:
            self.create_tab(self.tab1, "Movies", "No Values Loaded", "No Values Loaded")

        try:
            self.create_tab(self.tab2, "TV Shows", self.recommender.getTVList(), self.recommender.getTVStats())
        except:
            self.create_tab(self.tab2, "TV Shows", "No Values Loaded", "No Values Loaded")

        try:
            self.create_tab(self.tab3, "Books", self.recommender.getBookList(), self.recommender.getBookStats())
        except:
            self.create_tab(self.tab3, "Books", "No Values Loaded", "No Values Loaded")
        self.search_books()
        self.search_TVMovies()
        self.getRecommendations()

    def create_tab(self, tab, tab_name, data_list, stats):
        """
        Create a tab in the notebook.
        :param tab: The tab to be created.
        :type tab: ttk.Frame
        :param tab_name: The name of the tab.
        :type tab_name: str
        :param data_list: The list of data to be displayed in the tab.
        :type data_list: str
        :param stats: The statistics to be displayed in the tab.
        :type stats: str
        """
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(0, weight=1)
        tab.grid_rowconfigure(1, weight=1)

        text_area1 = scrolledtext.ScrolledText(tab)
        text_area1.grid(row=0, column=0, sticky="nsew")

        text_area1.insert('end', data_list)
        text_area1.configure(state='disabled')

        text_area2 = tk.Text(tab)
        text_area2.grid(row=1, column=0, sticky="nsew")

        text_area2.insert('end', stats)
        text_area2.configure(state='disabled')

    def search_TVMovies(self):
        """
        Creates the "Search TV/Movies" tab.

        :return: None
        """
        self.tab4.grid_columnconfigure(0, weight=1)
        self.tab4.grid_columnconfigure(1, weight=1)
        self.tab4.grid_columnconfigure(2, weight=1)

        self.tab4.grid_rowconfigure(0, weight=1)
        self.tab4.grid_rowconfigure(1, weight=1)
        self.tab4.grid_rowconfigure(2, weight=1)
        self.tab4.grid_rowconfigure(3, weight=1)

        type_label = tk.Label(self.tab4, text="Type:")
        type_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        type_entry = ttk.Combobox(self.tab4, values=["Movie", "TV Show"])
        type_entry.grid(row=0, column=0, padx=10, pady=10)

        title_label = tk.Label(self.tab4, text="Title:")
        title_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        title_entry = tk.Entry(self.tab4, width=10)
        title_entry.grid(row=1, column=0, padx=10, pady=10)

        director_label = tk.Label(self.tab4, text="Director:")
        director_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        director_entry = tk.Entry(self.tab4, width=10)
        director_entry.grid(row=2, column=0, padx=10, pady=10)

        actor_label = tk.Label(self.tab4, text="Actor:")
        actor_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        actor_entry = tk.Entry(self.tab4, width=10)
        actor_entry.grid(row=3, column=0, padx=10, pady=10)

        genre_label = tk.Label(self.tab4, text="Genre:")
        genre_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        genre_entry = tk.Entry(self.tab4, width=10)
        genre_entry.grid(row=4, column=0, padx=10, pady=10)

        def perform_search():
            """
            Perform the search based on the user's input.
            This function is called when the user clicks the Search button.
            """
            type = type_entry.get()
            title = title_entry.get().lower()
            director = director_entry.get().lower()
            actor = actor_entry.get().lower()
            genre = genre_entry.get().lower()
            search_results = self.recommender.searchTVMovies(type=type, title=title, director=director, actor=actor,
                                                             genre=genre)
            self.search_TVMovies_results_text.delete('1.0', 'end')
            self.search_TVMovies_results_text.insert('end', search_results)

        search_button = tk.Button(self.tab4, text="Search", command=perform_search)
        search_button.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        self.search_TVMovies_results_text = scrolledtext.ScrolledText(self.tab4)
        self.search_TVMovies_results_text.grid(row=5, column=0, sticky="nsew", columnspan=3)

    
    def search_books(self):
        """
        Creates the "Search Books" tab.

        :return: None
        """
        self.tab5.grid_columnconfigure(0, weight=1)
        self.tab5.grid_columnconfigure(1, weight=1)
        self.tab5.grid_columnconfigure(2, weight=1)

        self.tab5.grid_rowconfigure(0, weight=1)
        self.tab5.grid_rowconfigure(1, weight=1)
        self.tab5.grid_rowconfigure(2, weight=1)
        self.tab5.grid_rowconfigure(3, weight=1)

        title_label = tk.Label(self.tab5, text="Title:")
        title_label.grid(row=0, column=0, padx=5, pady=5, sticky = 'w')
        title_entry = tk.Entry(self.tab5, width=10,)
        title_entry.grid(row =0, column=0, padx = 10, pady = 10)
        
        
        author_label = tk.Label(self.tab5, text="Author:")
        author_label.grid(row=1, column=0, padx=5, pady=5, sticky = 'w')
        author_entry = tk.Entry(self.tab5, width=10)
        author_entry.grid(row =1, column=0, padx = 10, pady = 10)

        publisher_label = tk.Label(self.tab5, text = "Publisher")
        publisher_label.grid(row=2, column=0, padx=5, pady=5, sticky = 'w')
        publisher_entry = tk.Entry(self.tab5, width=10)
        publisher_entry.grid(row =2, column=0, padx = 10, pady = 10)

        def perform_search():
            title = title_entry.get().lower()
            author = author_entry.get().lower()
            publisher = publisher_entry.get().lower()
            search_results = self.recommender.searchBooks(title=title, author=author, publisher=publisher)
            self.search_results_text.delete('1.0', 'end')
            self.search_results_text.insert('end', search_results)

        search_button = tk.Button(self.tab5, text="Search", command=perform_search)
        search_button.grid(row = 2,column=1, sticky="w", padx = 10, pady = 10)

        self.search_results_text = scrolledtext.ScrolledText(self.tab5)
        self.search_results_text.grid(row = 3, column=0, sticky="nsew", columnspan= 3)

    def getRecommendations(self):
        """
        Creates the "Recommendations" tab.

        :return: None
        """
        self.tab6.grid_columnconfigure(0, weight=1)
        self.tab6.grid_columnconfigure(1, weight=3)

        self.tab6.grid_rowconfigure(0, weight=1)
        self.tab6.grid_rowconfigure(1, weight=1)
        self.tab6.grid_rowconfigure(2, weight=1)

        type_label = tk.Label(self.tab6, text="Type:")
        type_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        type_entry = ttk.Combobox(self.tab6, values=["Movie", "TV Show", "Book"], width=15)
        type_entry.grid(row=0, column=0, padx=10, pady=10)

        title_label = tk.Label(self.tab6, text="Title:")
        title_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        title_entry = tk.Entry(self.tab6, width=20)
        title_entry.grid(row=1, column=0, padx=10, pady=10)

        def perform_search():
            type = type_entry.get()
            title = title_entry.get().lower()
            search_results = self.recommender.getRecommendations(type=type, title=title)
            self.search_recommendations_results_text.delete('1.0', 'end')
            self.search_recommendations_results_text.insert('end', search_results)

        search_button = tk.Button(self.tab6, text="Get Recommendations", command=perform_search)
        search_button.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        self.search_recommendations_results_text = scrolledtext.ScrolledText(self.tab6)
        self.search_recommendations_results_text.grid(row=3, column=0, columnspan=2, sticky="nsew")

    def RatingsTab(self):
        """
        This method creates the "Ratings" tab in the GUI. It displays pie charts for the distribution of movie and TV show ratings.
    
        :return: None
        """
        for widget in self.tab7.winfo_children():
            widget.destroy()

        ratings_movies, ratings_tv_shows = (), ()
        ratings_movies, ratings_tv_shows = self.recommender.Ratings()

        self.tab7.grid_columnconfigure(0, weight=1)
        self.tab7.grid_rowconfigure(0, weight=1)

        canvas = FigureCanvasTkAgg(Figure(), master=self.tab7)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill='both', expand=True)

        ax1 = canvas.figure.add_subplot(121)
        sizes1, labels1 = ratings_movies
        ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=140)
        ax1.set_title('Distribution of Movie Ratings')

        ax2 = canvas.figure.add_subplot(122)
        sizes2, labels2 = ratings_tv_shows
        ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=140)
        ax2.set_title('Distribution of TV Show Ratings')

    def info(self):
        """
        Displays an information message box.

        :return: The return value of the messagebox.showinfo function.
        :rtype: str
        """
        return messagebox.showinfo(title="Media for you!", message="Developed for: Engineering Programming Python\nBy: Gage Iannitelli, Rigoberto Perdomo, and Patrick Roscio\n Date finished: 5-5-2024")

    def load_shows(self):
        """
        Loads TV shows using the Recommender object and updates the tabs.

        :return: None
        """
        self.recommender.loadShows()
        self.update_tabs()
        self.RatingsTab()

    def load_books(self):
        """
        Loads books using the Recommender object and updates the tabs.

        :return: None
        """
        self.recommender.loadBooks()
        self.update_tabs()

    def load_associations(self):
        """
        Loads associations using the Recommender object and updates the tabs.

        :return: None
        """
        self.recommender.loadAssociations()
        self.update_tabs()

def main():
    """
    The main function of the program.
    This function creates a root window and an instance of the RecommenderGUI class,
    and then starts the main event loop.
    
    :return: None
    """
    root = tk.Tk()
    app = RecommenderGUI(root)
    root.mainloop()

main()
