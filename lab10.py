#!/usr/bin/python3                             
#-*- coding:utf-8 -*-               
import RPi.GPIO as GPIO                #导入RPi.GPIO库
import time                            #导入time库   

LED_RED = 26                            #红色LED引脚号
LED_GREEN = 19                          #绿色LED引脚号
KEY = 6                                 #按键引脚号

GPIO.setwarnings(False)                 #不加这句会有警告，因为该引脚已经被设置成了非默认值（也可以不加，不影响正常使用）
GPIO.setmode(GPIO.BCM)                  #使用BCM编码的引脚号
GPIO.setup(LED_RED, GPIO.OUT)           #配置红色LED引脚模式
GPIO.setup(LED_GREEN, GPIO.OUT)         #配置绿色LED引脚模式
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)  #设置KEY引脚模式

global led_status                       #记录LED电平状态（全局变量）
global blink_mode                       #记录是否处于闪烁模式
led_status = 0                           #初始时LED处于关闭状态
blink_mode = True                        #初始状态为闪烁模式

# 按键中断处理函数
def KEYInterrupt(KEY):
    #global blink_mode
    print(11111111)
    #if not blink_mode:  # 如果当前是常亮状态（切换模式为常亮）
    start_time=time.time()
    while time.time()-start_time < 3:
        GPIO.output(LED_RED, GPIO.HIGH)  # 红色LED常亮
        GPIO.output(LED_GREEN, GPIO.HIGH)  # 绿色LED常亮
        print("LEDs are ON (Constant Mode)")
    
    # 保持常亮2秒
    #time.sleep(3)
    print(22222)    
        # 返回主程序继续闪烁模式
        #blink_mode = True
        #print("LEDs are in Blink Mode")
    #else:
        #print("Already in Blink Mode")

# 按钮按下触发中断
GPIO.add_event_detect(KEY, GPIO.FALLING, KEYInterrupt, bouncetime=200)  # 200ms消抖

# 红绿LED交替闪烁函数
def blink_leds():
    global led_status
    if blink_mode:  # 如果是闪烁模式
        if led_status:
            GPIO.output(LED_RED, GPIO.HIGH)  # 红灯亮
            GPIO.output(LED_GREEN, GPIO.LOW)  # 绿灯灭
        else:
            GPIO.output(LED_RED, GPIO.LOW)   # 红灯灭
            GPIO.output(LED_GREEN, GPIO.HIGH) # 绿灯亮
        led_status = not led_status         # 切换状态
    time.sleep(1)  # 延时1秒

# 主循环
while True:
    blink_leds()
