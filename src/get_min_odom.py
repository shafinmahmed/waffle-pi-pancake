#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

min = PoseStamped()   # global PoseSstamped object that will be published
min_x = 0

min_y = 0

# callback function to process subscription data
def sub_callback(data):
    if (data != None):
        global min_x, min_y, min
        if (data.pose.pose.position.x < min_x):
            
            min_x = data.pose.pose.position.x

            # populate the PoseStamped object with the odom callback information
            min.pose.position.x = data.pose.pose.position.x

        if (data.pose.pose.position.y < min_y):
            min_y = data.pose.pose.position.y

            # populate the PoseStamped object with the odom callback information
            min.pose.position.y = data.pose.pose.position.y
        
        min.pose.orientation.w = 1.0


def get_min_odom():
    # initialize the node
    rospy.init_node('get_min_odom', anonymous=True)

    # subscribe to the /odom topic
    rospy.Subscriber('odom', Odometry, sub_callback)

    # create the publisher object to publish the initial pose information to /tb3_min topic
    publisher = rospy.Publisher('tb3_min', PoseStamped, queue_size=50)

    rate = rospy.Rate(10)   # 10 Hz refresh rate

    while not rospy.is_shutdown():
        global min

        # populate with time stamp information 
        min.header.stamp = rospy.get_rostime()
        min.header.frame_id = 'odom'
        
        # publish the PoseStamped object
        publisher.publish(min)

        rate.sleep()

if __name__ == '__main__':
    try:
        get_min_odom()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
