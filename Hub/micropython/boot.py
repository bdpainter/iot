# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import machine
import network
import ubinascii

from secrets import mqtt as mqtt_secrets
from secrets import wifi
from umqtt.simple import MQTTClient

esp.osdebug(None)
import gc
gc.collect()


# Set up WiFi
####################
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(wifi.SSID, wifi.PASSWORD)

while not station.isconnected():
    pass

print("Wifi connection successful")
print(station.ifconfig())


# Set up MQTT connection
#########################
client_id = ubinascii.hexlify(machine.unique_id())
MQTT_CLIENT_NAME = b"TestHub_" + client_id
mqttc = MQTTClient(MQTT_CLIENT_NAME, mqtt_secrets.MQTT_SERVER,
                   user=mqtt_secrets.MQTT_USER, password=mqtt_secrets.MQTT_PASSWORD)
mqttc.connect()
                   