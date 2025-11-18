

#!/usr/bin/env pybricks-micropython
import time
import json

# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile


# Hier können Dateien mit eigenen Funktionen importiert werden
from funktionen import *


# Hier wird die angeschlossene Hardware definiert und konfiguriert
ev3 = EV3Brick()



m1 = Motor(Port.A)
m2 = Motor(Port.D)

dist = UltrasonicSensor(Port.S4)
touch = TouchSensor(Port.S1)

speed = -500

m1.run(speed)
m2.run(speed)


time.sleep(0.5)

goal = dist.distance()

for i in range(300):
    d = dist.distance()
    delta = goal-d # negativ, wenn zu nah an Wand
    m2.run(speed+delta*3)
    print(speed)
    time.sleep(.1)

m1.brake()
m2.brake()

