#!/usr/bin/env python
from io import StringIO
import rospy
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalID
from std_msgs.msg import Int32
from visualization_msgs.msg import Marker



flag = False    # flag to only send return goal once
markerGoal = PoseStamped()    # PoseStamped object to be published as the goal

# callback function for explore_cancel_0 subscription
def ex_callback_0(data):
    if (data.data == 0):     # condition to trigger move base goals to marker location
        global flag
        flag = True
        rospy.loginfo("MARKER FOUND")

# callback function for /tb3_init_pose subscription 
def locate_callback_0(data):
    if (data != None and flag == True):
        global markerGoal

        # populate PoseStamped object with the data received
        markerGoal.pose.position.x = data.pose.position.x
        markerGoal.pose.position.y = data.pose.position.y
        markerGoal.pose.position.z = 0.0
        markerGoal.pose.orientation.w = 1.0                               #WHAT DO WE MAKE ORIENTATION? nEED TO GO HEAD ON

# callback function for explore_cancel_0 subscription
def ex_callback_1(data):
    if (data.data == 1):     # condition to trigger move base goals to marker location
        global flag
        flag = True

# callback function for /tb3_init_pose subscription 
def locate_callback_1(data):
    if (data != None and flag == True):
        global markerGoal

        # populate PoseStamped object with the data received
        markerGoal.pose.position.x = data.pose.position.x
        markerGoal.pose.position.y = data.pose.position.y
        markerGoal.pose.position.z = 0.0
        markerGoal.pose.orientation.w = 1.0                               #WHAT DO WE MAKE ORIENTATION? nEED TO GO HEAD ON

def go_to_marker():

    # initialize node
    rospy.init_node('go_to_marker', anonymous=True)


    rospy.loginfo('GOING TO MARKER')

    global flag

    # subscribe to explore_cancel (empty string or FOUND 0)
    rospy.Subscriber('explore_cancel_0', Int32, ex_callback_0)
    rospy.Subscriber('explore_cancel_1', Int32, ex_callback_1)

    # subscribe to 
    rospy.Subscriber('visulization_marker/ArUco_Location_0', Marker, locate_callback_0)

    # subscribe to explore_cancel (empty string or FOUND 1)

    # subscribe to 
    rospy.Subscriber('visulization_marker/ArUco_Location_1', Marker, locate_callback_1)


    # Publisher obect to publish goal to return to origin
    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=50)
    
    rate = rospy.Rate(10)

    i = 0

    while not rospy.is_shutdown():
        if (flag == True):  # Check condition for explore_lite completion

            if (i == 0):

                goal = markerGoal

                # publish the PoseStamped object goal
                rospy.loginfo("PUBLISHING MARKER GOAL")
                publisher.publish(goal)
                
                # set flag to false to prevent repeated sending of the goal
                flag = False
            i += 1

        rate.sleep()

if __name__ == '__main__':
    try:
        go_to_marker()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass