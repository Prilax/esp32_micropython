# toggle the state of led with button press
from machine import Pin

led = Pin(2,Pin.OUT)
button = Pin(0,Pin.IN)

while True:
    if not button.value():
        led.value(not led .value())
        print("LED TURNED ON" if led.value() else "LED TURNED OFF")
        
        while not button. value():
            pass