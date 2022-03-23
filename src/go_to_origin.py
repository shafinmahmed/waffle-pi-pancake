#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalID


flag = False    # flag to only send return goal once
origGoal = PoseStamped()    # PoseStamped object to be published as the goal

# callback function for /move_base/cancel subscription
def mb_callback(data):
    if (data.id == ''):     # condition to trigger sending return to origin goal to move_base_simple/goal
        global flag
        flag = True

# callback function for /tb3_init_pose subscription
def ip_callback(data):
    if (data != None):
        global origGoal

        # populate PoseStamped object with the data received
        origGoal = data


def go_to_origin():
    rospy.loginfo('RETURNING TO ORIGIN')

    # initialize node
    rospy.init_node('go_to_origin', anonymous=True)

    # subscribe to /move_base/cancel topic 
    rospy.Subscriber('move_base/cancel', GoalID, mb_callback)

    #subscribe to /tb3_init_pose topic
    rospy.Subscriber('tb3_init_pose', PoseStamped, ip_callback)

    # Publisher obect to publish goal to return to origin
    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=50)
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if (flag == True):  # Check condition for explore_lite completion
            goal = origGoal

            # publish the PoseStamped object goal
            publisher.publish(goal)
            
            # set flag to false to prevent repeated sending of the goal
            global flag
            flag = False

        rate.sleep()

if __name__ == '__main__':
    try:
        go_to_origin()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass