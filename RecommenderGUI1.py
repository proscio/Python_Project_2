import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from Recommender import Recommender

class RecommenderGUI:
    def __init__(self, main):
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

        self.notebook.add(self.tab1, text="Movies")
        self.notebook.add(self.tab2, text="TV Shows")
        self.notebook.add(self.tab3, text="Books")
        self.notebook.add(self.tab4, text="Search Movies/TV")
        self.notebook.add(self.tab5, text="Search Books")
        self.notebook.add(self.tab6, text="Recommendations")

        self.notebook.pack(expand=1, fill="both")

        # Call the function to create tabs initially
        self.update_tabs()

    def update_tabs(self):
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

    def create_tab(self, tab, tab_name, data_list, stats):
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

    def info(self):
        return messagebox.showinfo(title="Media for you!", message="Developed for: Engineering Programming Python\nBy: Gage Iannitelli, Rigoberto Perdomo, and Patrick Roscio")

    def load_shows(self):
        self.recommender.loadShows()
        self.update_tabs()

    def load_books(self):
        self.recommender.loadBooks()
        self.update_tabs()

    def load_associations(self):
        self.recommender.loadAssociations()
        self.update_tabs()

def main():
    root = tk.Tk()
    app = RecommenderGUI(root)
    root.mainloop()

main()
