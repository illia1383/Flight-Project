from Flight import *
from Airport import *

#making the dictionary and the tuple (containers)
allAirports = []
allFlights = {}

def loadData(airportFile, flightFile):
    #Reading the files with the airports and flights
    global allAirports
    global allFlights

    try:
        airports = open(airportFile, "r")

        for i in airports:
            tempAirport = [] #Reset the temp list
            line = i.strip()
            parts = line.split(",")
            for j in range(len(parts)):
                parts[j] = parts[j].strip()
                tempAirport.append(parts[j])
            a = Airport(tempAirport[0], tempAirport[2], tempAirport[1])
            allAirports.append(a)
        airports.close()
    except IOError:
        return False
    except:
        return False


    tempFlight = []
    try:
        flights = open(flightFile, "r")

        for i in flights:
            testFlight = []
            line = i.strip()
            parts = line.split(",")
            for n in range(len(parts)):
                parts[n] = parts[n].strip()
                testFlight.append(parts[n])

            a1 = getAirportByCode(testFlight[1])

            a2 = getAirportByCode(testFlight[2])

            f1 = Flight(testFlight[0], a1, a2)
            if a1.getCode() not in allFlights:
                allFlights[a1.getCode()] = [f1]
            else:
                allFlights[a1.getCode()].append(f1)
    except IOError:
        return False
    except:
        return False
    return True  #returns true if there are no erros

def getAirportByCode(code):
    global allAirports

    #loops throught the lists of all airports till it find the one with the same code as specified
    for i in range(len(allAirports)):
        if allAirports[i].getCode() == code: \
            return allAirports[i]

def findAllCityFlights(city):
    global allAirports
    global allFlights
    flightsCity = [] #List holding all of the flights to and from the city

    for flight in allFlights.values():
        for i in flight:
            if i.getOrigin().getCity().upper() == city.upper() or i.getDestination().getCity().upper() == city.upper():
                flightsCity.append(i)
    return flightsCity

def findAllCountryFlights(country):
    global allAirports
    global allFlights
    flightsInCountry = []
    #loops through the values of the dictionary which become a list of lists
    for flight in allFlights.values(): #Looping through the values of the dictionary which becomes a list of lists
        for i in flight:
            #If the country is the destination or the origin of the flight
            if i.getOrigin().getCountry().upper() == country.upper() or i.getDestination().getCountry().upper() == country.upper():
                flightsInCountry.append(i)
    return flightsInCountry

def findFlightBetween(origAirport, destAirport):
    global allAirports
    global allFlights
    singleHop = set()
    flightsFromOrigin = []
    for i in range(len(allFlights[origAirport.getCode()])):
        if allFlights[origAirport.getCode()][i].getDestination().getCode() == destAirport.getCode():
            return "Direct Flight: " + origAirport.getCode() + " to " + destAirport.getCode()
        else:
            flightsFromOrigin.append(allFlights[origAirport.getCode()][i])

    for i in flightsFromOrigin:
        h1 = i.getDestination() #Gets the destination of the ith flight leaving the original city
        for n in range(len(allFlights[h1.getCode()])):
            if allFlights[h1.getCode()][n].getDestination().getCode() == destAirport.getCode():
                singleHop.add(allFlights[h1.getCode()][n].getOrigin().getCode())

    if len(singleHop) == 0: #checks to see if the set is empy
        return -1
    else:
        return singleHop

def findReturnFlight(firstFlight):
    global allFlights
    global allAirports
    for i in allFlights[firstFlight.getDestination().getCode()]:
        if i.getDestination().getCode() == firstFlight.getOrigin().getCode():
            return i
    return -1
