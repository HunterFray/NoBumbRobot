from machine import Pin, I2C, PWM
import utime
from sh1106 import SH1106_I2C
from hcsr04 import HCSR04
import math
from motor import Motor, pico_motor_shim
from pimoroni import NORMAL_DIR, REVERSED_DIR


i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
oled = SH1106_I2C(128, 64, i2c)
oled.rotate(1)
sensor = HCSR04(trigger_pin=14, echo_pin=15,echo_timeout_us=1000000)
distance = sensor.distance_cm()
min_dist = 30

SPEED_SCALE = 5.4               # The scaling to apply to each motor's speed to match its real-world speed
DRIVING_SPEED = SPEED_SCALE     # The speed to drive the wheels at, from 0.0 to SPEED_SCALE
left = Motor(pico_motor_shim.MOTOR_1, direction=NORMAL_DIR, speed_scale=SPEED_SCALE)
right = Motor(pico_motor_shim.MOTOR_2, direction=REVERSED_DIR, speed_scale=SPEED_SCALE)


def backward(speed=DRIVING_SPEED):
    left.speed(-speed)
    right.speed(-speed)

def forward(speed=DRIVING_SPEED):
            left.speed(speed)
            right.speed(speed)
            
def robot():
    distance = sensor.distance_cm()
    print(distance)
    utime.sleep(1)
    
    if sensor.distance_cm() >= min_dist:
        print("no obstacles")
        oled.fill(0)
        oled.text("Distance: ", 10, 20)
        oled.text(str(distance), 10,30)
        oled.text("Path is", 10, 40)
        oled.text("clear", 10, 50)
        oled.show()
        forward()
    else:
        print("collision likely")
        oled.fill(0)
        oled.text("Distance: ", 10, 20)
        oled.text(str(distance),10,30)
        oled.text("Collision", 10,40)
        oled.text("Likely", 10,50)
        oled.show()
    

while True:
    robot()
    
        
    



   



   