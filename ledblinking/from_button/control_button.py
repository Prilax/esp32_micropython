#micro python script

#led blinking script

import machine
import time

#create object for LED pin

#led_pin = machine.Pin(8,machine.Pin.OUT)

led = machine.Pin(8,machine.Pin.OUT)

#object for button
button =mac
while True:
    try:
         ''' led_pin.on()
       # led_pin.value(1)
        print("LED IS ON")
        time.sleep(1)
       # led_pin(0)
        print("LED IS OF")
        time.sleep(1)'''
         led.value(not led.value())
         print("LED IS ON" if led.value() else "LED IS OFF")
         time.sleep(1)
    except KeyboardInterrupt:
        print("EXIT")
        break
    
        