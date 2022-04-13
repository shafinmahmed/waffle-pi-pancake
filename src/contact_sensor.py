import rospy
from std_msgs.msg import Int32

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)  


def contact_sensor():
    rospy.init_node("contact_sensor", anonymous=True)

    pub = rospy.Publisher("contact_sensor", Int32, queue_size=100)

    attached = 0

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        input = GPIO.input(13)
        if (input == True):
            attached = 1 
        
        pub.publish(attached)

        rate.sleep()


if __name__ == '__main__':
    try:
        contact_sensor()
        rospy.spin()
    except rospy.ROSInterruptException:      #may want to change to rospy.ROSInterruptException:
        pass