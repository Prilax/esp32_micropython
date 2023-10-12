import machine
import time

# Define the GPIO pin numbers for the PIR sensor and relay
pir_pin = 12  # Replace with the actual GPIO pin number for the PIR sensor
relay_pin = 13  # Replace with the actual GPIO pin number for the relay

# Initialize the PIR sensor and relay
pir_sensor = machine.Pin(pir_pin, machine.Pin.IN)
relay = machine.Pin(relay_pin, machine.Pin.OUT)

# Function to activate the solenoid via the relay
def activate_solenoid():
    print("Motion detected. Activating solenoid.")
    relay.on()  # Turn on the relay to activate the solenoid
    time.sleep(2)# Keep the solenoid active for 2 seconds
    print("Deactivating solenoid.")
    relay.off()  # Turn off the relay

# Main loop
while True:
    if pir_sensor.value() == 1:  # PIR sensor detected motion
        activate_solenoid()  # Activate the solenoid
    time.sleep(0.1)  # Small delay between sensor readings