import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#button GPIO18--12
SWITCH_PIN=12
GREEN_LED = 35
BLUE_LED = 33
GPIO.setmode(GPIO.BOARD)

GPIO.setup(GREEN_LED,GPIO.OUT)
GPIO.setup(BLUE_LED,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = 0

def blink_led(led_pin, interval=0.2):
    global state
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(interval)
    
        if GPIO.input(SWITCH_PIN) == GPIO.LOW:
            time.sleep(0.05)  
            if GPIO.input(SWITCH_PIN) == GPIO.LOW: 
                state = (state+1)%4
                print(f"state in blink: {state}")
                
                #time.sleep(0.1)
                break  

while True:
    switch_state = GPIO.input(SWITCH_PIN)
    button_pressed = GPIO.input(SWITCH_PIN) == GPIO.LOW
    
    if button_pressed:
        time.sleep(0.05)
        if GPIO.input(SWITCH_PIN) == GPIO.LOW:
            print(f"state in if: {state}")
            if state == 0:
                print(111111)
                GPIO.output(GREEN_LED,0)
                GPIO.output(BLUE_LED,1)
                print(11111)
            if state == 1:
                print(222222)
                blink_led(BLUE_LED)
            if state == 2:
                GPIO.output(BLUE_LED,0)
                GPIO.output(GREEN_LED,1)
            if state == 3:
                blink_led(GREEN_LED)
            if state == 0:
                print(111111)
                GPIO.output(GREEN_LED,0)
                GPIO.output(BLUE_LED,1)
                print(11111)    
            state = (state + 1) % 4
            #print(state)
            time.sleep(0.2)
            
            

            

