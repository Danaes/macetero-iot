import asyncio

import provider as p
import temperature as t
import humidity as h

async def manageTemperature(tmp):
    while True:
        tExt = tmp.getTemperatureExt()
        tInt = tmp.getTemperatureInt()

        print(f'TemExt: {tExt}, TempInt: {tInt}')

        if(tExt > 5 and tInt > 7):
            tmp.sendAlertByHightTemperature()
        
        await asyncio.sleep(2)

async def manageHumidity(hum):
    while True:
        hExt = hum.getHumidityExt()
        hInt = hum.getHumidityInt()

        print(f'HumExt: {hExt}, HumInt: {hInt}')

        if(hExt > 5 and hInt > 7):
            hum.sendAlertByHightHumidity()
        
        await asyncio.sleep(0.5)

async def scheduler():
    tmp = t.Temperature()
    hum = h.Humidity()

    await asyncio.gather(
        manageTemperature(tmp),
        manageHumidity(hum),
    )



if __name__ == "__main__":
    asyncio.run(scheduler())