#!/usr/bin/env python

#import rospy
from gpiozero import Servo
from time import sleep

servo = Servo(17)

def do_servo_up():
    global val
    try:
        while True:
            servo.value = 0.0
    except KeyboardInterrupt:      #may want to remove
        print("Program stopped")

if __name__ == '__main__':
    try:
        do_servo_up()
    except KeyboardInterrupt:      #may want to change to rospy.ROSInterruptException:
        pass

