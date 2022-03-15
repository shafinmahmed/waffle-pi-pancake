#!/usr/bin/env python
import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

currPose = Odometry()


def sub_callback(data):
    global currPose
    if (currPose != None):
        currPose = data


def tf_broadcaster_test():
    rospy.init_node('tf_broadcaster_test', anonymous=True)
    rospy.Subscriber('odom', Odometry, sub_callback)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        br = tf.TransformBroadcaster()

        br.sendTransform((currPose.pose.pose.position.x, currPose.pose.pose.position.y, currPose.pose.pose.position.z), (currPose.pose.pose.orientation.x, currPose.pose.pose.orientation.y, currPose.pose.pose.orientation.z, currPose.pose.pose.orientation.w), rospy.Time.now(), currPose.child_frame_id, "/base_link")

        rate.sleep()

if __name__ == '__main__':
    try:
        tf_broadcaster_test()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

