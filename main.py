from machine import Pin, I2C
import utime
from sh1106 import SH1106_I2C
from hcsr04 import HCSR04

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = SH1106_I2C(128, 64, i2c)
sensor = HCSR04(trigger_pin=6, echo_pin=7,echo_timeout_us=1000000)
distance = sensor.distance_cm()
min_dist = 30
def dist():
    distance = sensor.distance_cm()
    print(distance)
    utime.sleep(1)
    oled.fill(0)
    oled.text("Distance: ", 10, 20)
    oled.text(str(distance),10,30)
    oled.show()

while True:
    dist()
    if sensor.distance_cm() >= min_dist:
        print("no obstacles")
    else:
        print("collision likely")
        
    



   



   