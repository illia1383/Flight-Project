from Airport import *

class Flight:
    def __init__(self, flightNo, origin, destination):
        self._flightNo = flightNo
        if isinstance(origin, Airport):
            self._origin = origin
        else:
            raise TypeError("The origin and destination must be Airport objects")
        if isinstance(destination, Airport):
            self._destination = destination
        else:
            raise TypeError("The origin and destination must be Airport objects")


    def __repr__(self):
        if self.isDomesticFlight() == True:
            return "Flight: " + str(self._flightNo) + " from " + self._origin.getCity().title() + " to " + self._destination.getCity().title() + " {domestic}"
        else:
            return "Flight: " + str(self._flightNo) + " from " + self._origin.getCity().title() + " to " + self._destination.getCity().title() + " {international}"

    #Checking if every part of the origin and destination flights are the exact same
    def __eq__(self, other):
        if isinstance(other, Flight): #checking to see if its an instance of flight
            #Checking if the origin is the same
            if self._origin.getCode() == other._origin.getCode() and self._origin.getCity() == other._origin.getCity() and self._origin.getCountry() == other._origin.getCountry():
                #checks to see if the destination is the same
                return self._destination.getCode() == other._destination.getCode() and self._destination.getCity() == other._destination.getCity() and self._destination.getCountry() == other._destination.getCountry()
            else:
                return False
        else:
            return False

    #checks to see if the country of the origin and destination are the same
    def isDomesticFlight(self):
        return self._origin.getCountry() == self._destination.getCountry()

    #Getters
    def getFlightNumber(self):
        return self._flightNo
    def getOrigin(self):
        return self._origin #Uses the repr function we made for the Airport function
    def getDestination(self):
        return self._destination #Uses the repr function we made for the Airport function

    #Setters
    def setOrigin(self, origin):
        self._origin = origin
    def setDestination(self, destination):
        self._destination = destination
