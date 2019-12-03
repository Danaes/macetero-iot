import spidev
import mraa

relayPin = 22
resistor = 2200

class Ground:
    
    temperature = 0
    weight = 0
    relay = 0
    spi = 0

    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(1,0)

        self.relay = mraa.Gpio(relayPin)
        self.relay.dir(mraa.DIR_OUT)

    def getWeight(self):
        const = 35.0
        adcValue = self.getDataFromSpi(0)
        self.weight = (int(adcValue) - 102) / const
        return self.weight
    
    def water(self, openValve):
	    if openValve:
		    self.relay.write(1)
	    else:
		    self.relay.write(0)
    
    def getTemperature(self): 
        adcValue = self.getDataFromSpi(1)
        self.temperature = (resistor*((1023/adcValue) - 1) - 1000)/3.875

        return self.temperature

    
    def getDataFromSpi(self, channel):
        r = self.spi.xfer([1,(8+channel)<<4,0])
        adcOut = ((r[1]&3) << 8) + r[2]
        return adcOut