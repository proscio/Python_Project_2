from media import Media

class Show(Media):
    def __init__(self, typeShow, directors, actors, countryCode, dateAired, releaseYear, rating, duration, genres, description ):
        super().__init__()
        self.__type = typeShow
        self.__directors = directors
        self.__actors = actors
        self.__countryCode = countryCode
        self.__dateAired = dateAired
        self.__releaseYear = releaseYear
        self.__rating = rating
        self.__duration = duration
        self.__genre = genres
        self.__description = description

    def get_type(self):
        return self.__type
    
    def get_directors(self):
        return self.__directors
    
    def get_actors(self):
        return self.__actors
    
    def get_country_code(self):
        return self.__countryCode
    
    def get_date_aired(self):
        return self.__dateAired
    
    def get_release_year(self):
        return self.__releaseYear
    
    def get_rating(self):
        return self.__rating
    
    def get_duration(self):
        return self.__duration
    
    def get_genres(self):
        return self.__genre
    
    def get_description(self):
        return self.__description