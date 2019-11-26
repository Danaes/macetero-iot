import smbus2 as smbus
from smbus2 import i2c_msg
import time

bus = smbus.SMBus(4)

addressTYH = 0x44
addressLight = 0x10
sensitivity = 1
integration_time = 100


class Enviroment:
    
    temperature = 0
    humidity    = 0
    brightness  = 0

    def __init__(self):
        bus.write_word_data(addressLight,0x00,0x0000)

    def loadData(self):
        bus.write_byte_data(addressTYH,0x24,0x16) #00 0b 16
        time.sleep(0.1)
        sensor = i2c_msg.read(addressTYH,6)
        bus.i2c_rdwr(sensor)
        rawdata = bytes(sensor)
        temp = int( rawdata[0] *256 ) + int( rawdata[1] )
        self.temperature = -45 + ( 175 * temp ) / ( 2**16 - 1 )
        hum = int( rawdata[3] * 256 ) + int( rawdata[4] )
        self.humidity = ( 100 * hum ) / ( 2**16 - 1 )

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getBrightness(self):
    	#READ AMBIENT LIGHT DATA FROM THE REGISTER 0x04 OF THE SENSOR
        self.brightness = bus.read_word_data(addressLight,0x04)
	#FORMULA THAT OBTAINS THE LIGHT LEVEL MEASURED IN lux 
        self.brightness = (self.brightness/sensitivity) * (10/integration_time)

        return self.brightness

    def activeLamp(self):
        print ("Activamos la lampara")
