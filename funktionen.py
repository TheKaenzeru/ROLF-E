# In dieser Datei können eigene Funktionen definiert werden. Es können auch weitere Dateien angelegt werden, die dann in main.py importiert werden müssen

# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# Beispiel für eine Funktion: Piept sobald wenn der Touch-Sensor gedrückt wird
def piep(ev3, sensor_touch):
    while(not sensor_touch.pressed()):
        pass # Dauerschleife bis Sensor gedrückt wird
    ev3.speaker.beep() # Piepton




def own_run_angle(motor,angle,speed):
    start = motor.angle()
    if angle < 1:
        motor.run(-speed)
        while motor.angle() > start+angle:
            pass
        motor.brake()
    else:
        motor.run(speed)
        while motor.angle() < start+angle:
            pass
        motor.brake()


def scan(motor,sensor):
    turn_angle = 90*0.65
    speed = 300
    left = sensor.distance()
    time.sleep(.01)
    own_run_angle(motor,turn_angle-motor.angle(),speed)
    front = sensor.distance()
    own_run_angle(motor,turn_angle,speed)
    right = sensor.distance()
    own_run_angle(motor,-2*turn_angle,speed)
    print(motor.angle())
    return left, front, right

def regulate(goal_angle,speed,motor,gyros,upspeed):
    delta = goal_angle-gyros.angle()
    print(delta,gyros.angle())
    motor.run(speed+delta*upspeed)



def turn_left(left,right,gyros):
    right.run(1000)
    start = gyros.angle()
    while gyros.angle > start-90:
        pass
    right.brake()

