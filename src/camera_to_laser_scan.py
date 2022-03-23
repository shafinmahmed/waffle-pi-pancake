#!/usr/bin/env python
from math import sqrt
from math import atan2

import rospy
from visualization_msgs.msg import Marker
from sensor_msgs.msg import LaserScan

# global variables for fake scan parameters
box_angle = 0
box_distance = 0
box_id = "0"
time_secs = 0
time_nsecs = 0

# callback function for Aruco marker location 
def cb_laserScan(data):
    global box_angle, box_distance, box_id, time_secs, time_nsecs
    
    # populate with fake scan parameters
    box_angle = atan2(data.pose.position.y, data.pose.position.x)
    box_distance = sqrt((data.pose.position.x * data.pose.position.x) + (data.pose.position.y * data.pose.position.y))
    box_id = "0"
    time_secs = data.header.stamp.secs
    time_nsecs = data.header.stamp.nsecs

def camera_to_laser_scan():
    # initialize node
    rospy.init_node('camera_to_laser_scan', anonymous=True)

    # subscribe to topic publishing the location of the Aruco marker
    rospy.Subscriber('visulization_marker/ArUco_Location_0', Marker, cb_laserScan) 

    # publisher to publish fake scan information
    publisher = rospy.Publisher('camera_to_laser_scan', LaserScan, queue_size=50) 

    rate = rospy.Rate(10) # 10 Hz refresh rate

    while not rospy.is_shutdown():
        global box_angle, box_distance, box_id, time_secs, time_nsecs

        laserScan = LaserScan() # fake scan object

        # populate with fake scan parameters
        laserScan.header.stamp.secs = time_secs
        laserScan.header.stamp.nsecs = time_nsecs
        laserScan.header.frame_id = 'map'
        laserScan.angle_min = box_angle
        laserScan.angle_max = box_angle + 0.0001
        laserScan.range_min = 0.0
        laserScan.range_max = 20
        laserScan.angle_increment = 0.0001
        laserScan.time_increment = 0.0001
        laserScan.ranges = [box_distance, box_distance]
        
        publisher.publish(laserScan)

        rate.sleep()

if __name__ == '__main__':
    try:
        camera_to_laser_scan()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
