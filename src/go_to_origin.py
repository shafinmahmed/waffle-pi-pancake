#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalID


flag = False
origGoal = PoseStamped()

def mb_callback(data):
    if (data.id == ''):
        global flag
        flag = True

def ip_callback(data):
    if (data != None):
        global origGoal
        origGoal = data


def go_to_origin():
    rospy.loginfo('RETURNING TO ORIGIN')
    rospy.init_node('go_to_origin', anonymous=True)
    rospy.Subscriber('move_base/cancel', GoalID, mb_callback)
    rospy.Subscriber('tb3_init_pose', PoseStamped, ip_callback)

    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=50)
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if (flag == True):
            goal = origGoal

            # rospy.loginfo(goal)
            publisher.publish(goal)
            
            global flag
            flag = False

        rate.sleep()

if __name__ == '__main__':
    try:
        go_to_origin()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass