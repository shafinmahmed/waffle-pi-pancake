#!/usr/bin/env python

import rospy
from gpiozero import Servo
from time import sleep
from actionlib_msgs.msg import GoalID

flag = False


def mb_callback(data):
    if (data.id == ''):     # condition to trigger sending return to origin goal to move_base_simple/goal
        rospy.logdebug("EXPLORE STOPPED")
        global flag
        flag = True

def servo_up():
    rospy.init_node("servo_node", anonymous=True)
    rospy.Subscriber('move_base/cancel', GoalID, mb_callback)

    rate = rospy.Rate(10)


    servo = Servo(17)
    
    while not rospy.is_shutdown():
        if (flag == True):
            try:
                rospy.loginfo("SERVO UP")
                servo.value = -0.5
            except KeyboardInterrupt:
                pass
        else:
            try:
                rospy.loginfo("SERVO DOWN")
                servo.value = 0.5
            except KeyboardInterrupt:
                pass

        rate.sleep()

# def do_servo_up():
#     global val
#     try:
#         while True:
#             servo.value = 0.0
#     except KeyboardInterrupt:      #may want to remove
#         print("Program stopped")

if __name__ == '__main__':
    try:
        servo_up()
        rospy.spin()
    except rospy.ROSInterruptException:      #may want to change to rospy.ROSInterruptException:
        pass