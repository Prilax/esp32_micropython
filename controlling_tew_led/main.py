#controlling two led

import machine
import time


Led_state_1 = 0
Last_change_1 = 0
Led_state_2 = 0
Last_change_2 = 0

def led_toggle_1(pin,pin,on_time,off_time):
    global Led_state_1
    global Last_change_1
    
    #create object for led
    Led_1 = machine.Pin(Pin1,machine.Pin.OUT)
    
    
    if (time.ticks_ms()-Last_change1)>=off_time and Led_state is 0:
        Last_change_1 = time.ticks_ms()
        Led_state_1 = 1
        Led.value(Led_state)
        print("LED IS ON")
   
    elif (time.ticks_ms()-Last_change1)>=off_time and Led_state is 1:
        Last_change_1 = time.ticks_ms()
        Led_state_1 = 0
        Led.value(Led_state)
        print("LED IS OFF")
def led_toggle_2(pin,pin,on_time,off_time):
    global Led_state_2
    global Last_change_2
     #create object for led
    Led_2 = machine.Pin(Pin2,machine.Pin.OUT)
    if (time.ticks_ms()-Last_change2)>=off_time and Led_state is 0:
        Last_change_2 = time.ticks_ms()
        Led_state_2 = 1
        Led.value(Led_state)
        print("LED IS On")
    elif (time.ticks_ms()-Last_change2)>=off_time and Led_state is 1:
        Last_change_2 = time.ticks_ms()
        Led_state_2 = 0
        Led.value(Led_state)
        print("LED IS OFF")


while True:
    try:
        led_toggle_1(2,1000,2000)
        led_toggle_2(4,2000,1000)
    except KeyboardInterrupt:
        print("EXIT")
        break
        
    


