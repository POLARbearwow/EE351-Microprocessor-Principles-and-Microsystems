import RPi.GPIO as GPIO
import time


GREEN_LED = 18 
RED_LED = 16    
DELAY = 0.5    

# 初始化GPIO设置
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def led_blink():
    try:
        while True:
            GPIO.output(GREEN_LED, GPIO.HIGH)
            GPIO.output(RED_LED, GPIO.LOW)
            time.sleep(DELAY)

            GPIO.output(GREEN_LED, GPIO.LOW)
            GPIO.output(RED_LED, GPIO.HIGH)
            time.sleep(DELAY)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("程序已终止，GPIO清理完毕。")

led_blink()
