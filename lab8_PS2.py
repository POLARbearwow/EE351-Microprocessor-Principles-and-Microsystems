import smbus
import RPi.GPIO as GPIO
import time

# Initialize the I2C bus
bus = smbus.SMBus(1)  # Use I2C bus 1
PCF8591_ADDRESS = 0x48  # Address of the PCF8591 module

# GPIO Pin Definitions for LEDs
LED_X = 17  # LED for X-axis
LED_Y = 27  # LED for Y-axis
BUTTON_LED = 22  # LED for button (Z-axis)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_X, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.setup(BUTTON_LED, GPIO.OUT)

# Initialize PWM for LEDs
pwm_led_x = GPIO.PWM(LED_X, 100)  # 100 Hz frequency
pwm_led_y = GPIO.PWM(LED_Y, 100)
pwm_button_led = GPIO.PWM(BUTTON_LED, 100)

pwm_led_x.start(0)  # Start with 0% duty cycle
pwm_led_y.start(0)
pwm_button_led.start(0)

# Read analog value from a specific channel
def read_analog(channel):
    bus.write_byte(PCF8591_ADDRESS, channel)  # Select channel
    bus.read_byte(PCF8591_ADDRESS)  # Dummy read
    value = bus.read_byte(PCF8591_ADDRESS)  # Read actual value
    return value

# Map the joystick input to LED brightness or control range
def map_value(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Main loop
try:
    while True:
        # Read joystick values
        x_value = read_analog(0)  # Read X-axis value from channel 0
        y_value = read_analog(1)  # Read Y-axis value from channel 1
        button_value = read_analog(2)  # Read Z-axis button state from channel 2
        
        # Debugging: Print values
        print(f"X-axis: {x_value}, Y-axis: {y_value}, Button: {button_value}")
        
        # Map joystick values to LED brightness (0-100 for PWM duty cycle)
        led_brightness_x = map_value(x_value, 0, 255, 0, 100)
        led_brightness_y = map_value(y_value, 0, 255, 0, 100)
        
        # Update LEDs based on joystick movement
        pwm_led_x.ChangeDutyCycle(led_brightness_x)
        pwm_led_y.ChangeDutyCycle(led_brightness_y)
        
        # Check if button is pressed (threshold for button press detection)
        if button_value < 10:  # Adjust threshold based on your button
            pwm_button_led.ChangeDutyCycle(100)  # Turn on button LED
        else:
            pwm_button_led.ChangeDutyCycle(0)  # Turn off button LED
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program terminated")
    # Cleanup GPIO and PWM
    pwm_led_x.stop()
    pwm_led_y.stop()
    pwm_button_led.stop()
    GPIO.cleanup()
