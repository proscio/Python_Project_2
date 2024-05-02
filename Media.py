class Media:
    def __init__(self, id, title, averageRating):
        self.__id = id
        self.__title = title
        self.__averageRating = averageRating

    def getId(self):
        return self.__id

    def getTitle(self):
        return self.__title

    def getAverageRating(self):
        return self.__averageRating

    def setID(self, ID):
        self.__id = ID

    def setTitle(self, Title):
        self.__title = Title

    def setAverageRating(self, averageRating):
        self.__averageRating = averageRating