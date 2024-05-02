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
        return self.authors

    def getIsbn(self):
        return self.isbn

    def getIsbn13(self):
        return self.isbn13

    def getLanguageCode(self):
        return self.languageCode

    def getPageCount(self):
        return self.pageCount

    def getNumRatings(self):
        return self.numRatings

    def getPublicationDate(self):
        return self.publicationDate

    def getPublisher(self):
        return self.publisher

    def setAuthors(self, authors):
        self.authors = authors

    def setIsbn(self, isbn):
        self.isbn = isbn

    def setIsbn13(self, isbn13):
        self.isbn13 = isbn13

    def setLanguageCode(self, languageCode):
        self.languageCode = languageCode

    def setPageCount(self, pageCount):
        self.pageCount = pageCount

    def setNumRatings(self, numRatings):
        self.numRatings = numRatings

    def setPublicationDate(self, publicationDate):
        self.publicationDate = publicationDate

    def setPublisher(self, publisher):
        self.publisher = publisher