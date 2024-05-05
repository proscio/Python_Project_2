class Media:
     """
    The Media class represents a general media item with an ID, title, and average rating.
    """
    def __init__(self, id, title, averageRating):
        """
        Initialize a Media object.
        
        :param id: The unique identifier for the media item.
        :type id: str
        :param title: The title of the media item.
        :type title: str
        :param averageRating: The average rating of the media item.
        :type averageRating: float
        """
        self.__id = id
        self.__title = title
        self.__averageRating = averageRating

    def getId(self):
        """
        Get the ID of the media item.
        
        :return: The ID of the media item.
        :rtype: str
        """
        return self.__id

    def getTitle(self):
        """
        Get the title of the media item.
        
        :return: The title of the media item.
        :rtype: str
        """
        return self.__title

    def getAverageRating(self):
        """
        Get the average rating of the media item.
        
        :return: The average rating of the media item.
        :rtype: float
        """
        return self.__averageRating

    def setID(self, ID):
        """
        Set the ID of the media item.
        
        :param ID: The new ID for the media item.
        :type ID: str
        :return: None
        """
        self.__id = ID

    def setTitle(self, Title):
        """
        Set the title of the media item.
        
        :param Title: The new title for the media item.
        :type Title: str
        :return: None
        """
        self.__title = Title

    def setAverageRating(self, averageRating):
         """
        Set the average rating of the media item.
        
        :param averageRating: The new average rating for the media item.
        :type averageRating: float
        :return: None
        """
        self.__averageRating = averageRating
