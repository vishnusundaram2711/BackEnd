from math import modf
from math import sqrt
from math import pow

"""
? Class for utilityFunctions
"""
class generalFunctions:
    def __init__(self) -> None:
        """
        * All the ration co-ordinates are stored in the initialisation stage in a sorted manner
        """
        self.rationCoordinates = []
        self.rationCoordinatesLength = 10
    """
    * A script to find the nearest ration shops using binary Search
    * Latitude and Longitude are always in a sorted order
    ! Parameter override [Requires Effort]
    """
    def nearestShop(self,currentLocation: list[float]):
        """
        * Binary Search Implemented
        TODO Binary Search Implementation and Optmisation Pending
        ? Boiler Code Updated
        """
        targetLat, targetLong = currentLocation[0], currentLocation[1]
        targetLat, targetLong = modf(targetLat)[0] , modf(targetLong)[1]
        lowPtr, highPtr = 0, self.rationCoordinatesLength-1
        while lowPtr <= highPtr :
            pivotPtr = lowPtr + (highPtr - lowPtr) // 2
            pivotElement = self.rationCoordinates[pivotPtr]
            targetLat, targetLong = modf(pivotElement)[0], modf(pivotElement)[1]
            """
            TODO :  Binary Search Fixed
            """

    """
        * Calculating distance between given Cordinate
        TODO : Triangle Law Calculation for finding distance
    """
    def calculateDistance(self,currentLocation : list[float], shopLocation: list[float]):
        """
            TODO : Requires Testing
            * Algorithm updated using the following
            ? Use ((x2 - x1)**2 + (y2 - y1)**2)* 1/2
        """
        curLat, curLong = currentLocation[0], currentLocation[1]
        tarLat, tarLong = shopLocation[0], shopLocation[1]
        distance = pow((tarLat - curLat),2) + pow((tarLong - curLong),2)
        return sqrt(distance)


    def fetchData(self,key:dict):
        pass
