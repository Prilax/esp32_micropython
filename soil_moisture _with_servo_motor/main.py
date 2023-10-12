import machine
from machine import PWM, ADC
import time

# Define the PWM pin for the servo motor
servo_pin = machine.Pin(4, machine.Pin.OUT)
servo = PWM(servo_pin, freq=50)

# Define the ADC pin for the moisture sensor
moisture_pin = machine.Pin(18)
adc = ADC(moisture_pin)

# Function to control the servo based on moisture level
def control_servo():
    moisture_value = adc.read()
    if moisture_value < 3900:  # Adjust this threshold based on your sensor
        servo.duty(100)  # Adjust the duty cycle to set servo position (0-1023)
        print("Moisture level is low. Watering the plant.")
    else:
        servo.duty(0)  # Set servo to a different position for dry soil
        print("Moisture level is okay. No need to water the plant.")

try:
    while True:
        control_servo()
        time.sleep(1)  # Check moisture level every 60 seconds

except KeyboardInterrupt:
    servo.duty(0)  # Stop the servo when the program is interrupted
