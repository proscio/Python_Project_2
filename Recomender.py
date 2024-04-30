import os
import tkinter.filedialog as filedialog
from Book import Book
from Show import Show
class Recomender:
    def __init__(self):
        self.__books = {}
        self.__shows = {}
        self.__assosiations = {}
        
    def loadBooks(self):
        file = filedialog.askopenfilename(title = "Book File", initialdir = os.getcwd())
        with open(file, "r") as bookFile:
            for line in bookFile:
                value = line.strip().split(",")
                newBook = Book(ID= value[0], Title = value[1], authors=value[2], Rating=value[3], isbn=value[4], isbn13=value[5], languageCode=value[6], pageCount= value[7], numRatings=value[8], publicationDate= value[9], publisher=value[10] )
                self.__books[value[0]]= newBook 
    def loadShows(self):
        file = filedialog.askopenfilename(title = "Show File", initialdir=os.getcwd())
        with open(file,"r") as showFile:
            for line in showFile:
                value = line.strip().split(",")
                newShow = Show(ID=value[0], typeShow=value[1], Title=value[2], directors=value[3], actors=value[4], avgRating=value[5], countryCode=value[6], dateAired=value[7], releaseYear=value[8], Rating=value[9], duration=value[10], listedIn = value[11], description=value[12])
                self.__shows[value[0]]= newShow
    def loadAssosiations():
        file = filedialog.askopenfile(title = "Assosiation File", inidialir = os.getcwd())
        with open(file, "r") as assosiationFile:
            for line in assosiationFile:
                line.strip().split(",")