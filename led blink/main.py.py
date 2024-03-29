#micro python script for esp32s3

#blink the led and print led state on terminal
from machine import Pin
from time import sleep

#create object for led pin
led = Pin(2,Pin.OUT)

#global variable
led_state = True

#blink the led forever
#print the state of led on terminal

while True:
    led_state = not led_state
    led.value(led_state)
    print("LED TURNED ON" if led_state else "LED TURNED OFF")
    sleep(0.1)
