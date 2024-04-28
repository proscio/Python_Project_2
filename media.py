class Media:
    def __init__(self):
        self.__id = 0
        self.__title = ""
        self.__rating = 0
    
    def getId(self):
        return self.__id
    
    def getTitle(self):
        return self.__title
    
    def getRating(self):
        return self.__rating

    def setID(self,ID):
        self.__id = ID
    def setTitle(self,Title):
        self.__title = Title
    def setRating(self,Rating):
        self.__rating = Rating