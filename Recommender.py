import os
import tkinter.filedialog as filedialog
from tkinter import messagebox
from Book import Book
from Show import Show

class Recommender:
    def __init__(self):
        self.__books = {}
        self.__shows = {}
        self.__associations = {}

    def loadBooks(self):
        self.__books = {}
        file = filedialog.askopenfilename(title="Book File", initialdir=os.getcwd())
        with open(file, "r") as bookFile:
            next(bookFile)
            for line in bookFile:
                value = line.strip().split(",")
                newBook = Book(id=value[0], title=value[1], authors=value[2], averageRating=value[3], isbn=value[4],
                               isbn13=value[5], languageCode=value[6], pageCount=value[7], numRatings=value[8],
                               publicationDate=value[9], publisher=value[10])
                self.__books[value[0]] = newBook

    def loadShows(self):
        self.__shows = {}
        file = filedialog.askopenfilename(title="Show File", initialdir=os.getcwd())
        with open(file, "r") as showFile:
            next(showFile)
            for line in showFile:
                value = line.strip().split(",")
                if value[0] == 'show_id':
                    continue
                newShow = Show(id=value[0], typeShow=value[1], title=value[2], directors=value[3], actors=value[4],
                               averageRating=value[5], countryCode=value[6], dateAired=value[7], releaseYear=value[8],
                               rating=value[9], duration=value[10], genres=value[11], description=value[12])
                self.__shows[value[0]] = newShow

    def loadAssociations(self):
        self.__associations = {}
        file = filedialog.askopenfilename(title="Association File", initialdir=os.getcwd())
        with open(file, "r") as associationFile:
            for line in associationFile:
                value = line.strip().split(",")
                if value[0] not in self.__associations:
                    self.__associations[value[0]] = {value[1]: 1}
                else:
                    if value[1] in self.__associations[value[0]]:
                        self.__associations[value[0]][value[1]] += 1
                    else:
                        self.__associations[value[0]][value[1]] = 1
                if value[1] not in self.__associations:
                    self.__associations[value[1]] = {value[0]: 1}
                else:
                    if value[0] in self.__associations[value[1]]:
                        self.__associations[value[1]][value[0]] += 1
                    else:
                        self.__associations[value[1]][value[0]] = 1

    def getMovieList(self):
        string = ""
        width = 0
        for i in self.__shows:
            if Show.getTypeShow(self.__shows[i]) == "Movie":
                title_length = len(Show.getTitle(self.__shows[i]))
                if title_length > width:
                    width = title_length
        padding = " " * (width-(len("Title")+1))    
        string += f"Title:{padding} | Duration:"
        for i in self.__shows:
            if Show.getTypeShow(self.__shows[i]) == "Movie":
                data = ""  
                title = Show.getTitle(self.__shows[i])
                duration = Show.getDuration(self.__shows[i])
                title_length = len(title)
                padding = " " * (width - title_length)    
                data = f"\n{title}{padding} | {duration:10}"
                string += data
        return string


    def getTVList(self):
        string = ""
        width = 0
        for i in self.__shows:
            if Show.getTypeShow(self.__shows[i]) == "TV Show":
                title_length = len(Show.getTitle(self.__shows[i]))
                if title_length > width:
                    width = title_length
        padding = " " * (width-(len("Title")+1))    
        string += f"Title:{padding} | Duration:"
        for i in self.__shows:
            if Show.getTypeShow(self.__shows[i]) == "TV Show":
                data = ""  
                title = Show.getTitle(self.__shows[i])
                duration = Show.getDuration(self.__shows[i])
                title_length = len(title)
                padding = " " * (width - title_length)    
                data = f"\n{title}{padding} | {duration:10}"
                string += data
        return string

    def getBookList(self):
        string = ""
        width = 0
        for i in self.__books:
            title_length = len(Book.getTitle(self.__books[i]))
            if title_length > width:
                width = title_length
        padding = " " * (width-(len("Title")+1))    
        string += f"Title:{padding} | Author:"
        for i in self.__books:
            data = ""
            title = Book.getTitle(self.__books[i])
            author = Book.getAuthors(self.__books[i])
            title_length = len(title)
            padding = " " * (width - title_length)    
            data = f"\n{title}{padding} | {author}"
            string += data
        return string

    def getMovieStats(self):
        Rating_list, Duration_List, Director_list, Actor_list, Genre_list = [], [], [], [], []
        for i in self.__shows:
            if Show.getTypeShow(self.__shows[i]) == "Movie":
                Rating_list.append(Show.getRating(self.__shows[i]))
                Duration_List.append(Show.getDuration(self.__shows[i]))
                Director_list.append(str(Show.getDirectors(self.__shows[i])).strip().split("\\"))
                Actor_list.append(str(Show.getActors(self.__shows[i])).strip().split("\\"))
                Genre_list.append(str(Show.getGenres(self.__shows[i])).strip().split("\\"))

        def most_frequent(list):
            freq_dict = {}
            for i in list:
                for j in i:
                    if j.strip():
                        if j in freq_dict:
                            freq_dict[j] += 1
                        else:
                            freq_dict[j] = 1
                most_frequent = max(freq_dict, key=freq_dict.get)
            return most_frequent

        def frequencies(list):
            ratings = {"R": 0, "ALL": 0, "18+": 0, "7+": 0, "13+": 0, "16+": 0, "None": 0, "NR": 0, "PG-13": 0, "G": 0, "PG": 0, "AGES_16_": 0}
            ratingString = "Ratings:\n"
            for i in list:
                if i == "":
                    i = 'None'
                ratings[i] += 1

            for i in ratings:
                if ratings[i] != 0:
                    ratingString += (i + " " + f"{float((ratings[i] / len(list))*100):.2f}" + "%\n")
            return ratingString

        def mean(list):
            total_sum = 0
            for i in list:
                total_sum += int(i.split(' ')[0])
            average = total_sum / len(list)
            return average

        return f"{frequencies(Rating_list)}\nAverage Movie Duration:{mean(Duration_List): .2f} minutes\n\nMost Prolific Director: {most_frequent(Director_list)}\n\nMost Prolific Actor: {most_frequent(Actor_list)}\n\nMost Frequent Genre: {most_frequent(Genre_list)}"

    def getTVStats(self):
        Rating_list, Duration_List, Actor_list, Genre_list = [], [], [], []
        for i in self.__shows:
            if Show.getTypeShow(self.__shows[i]) == "TV Show":
                Rating_list.append(Show.getRating(self.__shows[i]))
                Duration_List.append(Show.getDuration(self.__shows[i]))
                Genre_list.append(str(Show.getGenres(self.__shows[i])).strip().split("\\"))
                Actor_list.append(str(Show.getActors(self.__shows[i])).strip().split("\\"))

        def most_frequent(list):
            freq_dict = {}
            for i in list:
                for j in i:
                    if j in freq_dict:
                        freq_dict[j] += 1
                    else:
                        freq_dict[j] = 1
            most_frequent = max(freq_dict, key=freq_dict.get)
            return most_frequent
        
        def frequencies(list):
            ratings = {"7+": 0, "TV-14": 0, "13+": 0, "TV-Y": 0, "ALL": 0, "TV-NR": 0, "18+": 0, "TV-Y7": 0, "16+": 0, "TV-G": 0, "TV-PG": 0, "None": 0, "NR": 0, "TV-MA": 0}
            ratingString = f"Ratings:\n"
            for i in list:
                print(i)
                if i == "" or i == "NR":
                    i = 'None'
                ratings[i] += 1

            for i in ratings:
                if ratings[i] != 0:
                    ratingString += (i + " " + f"{float((ratings[i] / len(list))*100):.2f}" + "%\n")
            return ratingString

        def mean(list):
            total_sum = 0
            for i in list:
                h = int(i.split(' ')[0])
                total_sum += h
            average = total_sum / len(list)
            return average

        return f"{frequencies(Rating_list)}\nAverage Number of Seasons: {mean(Duration_List): .2f} seasons\n\nMost Prolific Actor: {most_frequent(Actor_list)}\n\nMost Frequent Genre: {most_frequent(Genre_list)}"

    def getBookStats(self):
        PageCount_list, Author_list, Publisher_list = [], [], []
        for i in self.__books:
            PageCount_list.append(Book.getPageCount(self.__books[i]))
            Author_list.append(Book.getAuthors(self.__books[i]))
            Publisher_list.append(Book.getPublisher(self.__books[i]))
        print(Author_list)

        def most_frequent(list):
            freq_dict = {}
            print(list)
            for i in list:
                print(i)
                if i in freq_dict:
                    freq_dict[i] += 1
                    print(freq_dict[i])
                else:
                    freq_dict[i] = 1
            most_frequent = max(freq_dict, key=freq_dict.get)
            return most_frequent

        def mean(list):
            total_sum = 0
            for i in list:
                total_sum += int(i)
            average = total_sum / len(list)
            return average

        return f"Average Page Count:{mean(PageCount_list): .2f} pages\n\nMost Prolific Author: {most_frequent(Author_list)}\n\nMost Prolific Publisher: {most_frequent(Publisher_list)}"

    def searchTVMovies(self, type, title, director, actor, genre):
        if type not in ["Movie", "TV Show"]:
            messagebox.showerror("Error", "Please select 'Movie' or 'TV Show' from Type.")
            return "No Results"

        if not (title or director or actor or genre):
            messagebox.showerror("Error", "Please enter information for Title, Director, Actor, and/or Genre.")
            return "No Results"

        results = ""
        for show_id, show in self.__shows.items():
            if (type == "Movie" and show.getTypeShow() == "Movie") or (type == "TV Show" and show.getTypeShow() == "TV Show"):
                if (not title or title.lower() in show.getTitle().lower()) and \
                   (not director or director.lower() in show.getDirectors().lower()) and \
                   (not actor or actor.lower() in show.getActors().lower()) and \
                   (not genre or genre.lower() in show.getGenres().lower()):

                    results += f"Title: {show.getTitle()}\n"
                    results += f"Director: {show.getDirectors()}\n"
                    results += f"Actors: {show.getActors()}\n"
                    results += f"Genre: {show.getGenres()}\n"
        if not results:
            return "No Results"
        return results

    def searchBooks(self, title, author, publisher):
        if not (title or author or publisher):
            messagebox.showerror("Error", "Please enter information for Title, Author, and/or Publisher.")
            return "No Results"

        results = ""
        for book_id, book in self.__books.items():
            if title not in Book.getTitle(book).lower():
                continue
            elif author not in Book.getAuthors(book).lower():
                continue
            elif publisher not in Book.getPublisher(book).lower():
                continue

            results += f"Title: {Book.getTitle(book)}\n"
            results += f"Author: {Book.getAuthors(book)}\n"
            results += f"Publisher: {Book.getPublisher(book)}\n\n"

        if not results:
            return "No Results"
        return results


    def getRecommendations(self, type, title):
        if type == "Movie" or type == "TV Show":
            show_id = None
            for show_id, show in self.__shows.items():
                if show.getTypeShow() == type and show.getTitle().lower() == title.lower():
                    break
            else:
                messagebox.showwarning("Warning", f"No recommendations found for {title}.")
                return "No Results"

            recommendations = self.__associations.get(show_id, [])
            if not recommendations:
                return "No Results"

            results = ""
            for recommendation_id in recommendations:
                if recommendation_id in self.__books:
                    book = self.__books[recommendation_id]
                    results += f"Title: {book.getTitle()}\n"
                    results += f"Author: {book.getAuthors()}\n"
                    results += f"Publisher: {book.getPublisher()}\n\n"
        elif type == "Book":
            book_id = None
            for book_id, book in self.__books.items():
                if book.getTitle().lower() == title.lower():
                    break
            else:
                messagebox.showwarning("Warning", f"No recommendations found for {title}.")
                return "No Results"

            recommendations = self.__associations.get(book_id, [])
            if not recommendations:
                return "No Results"

            results = ""
            for recommendation_id in recommendations:
                if recommendation_id in self.__shows:
                    show = self.__shows[recommendation_id]
                    results += f"Title: {show.getTitle()}\n"
                    results += f"Director: {show.getDirectors()}\n"
                    results += f"Actors: {show.getActors()}\n"
                    results += f"Genre: {show.getGenres()}\n\n"
        else:
            messagebox.showerror("Error", "Invalid type. Please specify 'Movie', 'TV Show', or 'Book'.")
            return "No Results"

        return results