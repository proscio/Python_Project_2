import os
import tkinter.filedialog as filedialog
from Book import Book
from Show import Show

class Recommender:
    def __init__(self):
        self.__books = {}
        self.__shows = {}
        self.__associations = {}

    def loadBooks(self):
        file = filedialog.askopenfilename(title="Book File", initialdir=os.getcwd())
        with open(file, "r") as bookFile:
            for line in bookFile:
                value = line.strip().split(",")
                newBook = Book(ID=value[0], Title=value[1], authors=value[2], Rating=value[3], isbn=value[4],
                               isbn13=value[5], languageCode=value[6], pageCount=value[7], numRatings=value[8],
                               publicationDate=value[9], publisher=value[10])
                self.__books[value[0]] = newBook

    def loadShows(self):
        file = filedialog.askopenfilename(title="Show File", initialdir=os.getcwd())
        with open(file, "r") as showFile:
            for line in showFile:
                value = line.strip().split(",")
                newShow = Show(ID=value[0], typeShow=value[1], Title=value[2], directors=value[3], actors=value[4],
                               avgRating=value[5], countryCode=value[6], dateAired=value[7], releaseYear=value[8],
                               Rating=value[9], duration=value[10], listedIn=value[11], description=value[12])
                self.__shows[value[0]] = newShow

    def loadAssociations(self):
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
        string = f"Title:\t Duration:\n"
        for i in self.__shows:
            if Show.getTypeShow(i) == "Movie":
                data = f"\n{Show.getTitle(i): 10} | {Show.getDuration(i): 10}"
            string = string + data
        return string

    def getTVList(self):
        string = f"Title:\t Duration:\n"
        for i in self.__shows:
            if Show.getTypeShow(i) == "TV Show":
                data = f"\n{Show.getTitle(i): 10} | {Show.getDuration(i): 10}"
            string = string + data
        return string

    def getBookList(self):
        string = f"Title:\t Author: \n"
        for i in self.__books:
            data = f"\n{Book.getTitle(i):10} | {Book.get_authors(i) : 10}"
            string = string + data
        return string

    def getMovieStats(self):
        Rating_list, Duration_List, Director_list, Actor_list, Genre_list = [], [], [], [], [], []
        for i in self.__shows:
            if Show.getTypeShow(i) == "Movie":
                Rating_list.append(Show.getRating(i))
                Duration_List.append(Show.getDuration(i))
                Director_list.append(str(Show.getDirectors(i)).strip().split("\\"))
                Actor_list.append(str(Show.getActors(i)).strip().split("\\"))
                Genre_list.append(Show.getGenres(i))

        def most_frequent(list):
            freq_dict = {}
            for i in list:
                if i in freq_dict:
                    freq_dict[i] += 1
                else:
                    freq_dict[i] = 1
            most_frequent = max(freq_dict, key=freq_dict.get)
            return most_frequent

        def frequencies(list):
            ratings = {"7+": 0, "TV-14": 0, "13+": 0, "TV-Y": 0, "ALL": 0, "TV-NR": 0, "18+": 0, "TV-Y7": 0, "16+": 0, "TV-G": 0, "TV-PG": 0}
            ratingString = "Ratings:\n"
            for i in list:
                ratings[i] += 1

            for i in ratings:
                ratingString += (i + " " + ((i / len(ratings)) + "%\n"))
            return ratingString

        def mean(list):
            total_sum = 0
            for i in list:
                total_sum += i
            average = total_sum / len(list)
            return average

        return f"{frequencies(Rating_list)}Length: {mean(Duration_List): .2f}\nMost Prominent Director: {most_frequent(Director_list)}\nMost Prolific Actor: {most_frequent(Actor_list)}\nMost Frequenct Genre: {most_frequent(Genre_list)}"

    def getTVStats(self):
        Rating_list, Duration_List, Actor_list, Genre_list = [], [], [], [], [], []
        for i in self.__shows:
            if Show.getTypeShow(i) == "TV Show":
                Rating_list.append(Show.getRating(i))
                Duration_List.append(Show.getDuration(i))
                Genre_list.append(Show.getGenres(i))
                Actor_list.append(str(Show.getActors(i)).strip().split("\\"))

        def most_frequent(list):
            freq_dict = {}
            for i in list:
                if i in freq_dict:
                    freq_dict[i] += 1
                else:
                    freq_dict[i] = 1
            most_frequent = max(freq_dict, key=freq_dict.get)
            return most_frequent

        def frequencies(list):
            ratings = {"7+": 0, "TV-14": 0, "13+": 0, "TV-Y": 0, "ALL": 0, "TV-NR": 0, "18+": 0, "TV-Y7": 0, "16+": 0, "TV-G": 0, "TV-PG": 0}
            ratingString = "Ratings:\n"
            for i in list:
                ratings[i] += 1

            for i in ratings:
                ratingString += (i + " " + ((i / len(ratings)) + "%\n"))
            return ratingString

        def mean(list):
            total_sum = 0
            for i in list:
                total_sum += i
            average = total_sum / len(list)
            return average

        return f"{frequencies(Rating_list)}\nAverage Length: {mean(Duration_List): .2f}\nMost Prominent Actor: {most_frequent(Actor_list)}\nLargest Genre: {most_frequent(Genre_list)}"

    def getBookStats(self):
        PageCount_list, Author_list, Publisher_list = [], [], []
        for i in self.__books:
            PageCount_list.append(Book.getPageCount(i))
            Author_list.append(Book.getAuthors(i))
            Publisher_list.append(Book.getPublisher(i))

        def most_frequent(list):
            freq_dict = {}
            for i in list:
                if i in freq_dict:
                    freq_dict[i] += 1
                else:
                    freq_dict[i] = 1
            most_frequent = max(freq_dict, key=freq_dict.get)
            return most_frequent

        def mean(list):
            total_sum = 0
            for i in list:
                total_sum += i
            average = total_sum / len(list)
            return average

        return f"Average Page Count: {mean(PageCount_list): .2f}\nMost Prolific Author: {most_frequent(Author_list)}\nMost Prolific Publisher: {most_frequent(Publisher_list)}"
def searchTVMovies(typeShow, title, director, actors, genre):
    if typeShow != "Movie" or "TV Show":
        print("start here")