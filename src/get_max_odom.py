#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

max = PoseStamped()   # global PoseSstamped object that will be published
max_x = 0

max_y = 0

# callback function to process subscription data
def sub_callback(data):
    if (data != None):
        global max_x, max_y, max
        if (data.pose.pose.position.x > max_x):
            
            max_x = data.pose.pose.position.x

            # populate the PoseStamped object with the odom callback information
            max.pose.position.x = data.pose.pose.position.x

        if (data.pose.pose.position.y > max_y):
            max_y = data.pose.pose.position.y

            # populate the PoseStamped object with the odom callback information
            max.pose.position.y = data.pose.pose.position.y
        
        max.pose.orientation.w = 1.0


def get_max_odom():
    # initialize the node
    rospy.init_node('get_max_odom', anonymous=True)

    # subscribe to the /odom topic
    rospy.Subscriber('odom', Odometry, sub_callback)

    # create the publisher object to publish the initial pose information to /tb3_init_pose topic
    publisher = rospy.Publisher('tb3_max', PoseStamped, queue_size=50)

    rate = rospy.Rate(10)   # 10 Hz refresh rate

    while not rospy.is_shutdown():
        global max

        # populate with time stamp information 
        max.header.stamp = rospy.get_rostime()
        max.header.frame_id = 'odom'
        
        # publish the PoseStamped object
        publisher.publish(max)

        rate.sleep()

if __name__ == '__main__':
    try:
        get_max_odom()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
