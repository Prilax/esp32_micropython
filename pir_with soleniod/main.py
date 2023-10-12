import machine
import time

# Define GPIO pin for PIR sensor and relay control pin
pir_pin = machine.Pin(14, machine.Pin.IN)  # Replace with the appropriate pin number
relay_pin = machine.Pin(12, machine.Pin.OUT)  # Replace with the appropriate pin number

# Initialize the relay
relay = machine.Pin(relay_pin, machine.Pin.OUT)
relay.off()  # Make sure the solenoid is initially off

while True:
    if pir_pin.value():
        print("Motion detected!")
        relay.on()  # Turn on the relay to activate the solenoid
        time.sleep(2)  # Keep the solenoid on for 2 seconds (adjust as needed)
        relay.off()  # Turn off the relay to deactivate the solenoid
    else:
        print("No motion detected.")
    time.sleep(1)  # Delay to reduce sensor reading frequency (adjust as needed)
