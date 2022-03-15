#!/usr/bin/env python
from attr import NOTHING
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

init_pose = PoseStamped()
cntr = 0

def sub_callback(data):
    if (data != None):
        global cntr
        if (cntr == 0):
            global init_pose
            init_pose.pose.position.x = data.pose.pose.position.x
            init_pose.pose.position.y = data.pose.pose.position.y
            init_pose.pose.position.z = data.pose.pose.position.z
            init_pose.pose.orientation.w = data.pose.pose.orientation.w
        
        cntr += 1


def get_init_pose():
    rospy.init_node('get_init_pose', anonymous=True)

    rospy.Subscriber('odom', Odometry, sub_callback)

    publisher = rospy.Publisher('tb3_init_pose', PoseStamped, queue_size=50)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        global init_pose
        init_pose.header.stamp = rospy.get_rostime()
        init_pose.header.frame_id = 'odom'

        # rospy.loginfo(init_pose)
        
        publisher.publish(init_pose)

        rate.sleep()

if __name__ == '__main__':
    try:
        get_init_pose()
    except rospy.ROSInterruptException:
        pass
    rospy.spin()
