from machine import Pin
from shadow.candle_shadow import CandleShadow

led = Pin(32, Pin.OUT)
led.value(True)


shadows = [
    CandleShadow("0")
]

# TESTING: Subscribe to MQTT topic, use it to turn on and off candle
HUB_TOPIC = b"hub/shadow/#"
    
def handle_mqtt(topic, message):
    print(topic)
    print(message)
    
mqttc.set_callback(handle_mqtt)
mqttc.subscribe(HUB_TOPIC)


while True:
    mqttc.check_msg()