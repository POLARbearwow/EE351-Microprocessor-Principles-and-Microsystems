import smbus
import time
import math

bus = smbus.SMBus(1)
PCF8591_address = 0x48

R_known = 1000  
V_input = 3.3 
R0 = 960    
B = 3950       
T0 = 298.15    

def read_analog_input():
    bus.write_byte(PCF8591_address, 0x02)
    analog_value = bus.read_byte(PCF8591_address)
    return analog_value

def adc_to_voltage(adc_value):
    voltage = (adc_value / 255.0) * V_input
    return voltage

def calculate_thermistor_resistance(voltage):
    if voltage == 0:
        return None
    R_thermistor = R_known * voltage / (V_input - voltage)
    print(R_thermistor)
    return R_thermistor

def calculate_temperature(R_thermistor):
    if R_thermistor is None:
        return None
    temperature_kelvin = 1 / (1 / T0 + (1 / B) * math.log(R_thermistor / R0))
    temperature_celsius = temperature_kelvin - 273.15
    return temperature_celsius

while True:
    adc_value = read_analog_input()
    voltage = adc_to_voltage(adc_value)
    R_thermistor = calculate_thermistor_resistance(voltage)
    temperature_celsius = calculate_temperature(R_thermistor)

    if temperature_celsius is not None:
        print(f"Analog input: {adc_value}, Voltage: {voltage:.2f}V, Temperature: {temperature_celsius:.2f} c")
    else:
        print("Error: Unable to calculate temperature (voltage is zero)")

    time.sleep(1)
