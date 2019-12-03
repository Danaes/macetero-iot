import sys
import mraa
import smbus2 as smbus
from smbus2 import i2c_msg
import time

bus4 = smbus.SMBus(4)
bus5 = smbus.SMBus(5)

addressTYH = 0x44
addressLight = 0x10
sensitivity = 1
integration_time = 100

ledRPin = 18
ledGPin = 15
ledBPin = 13


class Enviroment:

    temperature = 0
    humidity = 0
    brightness = 0
    ledR = 0
    ledG = 0
    ledB = 0

    def __init__(self):
        bus4.write_word_data(addressLight, 0x00, 0x0000)

        # Export the GPIO pin for use
        self.ledR = mraa.Gpio(ledRPin)
        self.ledG = mraa.Gpio(ledGPin)
        self.ledB = mraa.Gpio(ledBPin)

        self.ledR.dir(mraa.DIR_OUT)
        self.ledG.dir(mraa.DIR_OUT)
        self.ledB.dir(mraa.DIR_OUT)

    def loadDataFromInternalSensors(self):
        bus5.write_byte_data(addressTYH, 0x24, 0x16)  # 00 0b 16
        time.sleep(0.1)
        sensor = i2c_msg.read(addressTYH, 6)
        bus5.i2c_rdwr(sensor)
        rawdata = bytes(sensor)
        temp = int(rawdata[0] * 256) + int(rawdata[1])
        self.temperature = self.truncate(-45 + (175 * temp) / (2**16 - 1))
        hum = int(rawdata[3] * 256) + int(rawdata[4])
        self.humidity = self.truncate((100 * hum) / (2**16 - 1))

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getBrightness(self):
        # READ AMBIENT LIGHT DATA FROM THE REGISTER 0x04 OF THE SENSOR
        self.brightness = bus4.read_word_data(addressLight, 0x04)
        #   FORMULA THAT OBTAINS THE LIGHT LEVEL MEASURED IN lux
        self.brightness = self.truncate(
            (self.brightness/sensitivity) * (10/integration_time))

        return self.brightness

    def turnOnLamp(self, r, g, b):
        self.ledR.write(r)
        self.ledB.write(b)
        self.ledG.write(g)
        print("Activamos la lampara")

    def turnOffLamp(self):
        self.ledR.write(0)
        self.ledB.write(0)
        self.ledG.write(0)
        print("Apagamos la lampara")

    def truncate(self, n):
        return int(n * 100) / 100
