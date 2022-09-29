from machine import Pin, PWM, I2C
import utime
from sh1106 import SH1106_I2C
from hcsr04 import HCSR04
from motor_driver import *
import math
import random

#i2c = I2C(0, sda=Pin(6), scl=Pin(7), freq=400000)
#oled = SH1106_I2C(128, 64, i2c)
#oled.rotate
sensor = HCSR04(trigger_pin=5, echo_pin=4, echo_timeout_us=1000000)
distance = sensor.distance_cm()
min_dist = 20 #min dist in centimetres
motor = motor_driver(0,1,2,3) #Set pins for motor A and B  M1A=Pin0,M1B=Pin1,M2A=Pin3,M2B=Pin4

def forward():
    motor.speed(100,100)
    
def reverse():
    motor.speed(-50,-50)
    
def turn_left():
    motor.speed(0,50)
    
def allstop():
    motor.brake()

def left_turn():
    motor.brake()
    utime.sleep(1)
    motor.speed(-50,50)

def right_turn():
    motor.brake()
    utime.sleep(1)
    motor.speed(50,-50)

manouver = [left_turn, right_turn] #randomise which way the robot will turn when an obstacle is detected

def robot():
    distance = sensor.distance_cm()
    print(distance)
    
    if distance >= min_dist:
        print("Path is clear")
        #oled.fill(0)
        #oled.text("Path is", 10,10)
        #oled.text("Clear",20,20)
        #oled.show
        forward()
    else:
        print("Collision likely")
        #oled.fill(0)
        #oled.text("Collision", 10,10)
        #oled.text("Likely", 20,20)
        #oled.show()
        #allstop()
        random.choice(manouver)()
        utime.sleep(2)
        
while True:            
    robot()
        
