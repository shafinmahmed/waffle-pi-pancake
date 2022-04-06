#!/usr/bin/env python
# from tkinter import SW
import rospy
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalID
from list_of_points.msg import PointArray
from geometry_msgs.msg import Point
point1 = PoseStamped()
point2 = PoseStamped()
point3 = PoseStamped()
point4 = PoseStamped()

# p = PointArray()
# p.points.index

def sub_callback(data):
    if (data != None):
        global point1, point2, point3, point4
        point1.pose.position.x = data.points[0].x
        point1.pose.position.y = data.points[0].y
        point1.pose.position.z = data.points[0].z
        point1.pose.orientation.w = 1.0
        point2.pose.position = data.points[1]
        point2.pose.orientation.w = 1.0
        # populate the PoseStamped object with the odom callback information
        #min.pose.position.y = data.pose.position.y
    
        #min.pose.orientation.w = 1.0


def go_to_path_points():
    rospy.loginfo('GOING TO PATH POINTS')

    # initialize node
    rospy.init_node('go_to_path_points', anonymous=True)

    #subscribe to /tb3_init_pose topic
    #rospy.Subscriber('tb3_init_pose', PoseStamped, ip_callback)

    # Publisher obect to publish goal to return to origin
    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=50)
    rospy.Subscriber('path_points_topic', PointArray, sub_callback)

    newGoal = PoseStamped()
    counter = 1
    global point1
    if(counter == 1):
        newGoal.pose.position = point1
        rospy.loginfo('go to point 1')
        #if(moveBasesuccess or movebasefail)   /move_base/cancel
    
  #  if(counter == 2):
   #     newGoal.pose.position = point2
   
   # if(counter == 3):

    
   # if(counter == 4):


    # newGoal.pose.position.x = 1.0
    # newGoal.pose.position.y = 0.0
    # newGoal.pose.position.z = 0.0
    # newGoal.pose.orientation.w = 1.0
    
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