#!/usr/bin/env python
# from tkinter import SW
import rospy
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalID
from list_of_points.msg import PointArray
from geometry_msgs.msg import Point
from ast import Global


from nav_msgs.msg import Odometry
point1 = PoseStamped()
point2 = PoseStamped()
point3 = PoseStamped()
point4 = PoseStamped()

max = PoseStamped()   # global PoseSstamped object that will be published
max_x = 0
max_y = 0

min = PoseStamped()   # global PoseSstamped object that will be published
min_x = 0
min_y = 0

step_size_x = 0
steps_X = 3
zcordinate = 0

# callback function to process subscription data from tb3_max
def sub_callback_max(data):
    if (data != None):
        global max_x, max_y, max
        
            
        max_x = data.pose.position.x

        # populate the PoseStamped object with the odom callback information
        max.pose.position.x = data.pose.position.x

        max_y = data.pose.position.y

        # populate the PoseStamped object with the odom callback information
        max.pose.position.y = data.pose.position.y
    
        max.pose.orientation.w = 1.0

# callback function to process subscription data from tb3_min
def sub_callback_min(data):
    if (data != None):
        global min_x, min_y, min
        
            
        min_x = data.pose.position.x

        # populate the PoseStamped object with the odom callback information
        min.pose.position.x = data.pose.position.x

        min_y = data.pose.position.y

        # populate the PoseStamped object with the odom callback information
        min.pose.position.y = data.pose.position.y
    
        min.pose.orientation.w = 1.0

#calculate step size
step_size_x = (max_x - min_x)/steps_X



    
    



def calc_go_to_path_points():
    #rospy.loginfo('GOING TO PATH POINTS')

    # initialize node
    rospy.init_node('go_to_path_points', anonymous=True)

    #subscribe to /tb3_init_pose topic
    #rospy.Subscriber('tb3_init_pose', PoseStamped, ip_callback)

    # Publisher obect to publish goal to return to origin
    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=50)
    # subscribe to the /tb3_max
    rospy.Subscriber('tb3_max', PoseStamped, sub_callback_max)

    # subscribe to the /tb3_min
    rospy.Subscriber('tb3_min', PoseStamped, sub_callback_min)
    #rospy.Subscriber('path_points_topic', PointArray, sub_callback)

    newGoal = PoseStamped()
    #counter = 1
    global point2
   # if(counter == 1):
    # newGoal.pose.position.x = point2.pose.position.x
    # newGoal.pose.position.y = point2.pose.position.y
    # newGoal.pose.position.z = point2.pose.position.z
    # newGoal.pose.orientation.w = point2.pose.orientation.w
    # rospy.loginfo('go to point 1')
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
        global max, max_x, max_y, step_size_x

        # populate with time stamp information of max
        max.header.stamp = rospy.get_rostime()
        max.header.frame_id = 'tb3_max'


        # populate with time stamp information of min
        min.header.stamp = rospy.get_rostime()
        min.header.frame_id = 'tb3_min'

        point1.pose.position.x = max_x
        point1.pose.position.y = max_y
        point1.pose.position.z = 0.0
        point1.pose.orientation.w = 1.0
        rospy.loginfo(max_x)
        
        point2.pose.position.x = min_x
        point2.pose.position.y = max_y-step_size_x
        point2.pose.position.z = 0.0
        point2.pose.orientation.w = 1.0

        newGoal.pose.position.x = point2.pose.position.x
        newGoal.pose.position.y = point2.pose.position.y
        newGoal.pose.position.z = point2.pose.position.z
        newGoal.pose.orientation.w = point2.pose.orientation.w
        rospy.loginfo('go to point 1')

        if (flag == False):

            newGoal.header.stamp = rospy.get_rostime()
            newGoal.header.frame_id = 'odom'

            temp = newGoal

            publisher.publish(temp)

            #rospy.loginfo("SENT GOAL TO MOVE BASE")

            # flag = True

        rate.sleep()

if __name__ == '__main__':
    try:
        calc_go_to_path_points()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass