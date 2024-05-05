from Media import Media

class Book(Media):
     """
    The Book class inherits from the Media class and represents a book in the media library.
    """
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
         """
        Get the authors of the book.
        
        :return: The authors of the book.
        :rtype: str
        """
        return self.__authors

    def getIsbn(self):
        """
        Get the ISBN of the book.
        
        :return: The ISBN of the book.
        :rtype: str
        """
        return self.__isbn

    def getIsbn13(self):
        """
        Get the ISBN-13 of the book.
        
        :return: The ISBN-13 of the book.
        :rtype: str
        """
        return self.__isbn13

    def getLanguageCode(self):
        """
        Get the language code of the book.
        
        :return: The language code of the book.
        :rtype: str
        """
        return self.__languageCode

    def getPageCount(self):
        """
        Get the number of pages in the book.
        
        :return: The number of pages in the book.
        :rtype: int
        """
        return self.__pageCount

    def getNumRatings(self):
        """
        Get the number of ratings the book has received.
        
        :return: The number of ratings the book has received.
        :rtype: int
        """
        return self.__numRatings

    def getPublicationDate(self):
        """
        Get the publication date of the book.
        
        :return: The publication date of the book.
        :rtype: str
        """

        return self.__publicationDate

    def getPublisher(self):
        """
        Get the publisher of the book.
        
        :return: The publisher of the book.
        :rtype: str
        """
        return self.__publisher
