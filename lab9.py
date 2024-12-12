import RPi.GPIO as GPIO
import time
from lirc import RawConnection

# GPIO Pin setup
GPIO.setmode(GPIO.BCM)
RGB_LED_PIN = 17
GPIO.setup(RGB_LED_PIN, GPIO.OUT)
led = GPIO.PWM(RGB_LED_PIN, 100)  # Initialize PWM with 100 Hz frequency
led.start(0)

# LIRC connection setup
connection = RawConnection()

# Command to brightness mapping
CODES = {
    "ON/OFF": 0,
    "MODE": 25,
    "MUTE": 50,
    "PLUS": 100,
    "MINUS": 0,
}

def decode_signal():
    try:
        while True:
            data = connection.readline()  # Read raw data from IR receiver
            if data:
                code = data.split()[2]  # Extract the hexadecimal code
                print(f"Received code: {code}")
                if code in CODES:
                    brightness = CODES[code]
                    led.ChangeDutyCycle(brightness)  # Adjust brightness
                    print(f"Set brightness to {brightness}%")
    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        connection.close()
        led.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    decode_signal()
