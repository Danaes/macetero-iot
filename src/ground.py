import spidev
import mraa
import time

relayPin = 22
resistor = 2200


class Ground:

    temperature = 0
    weight = 0
    relay = 0
    spi = 0

    def __init__(self):
        self.spi = spidev.SpiDev()

        self.relay = mraa.Gpio(relayPin)
        self.relay.dir(mraa.DIR_OUT)

    def getWeight(self):
        const = 35.0
        adcValue = self.getDataFromSpi0(0)
        self.weight = (int(adcValue) - 102) / const
        return self.weight

    def openWatering(self):
        self.relay.write(1)

    def getHumidity(self):
        resistorWater1 = self.getDataFromSpi0(2)
        resistorWater2 = self.getDataFromSpi0(3)
        rw1 = 100 - ((resistorWater1-468)/(1023-468))*100
        rw2 = 100 - ((resistorWater2-468)/(1023-468))*100
        return (rw1 + rw2) / 2

    def checkWatering(self):
        adcValue = self.getDataFromSpi1(0)
        thresh = 200
        if adcValue < thresh:
            self.relay.write(0)

    def getTemperature(self):
        adcValue = self.getDataFromSpi0(1)
        self.temperature = (resistor*((1023/adcValue) - 1) - 1000)/3.875

        return self.temperature

    def getDataFromSpi0(self, channel):
        self.spi.open(1, 0)
        time.sleep(0.001)
        r = self.spi.xfer([1, (8+channel) << 4, 0])
        adcOut = ((r[1] & 3) << 8) + r[2]
        self.spi.close()
        return adcOut

    def getDataFromSpi1(self, channel):
        self.spi.open(1, 1)
        time.sleep(0.001)
        r = self.spi.xfer([1, (8+channel) << 4, 0])
        adcOut = ((r[1] & 3) << 8) + r[2]
        self.spi.close()
        return adcOut
