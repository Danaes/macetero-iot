class Temperature:
    
    temperatureExt = 0
    temperatureInt = 0

    def getTemperatureExt(self):
        self.temperatureExt += 1
        return self.temperatureExt

    def getTemperatureInt(self):
        self.temperatureInt += 1
        return self.temperatureInt

    def sendAlertByHightTemperature(self):
        self.temperatureExt -= 5
        self.temperatureInt -= 5
        print ("ALERTA! La temperatura es elevada")