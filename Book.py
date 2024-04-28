from media import Media
class Book(Media):
    def __init__(self, authors, isbn, isbn13, languageCode, pageCount, numRatings, publicationDate, publisher):
        super().__init__()     
        self.__authors = authors
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__languageCode = languageCode
        self.__pageCount = pageCount
        self.__numRatings = numRatings
        self.__publicationDate = publicationDate
        self.__publisher = publisher

    def get_authors(self):
        return self.__authors
    
    def get_isbn(self):
        return self.__isbn
    
    def get_isbn13(self):
        return self.__isbn13
    
    def get_language_code(self):
        return self.__languageCode
    
    def get_page_count(self):
        return self.__pageCount
    
    def get_num_ratings(self):
        return self.__numRatings
    
    def get_publication_date(self):
        return self.__publicationDate
    
    def get_publisher(self):
        return self.__publisher
    