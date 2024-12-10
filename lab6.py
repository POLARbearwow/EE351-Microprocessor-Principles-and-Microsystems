import smbus  # For I2C communication with PCF8591
import time
import RPi.GPIO as GPIO

# Setup for the LEDs
RED_PIN = 29   # GPIO pin for the red LED
GREEN_PIN = 31  # GPIO pin for the green LED

# Setup for I2C and PCF8591 (I2C address is typically 0x48 for PCF8591)
I2C_BUS = 1  # I2C bus number (usually 1 on Raspberry Pi)
PCF8591_ADDRESS = 0x48  # I2C address for the PCF8591 (can be 0x48 or 0x49 depending on A0 pin)

# Initialize GPIO and PWM for the LEDs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

# Initialize PWM for red and green LEDs
pwm_red = GPIO.PWM(RED_PIN, 1000)
pwm_green = GPIO.PWM(GREEN_PIN, 1000)
pwm_red.start(0)
pwm_green.start(0)

# Initialize I2C bus
bus = smbus.SMBus(I2C_BUS)

def read_analog(channel):
    """
    Function to read the analog value from the PCF8591 using I2C.
    :param channel: Analog input channel (0 = AN0, 1 = AN1, 2 = AN2)
    :return: Analog value (0-255)
    """
    # The command to read from the PCF8591 (register 0x40 for reading AN0)
    command = channel  # 0x40 is the base command, adding channel gives the correct register
    bus.write_byte(PCF8591_ADDRESS, command)  # Write the command to select the channel
    time.sleep(0.1)  # Small delay to allow the ADC to settle
    value = bus.read_byte(PCF8591_ADDRESS)  # Read the analog value from the selected channel
    return value

def control_leds():
    """
    Function to control the LEDs based on joystick input.
    The X and Y axes control the PWM brightness of the red and green LEDs,
    and the SW button controls the blinking behavior or LED turning off.
    """
    try:
        while True:
            # Read joystick values from PCF8591 (VRX = AN2, VRY = AN1, SW = AN0)
            x_value = read_analog(1)  # VRX is connected to AN2
            y_value = read_analog(0)  # VRY is connected to AN1
            button_value = read_analog(2)  # SW button is connected to AN0
            
            # Print the joystick values for debugging
            print(f"Joystick values - X: {x_value}, Y: {y_value}, Button: {button_value}")
            
            # Scale the ADC values to 0-100 for PWM (scale from 0-255 to 0-100)
            pwm_red_value = (x_value / 255) * 100
            pwm_green_value = (y_value / 255) * 100  # Fixed typo here, removed the extra "a"

            # Update PWM duty cycles for red and green LED
            pwm_red.ChangeDutyCycle(pwm_red_value)
            pwm_green.ChangeDutyCycle(pwm_green_value)

            # Print PWM duty cycle values for debugging
            print(f"PWM Duty Cycle - Red: {pwm_red_value}%, Green: {pwm_green_value}%")

            # Check if SW button is pressed (value > 128 means pressed)
            if button_value > 128:  
                # When Z-axis button is pressed, turn off both LEDs
                print("Button pressed: LEDs will turn off.")
                GPIO.output(RED_PIN, GPIO.LOW)  # Turn off red LED
                GPIO.output(GREEN_PIN, GPIO.LOW)  # Turn off green LED
            else:
                # If SW button is not pressed, keep LEDs on with PWM brightness
                print("Button not pressed: LEDs will stay on with PWM brightness.")
                GPIO.output(RED_PIN, GPIO.HIGH)  # Keep red LED on
                GPIO.output(GREEN_PIN, GPIO.HIGH)  # Keep green LED on

            # Sleep briefly to avoid excessive CPU usage
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        # Gracefully handle exit on CTRL+C
        print("Program interrupted, cleaning up...")
        pwm_red.stop()
        pwm_green.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    print("Starting the joystick-controlled LED program.")
    control_leds()
