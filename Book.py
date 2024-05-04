from Media import Media

class Book(Media):
    def __init__(self, id, title, averageRating, authors, isbn, isbn13, languageCode, pageCount, numRatings, publicationDate, publisher):
        super().__init__(id, title, averageRating)
        self.__authors = authors
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__languageCode = languageCode
        self.__pageCount = pageCount
        self.__numRatings = numRatings
        self.__publicationDate = publicationDate
        self.__publisher = publisher

    def getAuthors(self):
        return self.__authors

    def getIsbn(self):
        return self.__isbn

    def getIsbn13(self):
        return self.__isbn13

    def getLanguageCode(self):
        return self.__languageCode

    def getPageCount(self):
        return self.__pageCount

    def getNumRatings(self):
        return self.__numRatings

    def getPublicationDate(self):
        return self.__publicationDate

    def getPublisher(self):
        return self.__publisher
