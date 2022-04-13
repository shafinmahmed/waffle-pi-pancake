#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
from std_msgs.msg import Int32

from geometry_msgs.msg import Twist

detected = False

twist = Twist()

def ar_callback(data):
    global detected, twist
    if (data != None):
        detected = True
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0

        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0



def stop_explore():
    rospy.init_node("stop_explore", anonymous=True)

    rospy.Subscriber('visulization_marker/ArUco_Location_0', Marker, ar_callback)

    pub = rospy.Publisher("explore_cancel_0", Int32, queue_size=100)
    pub2 = rospy.Publisher("cmd_vel", Twist, queue_size=10)

    msg = -1

    rate = rospy.Rate(10)

    global twist


    while not rospy.is_shutdown():

        if (detected == True):
            msg = 0
            #pub2.publish(twist)
        
        rospy.loginfo(msg)
        pub.publish(msg)

        rate.sleep()


if __name__ == "__main__":
    try:
        stop_explore()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
