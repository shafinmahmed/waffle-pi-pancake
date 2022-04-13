#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
from std_msgs.msg import Int32

detected = False

def ar_callback(data):
    global detected
    if (data != None):
        detected = True

def stop_explore():
    rospy.init_node("stop_explore", anonymous=True)

    rospy.Subscriber('visulization_marker/ArUco_Location_1', Marker, ar_callback)

    pub = rospy.Publisher("explore_cancel_1", Int32, queue_size=100)

    msg = -1

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if (detected == True):
            msg = 1
        
        rospy.loginfo(msg)
        pub.publish(msg)

        rate.sleep()


if __name__ == "__main__":
    try:
        stop_explore()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
