import asyncio
import provider as p
import enviroment as e
import ground as g

sensor_data = {
    'humidityExt'   : 0,
    'humidityInt'   : 0,
    'temperatureExt': 0,
    'temperatureInt': 0,
    'light'         : 0
}

async def manageTemperature(env, gnd):
    while True:
        sensor_data['temperatureExt'] = env.getTemperature()
        sensor_data['temperatureInt']  = gnd.getTemperature()
        sensor_data['light'] = env.getBrightness()

        await asyncio.sleep(1)

async def manageHumidity(env, gnd):
    while True:
        sensor_data['humidityExt'] = env.getHumidity()
        sensor_data['humidityInt'] = gnd.getHumidity()
        
        await asyncio.sleep(1.5)

async def manageTB(pvd, env):
    while True:
        pvd.sendData(sensor_data)
        #print(f'Envío datos a TB: {sensor_data}')
        env.loadData()
        await asyncio.sleep(2)

async def scheduler():
    env = e.Enviroment()
    gnd = g.Ground()
    pvd = p.CloudProvider()

    await asyncio.gather(
        manageTemperature(env, gnd),
        manageHumidity(env, gnd),
        manageTB(pvd, env),
    )

if __name__ == "__main__":
    asyncio.run(scheduler())