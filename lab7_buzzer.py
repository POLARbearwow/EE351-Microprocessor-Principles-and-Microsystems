import RPi.GPIO as GPIO
import time

# Set up the GPIO mode and pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

# Set up PWM on pin 18 (GPIO 18)
pwm = GPIO.PWM(18, 1000)  # Initial frequency set to 1000 Hz (which will be adjusted later)

# Define the note frequencies (in Hz)
notes = {
    '1': 261,  # C4
    '2': 293,  # D4
    '3': 329,  # E4
    '4': 349,  # F4
    '5': 392,  # G4
    '6': 440,  # A4
    '7': 493   # B4
}

# Define the melody (note and duration)
melody = [
    ('1', 0.5), ('1', 0.5), ('5', 0.5), ('5', 0.5), ('6', 0.5), ('6', 0.5), ('5', 1),
    ('4', 0.5), ('4', 0.5), ('3', 0.5), ('3', 0.5), ('2', 0.5), ('2', 0.5), ('1', 1),
    ('5', 0.5), ('5', 0.5), ('4', 0.5), ('4', 0.5), ('3', 0.5), ('3', 0.5), ('2', 1),
    ('5', 0.5), ('5', 0.5), ('4', 0.5), ('4', 0.5), ('3', 0.5), ('3', 0.5), ('2', 1),
    ('1', 0.5), ('1', 0.5), ('5', 0.5), ('5', 0.5), ('6', 0.5), ('6', 0.5), ('5', 1),
    ('4', 0.5), ('4', 0.5), ('3', 0.5), ('3', 0.5), ('2', 0.5), ('2', 0.5), ('1', 1)
]

# Function to generate beep sound using PWM
def beep(frequency, duration):
    pwm.ChangeFrequency(frequency)  # Change the PWM frequency to match the note
    pwm.start(50)  # Start PWM with 50% duty cycle (this is enough to create a tone)
    time.sleep(duration)  # Play the tone for the specified duration
    pwm.stop()  # Stop PWM after the note is played

# Play the melody
print("Starting the melody...")
for note, duration in melody:
    print(f"Playing note {note} for {duration} seconds.")
    beep(notes[note], duration)
    time.sleep(0.1)

print("Melody finished.")
GPIO.cleanup()

