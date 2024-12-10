
import smbus
import time

bus = smbus.SMBus(1)
PCF8591_address = 0x48

def read_analog_input():
    # Read the value from the analog input (ADC channel 0)
    analog_value = bus.read_byte_data(PCF8591_address, 0x00)
    return analog_value

def convert_to_voltage(analog_value):
    voltage = (analog_value / 255.0) * 3.3
    return voltage

try:
    while True:
        # Read analog input value
        analog_value = read_analog_input()
        
        # Convert analog value to voltage
        voltage = convert_to_voltage(analog_value)
        
        # Print the voltage
        print(f"Current voltage: {voltage:.2f} V")
        
        # Wait for a short time before the next reading
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Program terminated")
