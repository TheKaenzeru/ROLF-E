
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

import time

ev3 = EV3Brick()

m1 = Motor(Port.A)

m2 = Motor(Port.D)

gyros = GyroSensor(Port.S1)


def regulate(angle):
    delta = angle-gyros
    current_speed = m1.speed()
    m1.run(current_speed-10*delta)


m1.run(1000)
m2.run(1000)

ang = gyros.angle()

for i in range(100):
    regulate(ang)
    time.sleep(.1)

m1.brake()
m2.brake()