#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

init_pose = PoseStamped()   # global PoseSstamped object that will be published
cntr = 0

# callback function to process subscription data
def sub_callback(data):
    if (data != None):
        global cntr
        if (cntr == 0):     # only process the very first piece of data received 
            global init_pose

            # populate the PoseStamped object with the odom callback information
            init_pose.pose.position.x = data.pose.pose.position.x
            init_pose.pose.position.y = data.pose.pose.position.y
            init_pose.pose.position.z = data.pose.pose.position.z
            init_pose.pose.orientation.w = data.pose.pose.orientation.w
        
        cntr += 1


def get_init_pose():
    # initialize the node
    rospy.init_node('get_init_pose', anonymous=True)

    # subscribe to the /odom topic
    rospy.Subscriber('odom', Odometry, sub_callback)

    # create the publisher object to publish the initial pose information to /tb3_init_pose topic
    publisher = rospy.Publisher('tb3_init_pose', PoseStamped, queue_size=50)

    rate = rospy.Rate(10)   # 10 Hz refresh rate

    while not rospy.is_shutdown():
        global init_pose

        # populate with time stamp information
        init_pose.header.stamp = rospy.get_rostime()
        init_pose.header.frame_id = 'odom'
        
        # publish the PoseStamped object
        publisher.publish(init_pose)

        rate.sleep()

if __name__ == '__main__':
    try:
        get_init_pose()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
