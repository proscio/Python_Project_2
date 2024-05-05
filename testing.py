import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ratings_list1 = ['TV-14', '16+', 'ALL', '', 'ALL', 'ALL', 'TV-14', '16+', 'NR', '13+', 'TV-Y7', 'TV-14', 'TV-NR', 'NR', '16+', 'TV-14', 'TV-PG', '18+', 'TV-Y7', '7+', '13+', 'ALL', 'ALL', 'ALL', '13+', 'TV-14', 'TV-14', 'TV-14', '13+', 'TV-14', '13+', 'TV-Y', '13+', '16+', 'ALL', '16+', 'ALL', '18+', 'TV-PG', '13+', 'NR', 'TV-Y', 'TV-14', 'TV-NR', '', '16+', '7+', '13+', 'TV-14', 'TV-Y', 'ALL', 'ALL', '16+', '18+', 'ALL', '7+', '7+', '7+', 'TV-Y7', 'TV-14', '13+', '16+', 'TV-PG', 'ALL', '16+', 'TV-Y', '16+', 'TV-14', 'TV-PG', 'TV-G', 'TV-PG', 'TV-MA', 'TV-14', 'ALL', 'TV-MA', 'TV-NR', '7+', '18+', 'ALL', 'TV-Y', 'TV-14', '13+', '18+', '18+', '18+', 'ALL', 'TV-14', 'TV-14', 'TV-PG', 'ALL', 'TV-PG', 'TV-MA', '16+', 'ALL', 'TV-PG', '16+', 'ALL', 'TV-14', 'TV-Y7', '13+', '13+', 'TV-PG', 'TV-PG', '13+', 'ALL', 'TV-MA', 'TV-G', '13+', '13+', '18+', 'ALL', 'TV-Y', '13+', 'TV-PG', 'TV-14', 'ALL', '13+', '16+', 'TV-NR', '16+', 'ALL', 'TV-14', '7+', '13+', '16+', '16+', 'ALL', 'TV-14', 'TV-14', '13+', 'TV-14', '16+', 'ALL', '18+', '', 'NR', 'TV-NR', '13+', 'ALL', 'NR', 'TV-Y', 'TV-Y', 'TV-14', 'TV-14', 'TV-14', '16+', 'TV-Y7', '18+', 'ALL', 'TV-PG', 'TV-14', 'ALL', '13+', 'ALL', 'ALL', 'TV-14', 'TV-NR', '16+', '16+', '13+', 'TV-14', 'TV-Y', '13+', '13+', 'ALL', '16+', '18+', 'ALL', '7+', 'ALL', 'TV-14', 'TV-G', 'TV-14', 'TV-14', '18+', 'TV-Y7', 'TV-PG', '7+', 'TV-14', 'ALL', 'TV-Y7', 'TV-Y7', '13+', 'ALL', 'TV-14', 'ALL', '7+', 'ALL', '13+', 'TV-Y', 'TV-Y', 'ALL', '16+', 'TV-14', 'TV-MA', 'TV-14', 'TV-PG', 'TV-PG', 'TV-PG', 'TV-Y', '18+', 'ALL', '13+', 'TV-PG', 'ALL', 'TV-14', 'TV-PG', 'TV-Y', 'TV-14', 'TV-PG', 'ALL', '13+', 'ALL', 'TV-NR', 'TV-PG', 'TV-PG', 'TV-PG', '16+', 'TV-Y7', 'TV-Y', '13+', '13+', '16+', '16+', 'TV-Y', '18+', 'TV-G', 'TV-G', 'TV-MA', 'ALL', 'TV-Y7', '16+', 'TV-G', '16+', 'ALL', 'TV-PG', 'TV-NR', '7+', 'TV-PG', 'ALL', '13+', 'ALL', '16+', 'ALL', 'ALL', 'TV-14', 'ALL', 'TV-NR', 'TV-PG', 'TV-14', 'TV-PG', 'TV-G', 'TV-MA', 'TV-Y7', 'TV-14', '18+', 'TV-PG', 'ALL', 'ALL', '16+', 'TV-G', 'ALL', 'TV-PG', '18+', 'TV-G', 'TV-14', 'ALL', 'TV-Y', '13+', 'TV-PG', 'TV-PG', '13+', '13+', 'ALL', 'TV-Y', 'ALL', '16+', 'ALL', '13+', '13+', 'TV-G', '18+', 'ALL', 'ALL', '13+', 'ALL', '16+', 'TV-G', '13+', '16+', 'TV-NR', '7+', '18+', '13+', 'TV-14', '13+', 'TV-14', 'TV-PG', '16+', 'TV-PG', 'TV-14', 'TV-14', '16+', '16+', 'TV-PG', 'ALL', '16+', '18+', 'TV-Y', 'TV-14', 'TV-14', 'TV-MA', 'TV-PG', 'TV-14', 'TV-14', '13+', '7+', 'TV-Y', 'TV-14', 'NR', '16+', '16+', 'TV-PG', '16+', 'ALL', 'TV-14', 'TV-Y', 'ALL', 'TV-MA', 'TV-PG', 'ALL', 'TV-14', '13+', 'ALL', '13+', '16+', 'TV-PG', 'TV-14', 'TV-Y', 'ALL', 'ALL', '18+', 'ALL', '16+', 'TV-PG', 'TV-14', '13+', '13+', 'ALL', 'TV-NR', '16+', 'TV-G', 'TV-14', 'TV-14', 'TV-14', 'TV-NR', 'TV-PG', '16+', 'NR', 'TV-Y', 'ALL', 'TV-14', 'TV-PG', 'ALL', 'TV-NR', 'TV-NR', '13+', '16+', 'TV-Y', '13+', 'TV-PG', '13+', '7+', 'NR', 'TV-Y', 'TV-Y', 'TV-PG', 'TV-G', 'TV-14', '13+', '13+', 'ALL', 'TV-NR', 'TV-14', '18+', 'ALL', '18+', '16+', 'ALL', 'TV-PG', '16+', 'TV-14', 'TV-Y7', 'TV-MA', '13+', '7+', 'TV-Y', 'TV-14', 'TV-NR', 'TV-14', 'TV-G', 'ALL', '7+', 'TV-PG', '13+', 'ALL', '13+', '13+', 'TV-G', 'TV-14', 'TV-NR', 'ALL', 'TV-G', 'TV-14', '16+', 'TV-PG', 'TV-14', 'TV-14', 'TV-NR', 'ALL', 'TV-14', 'TV-14', '13+', 'TV-PG', 'ALL', 'ALL', '13+', '13+', 'ALL', '7+', '16+', 'ALL', '13+', '13+', 'TV-14', 'TV-NR', 'TV-14', 'TV-PG', '16+', 'TV-14', '13+', 'ALL', '7+', '7+', 'TV-PG', 'TV-NR', 'ALL', '18+', 'TV-PG', '13+', '7+', 'ALL', '18+', '18+', 'TV-PG', 'TV-14', 'ALL', 'TV-PG', '18+', '13+', 'TV-14', 'TV-PG', 'TV-G', 'TV-PG', 'TV-G', '18+', '16+', 'TV-NR', '7+', 'NR', '7+', 'TV-MA', 'TV-Y', 'TV-PG', 'ALL', 'ALL', '13+', 'ALL', 'TV-PG', '16+', '16+', '18+', '16+', 'ALL', 'TV-NR', 'TV-MA', 'NR', '7+', '13+', '16+', 'ALL', '7+', '16+', 'TV-PG', '18+', '13+', '16+', 'TV-14', '13+', '13+']
ratings_list2 = ['18+', 'ALL', '18+', 'ALL', 'ALL', 'PG-13', '16+', '16+', '16+', '16+', '16+', 'R', '', 'R', 'R', '18+', 'ALL', '13+', 'PG', 'NR', '18+', '13+', '16+', 'ALL', 'ALL', '18+', 'ALL', '18+', '13+', '16+', '13+', 'R', '18+', '16+', 'PG-13', '16+', '18+', '18+', 'PG-13', '13+', '18+', '18+', '16+', '13+', '13+', 'G', 'R', '18+', '13+', '13+', 'ALL', '18+', '16+', '13+', '18+', 'R', '13+', '13+', 'R', '18+', '13+', 'R', '13+', '', 'NR', 'R', 'R', '13+', 'R', '13+', '13+', 'ALL', '13+', 'PG', '18+', '13+', '18+', 'ALL', '18+', 'R', '13+', '16+', '16+', '16+', 'R', '18+', '', 'R', 'ALL', 'R', '18+', 'ALL', 'AGES_16_', '13+', 'ALL', '16+', '16+', '13+', '13+', '18+', 'PG-13', 'PG', '13+', '16+', '13+', '13+', 'R', '18+', 'R', 'ALL', 'ALL', '18+', '18+', '13+', '', '13+', '13+', '16+', '7+', 'ALL', '13+', '13+', 'NR', 'ALL', '13+', '18+', '18+', 'ALL', 'ALL', '13+', 'ALL', 'PG-13', 'ALL', '13+', '16+', '13+', '7+', '16+', '16+', '16+', '18+', '13+', '13+', '13+', '7+', '18+', 'NR', '18+', 'ALL', '16+', 'R', '16+', '7+', '18+', '16+', '7+', '16+', '18+', 'ALL', '', '18+', '13+', '16+', '18+', '', 'NR', 'PG', '', '7+', '18+', 'ALL', '13+', '16+', '18+', '18+', '13+', 'R', '16+', '18+', 'NR', 'R', '13+', '16+', '13+', '18+', '13+', '13+', 'ALL', 'ALL', '16+', '7+', '16+', 'R', '13+', 'PG-13', '13+', 'ALL', '18+', '18+', 'ALL', '16+', '16+', 'ALL', '13+', 'NR', 'R', '16+', 'ALL', '13+', 'ALL', '7+', '13+', '13+', '16+', 'ALL', '13+', '13+', '13+', '13+', '16+', 'PG', '16+', '18+', '13+', 'PG-13', '16+', '18+', 'R', '', '13+', 'ALL', '16+', '18+', '13+', 'R', '16+', 'R', 'ALL', '16+', '18+', 'ALL', '13+', '7+', 'PG-13', 'ALL', 'R', '18+', 'R', '18+', '7+', '7+', '18+', '7+', 'NR', 'ALL', '13+', 'ALL', '13+', '18+', '13+', 'NR', 'R', '18+', 'ALL', '13+', '13+', '13+', '13+', 'ALL', '13+', '16+', '13+', 'ALL', '16+', '13+', '13+', '7+', '', '7+', '18+', '16+', '16+', 'PG', 'PG', 'ALL', '13+', '7+', '18+', '16+', '13+', '7+', '16+', 'R', '7+', 'PG', '16+', '18+', '13+', '13+', 'R', '16+', '13+', '13+', '13+', '18+', '16+', 'ALL', '13+', '18+', 'ALL', '13+', 'ALL', 'ALL', '', '7+', '', 'NR', '18+', '13+', 'R', '16+', '13+', '13+', 'NR', '16+', 'ALL', '18+', '16+', '13+', 'NR', '13+', 'ALL', '13+', '16+', 'R', 'R', 'R', '13+', '13+', '13+', '13+', '16+', 'ALL', 'R', '18+', '18+', '13+', 'ALL', '', '13+', 'R', '16+', '13+', '13+', 'R', 'ALL', '13+', 'R', 'NR', '13+', 'R', 'NR', 'PG-13', 'ALL', 'PG-13', '18+', 'G', '7+', '18+', '13+', '16+', '13+', '18+', '16+', 'G', 'G', 'ALL', 'ALL', '7+', '16+', 'R', '13+', 'R', '18+', '16+', '', '16+', 'R', 'G', '16+', '18+', 'ALL', '13+', '18+', '', 'ALL', 'ALL', 'R', '16+', 'PG-13', 'ALL', '18+', 'ALL', 'ALL', '18+', '', '13+', '', 'NR', '13+', '18+', '13+', 'R', 'R', '18+', '16+', '13+', '13+', '16+', '18+', '7+', 'R', '16+', 'ALL', '13+', '7+', 'PG', 'ALL', 'ALL', 'ALL', 'ALL', 'PG-13', 'ALL', 'ALL', '13+', '', 'ALL', '13+', 'PG', '18+', '13+', 'ALL', '16+', '16+', '18+', '13+', '16+', 'ALL', '13+', '16+', 'PG-13', '16+', 'NR', 'ALL', '16+', 'ALL', '13+', 'ALL', '18+', 'PG', '13+', 'R', '16+', 'ALL', 'ALL', '', '16+', 'R', '13+', 'R', '18+', 'R', '13+', '16+', '', '16+', '13+', '16+', '18+', '16+', '13+', 'NR', '13+', 'G', '16+', '16+', '16+', '18+', '13+', '7+', '7+', 'ALL', '13+', 'NR', 'ALL', '7+', 'NR', '', '16+', 'ALL']

def create_pie_chart(ratings):
    rating_counts = {}
    total_ratings = 0
    for rating in ratings:
        if rating == '' or rating == 'TV-NR':
            rating = "NR"

        if rating in rating_counts:
            rating_counts[rating] += 1
        else:
            rating_counts[rating] = 1
        total_ratings += 1

    percentages = {rating: (count / total_ratings) * 100 for rating, count in rating_counts.items()}

    labels = list(percentages.keys())
    sizes = list(percentages.values())

    return sizes, labels

def display_gui():
    root = tk.Tk()
    root.title("Ratings Pie Chart")

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    frame = ttk.Frame(notebook)
    frame.pack(fill='both', expand=True)

    canvas = FigureCanvasTkAgg(Figure(), master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill='both', expand=True)

    ax1 = canvas.figure.add_subplot(121)
    sizes1, labels1 = create_pie_chart(ratings_list1)
    ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=140)
    ax1.set_title('Distribution of Ratings 1')

    ax2 = canvas.figure.add_subplot(122)
    sizes2, labels2 = create_pie_chart(ratings_list2)
    ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=140)
    ax2.set_title('Distribution of Ratings 2')

    notebook.add(frame, text='Pie Charts')

    root.mainloop()

display_gui()