class Ground:
    
    temperature = 0
    humidity = 0

    def getTemperature(self):
        self.temperature += 1
        return self.temperature

    def getHumidity(self):
        self.humidity += 1
        return self.humidity

    def activeSolenoid(self):
        print ("Activamos la electrovalvula")