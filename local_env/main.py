import RPi.GPIO as GPIO
import time
import threading
import subprocess

# Pin Definitions
button_pin = 23  # Use GPIO pin 23

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button pin set as input with pull-up resistor

# Variable to track if Enter key was pressed
exit_requested = False

# Function to wait for Enter key press in a separate thread
def wait_for_enter():
    global exit_requested
    input("Press Enter to exit...\n")
    exit_requested = True

# Function to run a Python script and print a success or error message
def run_python_script(script_path, success_message, error_message):
    try:
        # Run the Python script
        subprocess.run(["python", script_path], check=True)
        print(success_message)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path}: {e}")
        print(error_message)

def main():
    # Paths to the scripts you want to run
    imagecapture_script = "/home/sakibjawad/Downloads/299 project/local_env/imagecapture.py"
    predict_script = "/home/sakibjawad/Downloads/299 project/local_env/predict.py"
    txt_to_morse_script = "/home/sakibjawad/Downloads/299 project/local_env/txt_to_morse.py"
    vibration_script = "/home/sakibjawad/Downloads/299 project/local_env/vibration.py"

    try:
        # Start the thread that waits for Enter key press
        threading.Thread(target=wait_for_enter, daemon=True).start()

        while not exit_requested:
            button_state = GPIO.input(button_pin)
            if button_state == GPIO.LOW:  # Button is pressed
                run_python_script(imagecapture_script, "Image successfully captured.", "Error capturing image.")
                run_python_script(predict_script, "Prediction script executed successfully.", "Error running prediction script.")
                run_python_script(txt_to_morse_script, "Text successfully converted to Morse code.", "Error converting text to Morse code.")
                run_python_script(vibration_script, "Vibration activated successfully.", "Error activating vibration.")
                time.sleep(1)  # Debounce delay
            else:
                print("Waiting")
                time.sleep(0.5)  # Delay to avoid flooding the terminal

    except KeyboardInterrupt:
        print("Exiting gracefully")

    finally:
        GPIO.cleanup()  # Clean up GPIO on exit

if __name__ == "__main__":
    main()
