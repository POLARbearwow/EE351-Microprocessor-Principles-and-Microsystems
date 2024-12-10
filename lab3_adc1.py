import smbus
import time

bus = smbus.SMBus(1)
PCF8591_address = 0x48

def set_LED_brightness(brightness):
    if 0 <= brightness <= 255:
        bus.write_byte_data(PCF8591_address, 0x42, brightness)
    else:
        print("Brightness value should be between 0 and 255")

try:
    while True:
        brightness = int(input("Please enter the LED brightness (0-255): "))
        set_LED_brightness(brightness)
        print(f"Current LED brightness set to: {brightness}")
except KeyboardInterrupt:
    print("Program terminated")



