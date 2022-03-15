#!/usr/bin/env python

import rospy
import math
import tf
from geometry_msgs.msg import Pose

def tf_listener_test():
    rospy.init_node('tf_listener_test', anonymous=True)
    listener = tf.TransformListener()

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/base_link', '/fiducial_2', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
        rospy.loginfo('trans: ' + str(trans[0]) + ' ' + str(trans[1]) + ' ' + str(trans[2]))


        rate.sleep()

if __name__ == '__main__':
    try:
        tf_listener_test()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass