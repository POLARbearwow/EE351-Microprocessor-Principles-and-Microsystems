import smbus
import time
import math

# Initialize I2C bus
bus = smbus.SMBus(1)  # Use I2C bus 1
PCF8591_address = 0x48  # PCF8591 I2C address

# Constants for thermistor calculation
R_known = 10000  # Known resistance value in ohms
V_input = 5.0  # Input voltage in volts
R0 = 10000  # Thermistor resistance at T0 in ohms
B = 3950  # B constant of thermistor
T0 = 298.15  # Standard temperature in Kelvin (25°C)

# Function to read analog input from PCF8591
def read_analog_input():
    bus.write_byte(PCF8591_address, 0x00)  # Set PCF8591 to channel 0
    bus.read_byte(PCF8591_address)  # Dummy read to initialize
    analog_value = bus.read_byte(PCF8591_address)  # Read the actual value
    return analog_value

# Function to convert ADC value to voltage
def adc_to_voltage(adc_value):
    voltage = (adc_value / 255.0) * V_input
    return voltage

# Function to calculate thermistor resistance
def calculate_thermistor_resistance(voltage):
    if voltage == 0:
        return None
    R_thermistor = R_known * voltage / (V_input - voltage)
    return R_thermistor

# Function to calculate temperature from resistance
def calculate_temperature(R_thermistor):
    if R_thermistor is None:
        return None
    temperature_kelvin = 1 / (1 / T0 + (1 / B) * math.log(R_thermistor / R0))
    temperature_celsius = temperature_kelvin - 273.15
    return temperature_celsius

# Main loop
while True:
    adc_value = read_analog_input()  # Read analog input
    voltage = adc_to_voltage(adc_value)  # Convert to voltage
    R_thermistor = calculate_thermistor_resistance(voltage)  # Calculate resistance
    temperature_celsius = calculate_temperature(R_thermistor)  # Calculate temperature

    if temperature_celsius is not None:
        print(f"ADC: {adc_value}, Voltage: {voltage:.2f}V, Temperature: {temperature_celsius:.2f}°C")
    else:
        print("Error: Voltage is zero, unable to calculate temperature.")

    time.sleep(1)  # Delay for 1 second
