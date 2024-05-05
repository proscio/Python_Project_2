from Media import Media

class Show(Media):
    """
    The Show class inherits from the Media class and represents a TV show from the media csv file.
    """
    def __init__(self, id, title, averageRating, typeShow, directors, actors, countryCode, dateAired, releaseYear, rating, duration, genres, description):
        """
        Initialize a Show object.
        
        :param id: The unique identifier for the show.
        :type id: str
        :param title: The title of the show.
        :type title: str
        :param averageRating: The average rating of the show.
        :type averageRating: float
        :param typeShow: The type of the show (e.g., Movie, TV Show).
        :type typeShow: str
        :param directors: The directors of the show.
        :type directors: str
        :param actors: The actors in the show.
        :type actors: str
        :param countryCode: The country code of the show.
        :type countryCode: str
        :param dateAired: The date the show aired.
        :type dateAired: str
        :param releaseYear: The release year of the show.
        :type releaseYear: int
        :param rating: The rating of the show.
        :type rating: str
        :param duration: The duration of the show.
        :type duration: str
        :param genres: The genres of the show.
        :type genres: str
        :param description: The description of the show.
        :type description: str
        """
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
        """
        Get the type of the show.
        
        :return: The type of the show.
        :rtype: str
        """
        return self.typeShow

    def getDirectors(self):
        """
        Get the directors of the show.
        
        :return: The directors of the show.
        :rtype: str
        """
        return self.directors

    def getActors(self):
        """
        Get the actors in the show.
        
        :return: The actors in the show.
        :rtype: str
        """
        return self.actors

    def getCountryCode(self):
        """
        Get the country code of the show.
        
        :return: The country code of the show.
        :rtype: str
        """
        return self.countryCode

    def getDateAired(self):
        """
        Get the date the show aired.
        
        :return: The date the show aired.
        :rtype: str
        """
        return self.dateAired

    def getReleaseYear(self):
        """
        Get the release year of the show.
        
        :return: The release year of the show.
        :rtype: int
        """
        return self.releaseYear

    def getRating(self):
        """
        Get the rating of the show.
        
        :return: The rating of the show.
        :rtype: str
        """
        return self.rating

    def getDuration(self):
        """
        Get the duration of the show.
        
        :return: The duration of the show.
        :rtype: str
        """
        return self.duration

    def getGenres(self):
        """
        Get the genres of the show.
        
        :return: The genres of the show.
        :rtype: str
        """
        return self.genres

    def getDescription(self):
        """
        Get the description of the show.
        
        :return: The description of the show.
        :rtype: str
        """
        return self.description

    def setTypeShow(self, typeShow):
        """
        Set the type of the show.
        
        :param typeShow: The new type for the show.
        :type typeShow: str
        :return: None
        """
        self.typeShow = typeShow

    def setDirectors(self, directors):
        """
        Set the directors of the show.
        
        :param directors: The new directors for the show.
        :type directors: str
        :return: None
        """
        self.directors = directors

    def setActors(self, actors):
        """
        Set the actors in the show.
        
        :param actors: The new actors for the show.
        :type actors: str
        :return: None
        """
        self.actors = actors

    def setCountryCode(self, countryCode):
        """
        Set the country code of the show.
        
        :param countryCode: The new country code for the show.
        :type countryCode: str
        :return: None
        """
        self.countryCode = countryCode

    def setDateAired(self, dateAired):
        """
        Set the date the show aired.
        
        :param dateAired: The new date the show aired.
        :type dateAired: str
        :return: None
        """
        self.dateAired = dateAired

    def setReleaseYear(self, releaseYear):
        """
        Set the release year of the show.
        
        :param releaseYear: The new release year for the show.
        :type releaseYear: int
        :return: None
        """
        self.releaseYear = releaseYear

    def setRating(self, rating):
        """
        Set the rating of the show.
        
        :param rating: The new rating for the show.
        :type rating: str
        :return: None
        """
        self.rating = rating

    def setDuration(self, duration):
        """
        Set the duration of the show.
        
        :param duration: The new duration for the show.
        :type duration: str
        :return: None
        """
        self.duration = duration

    def setGenres(self, genres):
        """
        Set the genres of the show.
        
        :param genres: The new genres for the show.
        :type genres: str
        :return: None
        """
        self.genres = genres

    def setDescription(self, description):
        """
        Set the description of the show.
        
        :param description: The new description for the show.
        :type description: str
        :return: None
        """
        self.description = description
        
