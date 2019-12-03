import os
import time
import sys
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = '138.100.155.22'
TOKEN = 'BzsUstwSACH3YnVJdTaW'


class CloudProvider:

    def __init__(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(TOKEN)
        self.client.connect(THINGSBOARD_HOST, 1883, 60)
        self.client.loop_start()

    def sendData(self, data):
        # data deberia ir en formato JSON -> {'temperature': 0, 'humidity': 0}
        self.client.publish('v1/devices/me/telemetry', json.dumps(data), 1)
