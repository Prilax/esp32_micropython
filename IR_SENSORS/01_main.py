import machine
import utime

ir_pin = machine.Pin(18, machine.Pin.IN)  # Replace 14 with the actual pin number you're using

while True:
    ir_value = ir_pin.value()
    if ir_value == 1:
        print("No IR detected!")
    else:
        print("IR detected.")
    utime.sleep(1)  # Adjust the sleep time as needed
