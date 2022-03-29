#!/usr/bin/env python
from math import sqrt
from math import atan2

import rospy
from visualization_msgs.msg import Marker
from sensor_msgs.msg import LaserScan
import tf

# global variables for fake scan parameters
box_angle = 0
box_distance = 0
box_id = "0"
time_secs = 0
time_nsecs = 0
flag = True
tempLaserScan = LaserScan()


def camera_to_laser_scan():
    # initialize node
    rospy.init_node('camera_to_laser_scan', anonymous=True)

    # publisher to publish fake scan information
    publisher = rospy.Publisher('camera_to_laser_scan', LaserScan, queue_size=50) 

    rate = rospy.Rate(10) # 10 Hz refresh rate

    listener = tf.TransformListener()


    rate = rospy.Rate(10)       # 10 Hz refresh rate

    while not rospy.is_shutdown():
        try:
            # lookup transform between map and fiducial_0 
            (trans,rot) = listener.lookupTransform('/map', '/fiducial_0', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        global box_angle, box_distance, box_id, time_secs, time_nsecs
        
        # populate with fake scan parameters
        box_angle = atan2(trans[1], trans[0])
        box_distance = sqrt((trans[0] * trans[0]) + (trans[1] * trans[1]))
        box_id = "0"

        laserScan = LaserScan() # fake scan object
        global tempLaserScan

        # populate with fake scan parameters
        laserScan.header.stamp = rospy.get_rostime()
        laserScan.header.frame_id = 'map'
        laserScan.angle_min = box_angle - 0.01
        laserScan.angle_max = box_angle + 0.01
        laserScan.range_min = 0.0
        laserScan.range_max = 20
        laserScan.angle_increment = 0.0001
        laserScan.time_increment = 0.0001
        laserScan.ranges = [box_distance, (box_distance + 0.05), (box_distance + 0.05*2), (box_distance + 0.05*3)]
        
        publisher.publish(laserScan)

        rate.sleep()

if __name__ == '__main__':
    try:
        camera_to_laser_scan()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
