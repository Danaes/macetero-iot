class Enviroment:
    
    temperature = 0
    humidity    = 0
    brightness  = 0

    def getTemperature(self):
        self.temperature += 1
        return self.temperature

    def getHumidity(self):
        self.humidity += 1
        return self.humidity

    def getBrightness(self):
        self.brightness += 1
        return self.brightness

    def activeLamp(self):
        print ("Activamos la lampara")