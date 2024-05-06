from Media import Media

class Show(Media):
    def __init__(self, id, title, averageRating, typeShow, directors, actors, countryCode, dateAired, releaseYear, rating, duration, genres, description):
        super().__init__(id, title, averageRating)
        self.__typeShow = typeShow
        self.__directors = directors
        self.__actors = actors
        self.__countryCode = countryCode
        self.__dateAired = dateAired
        self.__releaseYear = releaseYear
        self.__rating = rating
        self.__duration = duration
        self.__genres = genres
        self.__description = description

    def getTypeShow(self):
        return self.__typeShow

    def getDirectors(self):
        return self.__directors

    def getActors(self):
        return self.__actors

    def getCountryCode(self):
        return self.__countryCode

    def getDateAired(self):
        return self.__dateAired

    def getReleaseYear(self):
        return self.__releaseYear

    def getRating(self):
        return self.__rating

    def getDuration(self):
        return self.__duration

    def getGenres(self):
        return self.__genres

    def getDescription(self):
        return self.__description   