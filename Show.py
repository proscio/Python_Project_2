from Media import Media

class Show(Media):
    def __init__(self, id, title, averageRating, typeShow, directors, actors, countryCode, dateAired, releaseYear, rating, duration, genres, description):
        super().__init__(id, title, averageRating)
        self.typeShow = typeShow
        self.directors = directors
        self.actors = actors
        self.countryCode = countryCode
        self.dateAired = dateAired
        self.releaseYear = releaseYear
        self.rating = rating
        self.duration = duration
        self.genres = genres
        self.description = description

    def getTypeShow(self):
        return self.typeShow

    def getDirectors(self):
        return self.directors

    def getActors(self):
        return self.actors

    def getCountryCode(self):
        return self.countryCode

    def getDateAired(self):
        return self.dateAired

    def getReleaseYear(self):
        return self.releaseYear

    def getRating(self):
        return self.rating

    def getDuration(self):
        return self.duration

    def getGenres(self):
        return self.genres

    def getDescription(self):
        return self.description

    def setTypeShow(self, typeShow):
        self.typeShow = typeShow

    def setDirectors(self, directors):
        self.directors = directors

    def setActors(self, actors):
        self.actors = actors

    def setCountryCode(self, countryCode):
        self.countryCode = countryCode

    def setDateAired(self, dateAired):
        self.dateAired = dateAired

    def setReleaseYear(self, releaseYear):
        self.releaseYear = releaseYear

    def setRating(self, rating):
        self.rating = rating

    def setDuration(self, duration):
        self.duration = duration

    def setGenres(self, genres):
        self.genres = genres

    def setDescription(self, description):
        self.description = description