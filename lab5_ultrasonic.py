import RPi.GPIO as GPIO
import time

# GPIO 引脚定义
TRIG_PIN = 17  # 触发信号引脚
ECHO_PIN = 18  # 回波信号引脚

# 初始化 GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    # 触发信号 - 高电平持续 10 微秒
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)  # 10 微秒
    GPIO.output(TRIG_PIN, False)
    
    # 等待回波信号开始
    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()
    
    # 等待回波信号结束
    while GPIO.input(ECHO_PIN) == 1:
        end_time = time.time()
    
    # 计算往返时间
    time_elapsed = end_time - start_time
    # 计算距离 (声速 343 m/s)
    distance = (time_elapsed * 34300) / 2  # 单位：厘米
    return distance

try:
    while True:
        distance = measure_distance()
        print(f"Measured Distance: {distance:.2f} cm")
        time.sleep(1)  # 1 秒测量一次

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
