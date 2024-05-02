import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from Recommender import Recommender

class RecommenderGUI:
    Recommender = Recommender()
    def __init__(self, main):
        self.main = main
        self.main.title("Media Recommender")
        self.main.geometry("1200x800")

        self.button_frame = tk.Frame(self.main)
        self.button_frame.pack(side="bottom", pady=5)
        self.button1 = tk.Button(self.button_frame, text='Load Shows')
        self.button1.pack(side="left", padx=80)
        self.button2 = tk.Button(self.button_frame, text='Load Books')
        self.button2.pack(side="left", padx=100)
        self.button3 = tk.Button(self.button_frame, text='Load Recommendations')
        self.button3.pack(side="left", padx=50)
        self.button4 = tk.Button(self.button_frame, text='Information')
        self.button4.pack(side="left", padx=100)
        self.button5 = tk.Button(self.button_frame, text='Quit')
        self.button5.pack(side="left", padx=30)

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

        # Tab 1 Movies Construction
        self.tab1.grid_columnconfigure(0, weight=1)
        self.tab1.grid_rowconfigure(0, weight=1)
        self.tab1.grid_rowconfigure(1, weight=1)

        self.text_area = scrolledtext.ScrolledText(self.tab1, state='disabled')
        self.text_area.grid(row=0, column=0, sticky="nsew")

        initial_text = "This is a non-editable text area."
        self.text_area.configure(state='normal')
        self.text_area.insert('end', initial_text)
        self.text_area.configure(state='disabled')

        self.text_area2 = tk.Text(self.tab1)
        self.text_area2.grid(row=1, column=0, sticky="nsew")

        self.text_area2.insert(tk.END, "poopy")


def main():
    root = tk.Tk()
    app = RecommenderGUI(root)
    root.mainloop()

main()
