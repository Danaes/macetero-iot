class Humidity:
    
    HumidityExt = 0
    HumidityInt = 0

    def getHumidityExt(self):
        self.HumidityExt += 1
        return self.HumidityExt

    def getHumidityInt(self):
        self.HumidityInt += 1
        return self.HumidityInt

    def sendAlertByHightHumidity(self):
        self.HumidityExt -= 5
        self.HumidityInt -= 5
        print ("ALERTA! La humedad es elevada")