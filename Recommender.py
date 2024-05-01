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
        file = filedialog.askopenfilename(title="Association File", inidialir=os.getcwd())
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
            if Show.get_type(i) == "Movie":
                data = "\n{Show.getTitle(i): 10} | {Show.get_duration(i): 10}"
            string = string + data
        return string

    def getTVList(self):
        string = f"Title:\t Duration:\n"
        for i in self.__shows:
            if Show.get_type(i) == "TV Show":
                data = "\n{Show.getTitle(i): 10} | {Show.get_duration(i): 10}"
            string = string + data
        return string

    def getBookList(self):
        string = f"Title:\t Authot: \n"
        for i in self.__books:
            data = "\n{Book.getTitle(i):10} | {Book.get_authors(i) : 10}"
            string = string + data
        return string

    def getMovieStats(self):
        Rating_list, Duration_List, Director_list, Actor_list, Genre_list = [], [], [], [], [], []
        for i in self.__shows:
            if Show.get_type(i) == "Movie":
                Rating_list.append(Show.getRating(i))
                Duration_List.append(Show.get_duration(i))
                Director_list.append(str(Show.get_directors(i)).strip().split("\\"))
                Actor_list.append(str(Show.get_actors(i)).strip().split("\\"))
                Genre_list.append(Show.get_genres(i))

        def most_frequent(list):
            freq_dict = {}
            for i in list:
                if i in freq_dict:
                    freq_dict[i] += 1
                else:
                    freq_dict[i] = 1
            most_frequent = max(freq_dict, key=freq_dict.get)
            return most_frequent

        return f"Most Common Rating: {most_frequent(Rating_list): .2f}\nAverage Length: {most_frequent(Duration_List): .2f}\nMost Prominent Director: {most_frequent(Director_list)}\nMost Prominent Actor: {most_frequent(Actor_list)}\nLargest Genre: {most_frequent(Genre_list)}"

    def getTVStats(self):
        Rating_list, Duration_List, Actor_list, Genre_list = [], [], [], [], [], []
        for i in self.__shows:
            if Show.get_type(i) == "TV Show":
                Rating_list.append(Show.getRating(i))
                Duration_List.append(Show.get_duration(i))
                Genre_list.append(Show.get_genres(i))
                Actor_list.append(str(Show.get_actors(i)).strip().split("\\"))

        def most_frequent(list):
            freq_dict = {}
            for i in list:
                if i in freq_dict:
                    freq_dict[i] += 1
                else:
                    freq_dict[i] = 1
            most_frequent = max(freq_dict, key=freq_dict.get)
            return most_frequent

        return f"Most Common Rating: {most_frequent(Rating_list): .2f}\nAverage Length: {most_frequent(Duration_List): .2f}\nMost Prominent Director: {most_frequent(Director_list)}\nMost Prominent Actor: {most_frequent(Actor_list)}\nLargest Genre: {most_frequent(Genre_list)}"
