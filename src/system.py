import asyncio
import provider as p
import enviroment as e
import ground as g

sensor_data = {
    'humidityExt': 0,
    'humidityInt': 0,
    'temperatureExt': 0,
    'temperatureInt': 0,
    'light': 0,
    'weight': 0
}


async def manageData(env, gnd):
    while True:
        env.loadDataFromInternalSensors()
        sensor_data['light'] = env.getBrightness()

        if (sensor_data['light'] < 200):
            env.turnOnLamp(1, 1, 1)
        else:
            env.turnOffLamp()

        gnd.checkWatering()

        await asyncio.sleep(1)


async def manageWatering(gnd):
    while True:
        sensor_data['humidityInt'] = gnd.getHumidity()

        if(sensor_data['humidityInt'] < 20):
            gnd.openWatering()

        await asyncio.sleep(5)


async def manageTB(pvd, env, gnd):
    while True:
        sensor_data['temperatureExt'] = env.getTemperature()
        sensor_data['temperatureInt'] = gnd.getTemperature()
        sensor_data['weight'] = gnd.getWeight()
        sensor_data['light'] = env.getBrightness()
        sensor_data['humidityExt'] = env.getHumidity()
        sensor_data['humidityInt'] = gnd.getHumidity()

        pvd.sendData(sensor_data)
        #print(f'Envío datos a TB: {sensor_data}')
        await asyncio.sleep(2)


async def scheduler():
    env = e.Enviroment()
    gnd = g.Ground()
    pvd = p.CloudProvider()

    await asyncio.gather(
        manageData(env, gnd),
        manageWatering(gnd),
        manageTB(pvd, env, gnd),
    )

if __name__ == "__main__":
    asyncio.run(scheduler())
