
from machine import I2C, Pin
from lib.pca9685 import PCA9685
from lib.servo import Servos

scl = Pin(1)
sda = Pin(0)
id = 0

i2c = I2C(id, sda=sda, scl=scl)

#pca1 = PCA9685(i2c = i2c)
#pca2 = PCA9685(i2c = i2c, address = 0x41)

# You can optionally provide a finer tuned reference clock speed to improve the accuracy of the
# timing pulses. This calibration will be specific to each board and its environment. See the
# calibration.py example in the PCA9685 driver.
# pca = PCA9685(i2c, reference_clock_speed=25630710)

#pca1.freq(freq=50)
#pca2.freq(freq=50)
servo1 = Servos(i2c = i2c, min_us=500, max_us=2550)
servo2 = Servos(i2c= i2c, address = 0x41, min_us=500, max_us=2550)

corxia1 = servo1
fermur1 = servo1
tidia1 = servo1

corxia2 = servo1
fermur2 = servo1
tidia2 = servo1

corxia3 = servo1
fermur3 = servo1
tidia3 = servo1

corxia6 = servo2
fermur6 = servo2
tidia6 = servo2

corxia5 = servo2
fermur5 = servo2
tidia5 = servo2

corxia4 = servo2
fermur4 = servo2
tidia4 = servo2

left_front =  [corxia1, fermur1, tidia1]
left_middle = [corxia2, fermur2, tidia2]
left_back = [corxia3, fermur3, tidia3]

right_front = [corxia4, fermur4, tidia4]
right_middle = [corxia5, fermur5, tidia5]
right_back = [corxia6, fermur6, tidia6]

pca_pin_number = [[0,1,2],[4,5,6],[8,9,10],
                  [8,9,10],[4,5,6],[0,1,2]]

leg_offset = [left_front, left_middle, 
              left_back, right_front, 
              right_middle, right_back]

#캘리브레이션 맞춘 각각의 서보 값은 90도는 아니지만 실재값은 90도이다.
left_front_angle = [87,100,100]
left_middle_angle = [104,100,90]
left_back_angle = [70,97,100]

right_back_angle = [97,60,90]
right_middle_angle = [90,75,110]
right_front_angle = [80,70,85]

leg_offset_angle = [left_front_angle, left_middle_angle, left_back_angle, 
                    right_front_angle, right_middle_angle, right_back_angle]


def check_calibration():
    for i in range(6):
        for x in range(3):
            leg_offset[i][x].position(index = pca_pin_number[i][x] , degrees = leg_offset_angle[i][x])