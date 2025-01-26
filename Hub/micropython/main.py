from machine import Pin
from time import sleep

led = Pin(32, Pin.OUT)
led.value(True)



# TESTING: Subscribe to MQTT topic, use it to turn on and off LED
LED_TOPIC = b"/test/hub/command/led"
def set_led_state(topic, msg):
    if msg.decode() == "1":
        led.value(1)
    else:
        led.value(0)
    
mqttc.set_callback(set_led_state)
mqttc.subscribe(LED_TOPIC)
    
while True:
    mqttc.check_msg()
    sleep(0.5)