#!/usr/bin/env pybricks-micropython

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

turnm = Motor(Port.C)

leftm = Motor(Port.D)
rightm = Motor(Port.A)

dist = UltrasonicSensor(Port.S1)

gyros = GyroSensor(Port.S2)

speed = 300

# leftm.run(speed)
# rightm.run(speed)

# start_angle = gyros.angle()

# while scan(turnm,dist)[1] > 200:
#     regulate(start_angle,speed,rightm,gyros,-20)

# leftm.brake()
# rightm.brake()


turn_left(leftm,rightm,gyros)


