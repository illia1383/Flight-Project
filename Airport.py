class Airport:
    #making the Airport class with code city and country
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):
        return str(self._code) + " (" + self._city.title() + ", " + self._country.title() + ")"

    #Getters
    def getCode(self):
        return self._code
    def getCity(self):
        return self._city
    def getCountry(self):
        return self._country

    #Setters
    def setCity(self, newCity):
        self._city = newCity
    def setCountry(self, newCountry):
        self._country = newCountry


