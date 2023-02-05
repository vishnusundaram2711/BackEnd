from pymongo import MongoClient

"""
? Class for MongoConnectivity
"""

class MongoConnect:
    def __init__(self) -> None:
        """
        ! Mongo PassCode is essential and it about to be changed as Repo Secret
        * MongoServer is used to pass and connect the mongoDb with the app
        * MongoServer Instance is created in the mongoServerInstance
        """
        self.mongoPasscode = "2rzj81gI4P4YOROk"
        self.mongoConnectLink = f"mongodb+srv://testdb:{self.mongoPasscode}@cluster0.nkxg5rn.mongodb.net/?retryWrites=true&w=majority"
      

    """
    ? Fire function connects the Heroku with MongoDb
    """ 
    def fire(self):
        self.mongoServer = MongoClient(self.mongoConnectLink)
        # Test Server Initialised
        self.mongoServerInstance = self.mongoServer.testing
        self.rationData = self.mongoServerInstance.get_collections("rationData")
        self.verificationCode = self.mongoServerInstance.get_collections("verificationCode")

    
    def insertdata(self):
        pass

    def updateData(self):
        pass

    def removeData(self):
        pass

    def returnData(self):
        pass