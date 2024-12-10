import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
SWITCH_PIN = 12
GREEN_LED = 35
BLUE_LED = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        button_pressed = GPIO.input(SWITCH_PIN) == GPIO.LOW

        if button_pressed:
            GPIO.output(BLUE_LED, GPIO.HIGH)
            GPIO.output(GREEN_LED, GPIO.LOW)
        else:
            GPIO.output(GREEN_LED, GPIO.HIGH)
            GPIO.output(BLUE_LED, GPIO.LOW)

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
