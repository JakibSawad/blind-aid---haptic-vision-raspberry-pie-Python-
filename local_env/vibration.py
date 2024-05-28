import RPi.GPIO as GPIO
import time

# Define GPIO pins for vibration modules
dot_pin = 17  # GPIO pin for dot (.)
dash_pin = 27  # GPIO pin for dash (-)
space_pin = 22  # GPIO pin for space (/)

# Morse code dictionary
morse_code_dict = {
    '.': dot_pin,
    '-': dash_pin,
    '/': space_pin
}

# Function to activate vibration
def vibrate(pin, duration=0.5):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)  # Vibrate for the specified duration
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)  # Add a short delay between vibrations

try:
    GPIO.setmode(GPIO.BCM)
    
    # Setup GPIO pins
    GPIO.setup(dot_pin, GPIO.OUT)
    GPIO.setup(dash_pin, GPIO.OUT)
    GPIO.setup(space_pin, GPIO.OUT)

    # Read Morse code from file
    with open("morse_code_output.txt", "r") as file:
        morse_code = file.read().strip()

    # Iterate through Morse code and activate vibration accordingly
    for char in morse_code:
        if char in morse_code_dict:
            pin = morse_code_dict[char]
            if char == '/':
                vibrate(pin, 1)  # Longer duration for space
            else:
                vibrate(pin)  # Default duration for dot and dash
        elif char == ' ':
            # Pause for word spacing
            time.sleep(2)  # Adjust duration for word spacing

finally:
    GPIO.cleanup()
