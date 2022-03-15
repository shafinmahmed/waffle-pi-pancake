#!/usr/bin/env python
import rospy
from fiducial_msgs.msg import FiducialTransformArray
from std_msgs.msg import String, Int32
import numpy as np

aruco_box = [0, 0, 0, 0]

box_info = ''

a = FiducialTransformArray()

def sub_callback(data):
    if (len(data.transforms) != 0):
        global box_info
        box_info = 'x: ' + str(data.transforms[0].transform.translation.x) + ' y: ' + str(data.transforms[0].transform.translation.y) + ' z: ' + str(data.transforms[0].transform.translation.y)
    

def locate_marker():
    rospy.init_node('aruco_transform', anonymous=True)

    rospy.Subscriber('fiducial_transforms', FiducialTransformArray, sub_callback)

    publisher = rospy.Publisher('aruco_transform', String, queue_size=50)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        publisher.publish(box_info)
    
    rate.sleep()




if __name__ == '__main__':
    try:
        locate_marker()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass