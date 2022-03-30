#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalID

def go_to_path_points():
    rospy.loginfo('RETURNING TO ORIGIN')

    # initialize node
    rospy.init_node('go_to_path_points', anonymous=True)

    #subscribe to /tb3_init_pose topic
    #rospy.Subscriber('tb3_init_pose', PoseStamped, ip_callback)

    # Publisher obect to publish goal to return to origin
    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=50)

    newGoal = PoseStamped()

    newGoal.pose.position.x = 1.0
    newGoal.pose.position.y = 0.0
    newGoal.pose.position.z = 0.0
    newGoal.pose.orientation.w = 1.0
    
    rate = rospy.Rate(10)

    flag = False

    while not rospy.is_shutdown():

        if (flag == False):

            newGoal.header.stamp = rospy.get_rostime()
            newGoal.header.frame_id = 'odom'

            temp = newGoal

            publisher.publish(temp)

            rospy.loginfo("SENT GOAL TO MOVE BASE")

            # flag = True

        rate.sleep()

if __name__ == '__main__':
    try:
        go_to_path_points()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass