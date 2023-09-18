#micropython script

#controlling the neopixel led

import machine
import neopixel
import time

#object for neopixel led

np =neopixel.NeoPixel(machine.Pin(48),1)

while True:
    try:
        np[0] =[255,255,0]
        np.write()
        time.sleep(2)
        np[0] =[0,255,0]
        np.write()
        time.sleep(2)
        np[0] =[0,0,255]
        np.write()
        time.sleep(2)
    except KeyboardInterrupt:
        print("EXIT")
        break