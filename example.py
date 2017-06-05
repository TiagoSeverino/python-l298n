import time
from l298n import *

#Motors Setup
MotorLeft = L298N(37, 35, 33)
MotorRight = L298N(40, 38, 36)

MotorLeft.Forward(50)
MotorRight.Forward(50)
time.sleep(5)
MotorLeft.Backward(50)
MotorRight.Backward(50)
time.sleep(5)
MotorLeft.Break(50)
MotorRight.Break(50)