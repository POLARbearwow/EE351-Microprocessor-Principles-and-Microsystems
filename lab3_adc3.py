import smbus
import time

bus = smbus.SMBus(1)
PCF8591_address = 0x48

def set_LED_brightness(brightness):
    if 0 <= brightness <= 255:
        bus.write_byte_data(PCF8591_address, 0x40, brightness)

def breathing_LED():
    try:
        while True:
            for brightness in range(0, 256):
                set_LED_brightness(brightness)
                time.sleep(0.01)  # Adjust this for speed of brightness increase

            for brightness in range(255, -1, -1):
                set_LED_brightness(brightness)
                time.sleep(0.01)  # Adjust this for speed of brightness decrease
    except KeyboardInterrupt:
        print("Breathing LED effect stopped")

breathing_LED()
