#dealy with time module
#non blocking method

import machine
import time


    
   
    # variables
Led_state = 0
Last_change = 0
def led_toggle(pin,on_time,off_time):
    global Led_state
    global Last_change
     #create object for led
    Led = machine.Pin(pin,machine.Pin.OUT)
    if (time.ticks_ms()-Last_change)>=off_time and Led_state is 0:
        Last_change = time.ticks_ms()
        Led_state = 1
        Led.value(Led_state)
        print("LED IS ON")
    elif (time.ticks_ms()-Last_change)>=off_time and Led_state is 1:
        Last_change = time.ticks_ms()
        Led_state = 0
        Led.value(Led_state)
        print("LED IS OFF")
        
while True:
    try:
        led_toggle(8,1000,2000)
    except KeyboardInterrupt:
        print("EXIT")
        break
        
    