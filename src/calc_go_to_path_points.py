#!/usr/bin/env python
# from tkinter import SW
import rospy
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalID
from list_of_points.msg import PointArray
from geometry_msgs.msg import Point
from actionlib_msgs.msg import GoalStatusArray
from actionlib_msgs.msg import GoalStatus
from nav_msgs.msg import Odometry
point1 = PoseStamped()
point2 = PoseStamped()
point3 = PoseStamped()
point4 = PoseStamped()
point5 = PoseStamped()

max = PoseStamped()   # global PoseSstamped object that will be published
max_x = 0
max_y = 0

min = PoseStamped()   # global PoseSstamped object that will be published
min_x = 0
min_y = 0

step_size_y = 0
steps = 3
zcordinate = 0
goalstatus = ''
counter = 1
reduction = 0.0
oldtimer = 0
timesec = 0

# callback function to process subscription data from tb3_max
def sub_callback_max(data):
    if (data != None):
        global max_x, max_y, max
        
            
        max_x = data.pose.position.x
        max_x = max_x - (max_x*reduction)

        # populate the PoseStamped object with the odom callback information
        max.pose.position.x = data.pose.position.x

        max_y = data.pose.position.y
        max_y = max_y - (max_y*reduction)

        # populate the PoseStamped object with the odom callback information
        max.pose.position.y = data.pose.position.y
    
        max.pose.orientation.w = 1.0

# callback function to process subscription data from tb3_min
def sub_callback_min(data):
    if (data != None):
        global min_x, min_y, min
        
            
        min_x = data.pose.position.x
        min_x = min_x + (min_x*reduction)

        # populate the PoseStamped object with the odom callback information
        min.pose.position.x = data.pose.position.x

        min_y = data.pose.position.y
        min_y = min_y + (min_y*reduction)

        # populate the PoseStamped object with the odom callback information
        min.pose.position.y = data.pose.position.y
    
        min.pose.orientation.w = 1.0










asd = GoalStatus().goal_id
a = GoalStatusArray()
# callback function to process subscription data from move_base/status
def sub_callback_status(data):
    if (data != None):
        
        global goalstatus
        goalstatus = data.status_list[len(data.status_list) - 1].status
            
        


    



def calc_go_to_path_points():


    # initialize node
    rospy.init_node('go_to_path_points', anonymous=True)

    # Publisher obect to publish goal to return to origin
    publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=50)
    # subscribe to the /tb3_max topic
    rospy.Subscriber('tb3_max', PoseStamped, sub_callback_max)

    # subscribe to the /tb3_min topic
    rospy.Subscriber('tb3_min', PoseStamped, sub_callback_min)

    # subscribe to the /move_base/status topic
    rospy.Subscriber('move_base/status', GoalStatusArray , sub_callback_status)

    

    newGoal = PoseStamped()
   


 
    
    rate = rospy.Rate(10)

    flag = False

    
    oldtimer = rospy.get_time()
    
    while not rospy.is_shutdown():
        global max, max_x, max_y, counter, timesec, step_size_y
        #calculate step size
        step_size_y = (max_y - min_y)/steps

        # populate with time stamp information of max
        max.header.stamp = rospy.get_rostime()
        max.header.frame_id = 'tb3_max'


        # populate with time stamp information of min
        min.header.stamp = rospy.get_rostime()
        min.header.frame_id = 'tb3_min'
        #Define point 1
        point1.pose.position.x = max_x
        point1.pose.position.y = max_y
        point1.pose.position.z = 0.0
        point1.pose.orientation.w = 1.0
        # rospy.loginfo(max_x)
        
        #Define point 2
        point2.pose.position.x = min_x
        point2.pose.position.y = max_y-step_size_y
        point2.pose.position.z = 0.0
        point2.pose.orientation.w = 1.0

        #Define point 3
        point3.pose.position.x = max_x
        point3.pose.position.y = max_y- (2*step_size_y)
        point3.pose.position.z = 0.0
        point3.pose.orientation.w = 1.0

        #Define point 4
        point4.pose.position.x = min_x
        point4.pose.position.y = min_y
        point4.pose.position.z = 0.0
        point4.pose.orientation.w = 1.0

        #Define point 5 (Home)
        point5.pose.position.x = 0.0
        point5.pose.position.y = 0.0
        point5.pose.position.z = 0.0
        point5.pose.orientation.w = 1.0

        

        
        global counter
        if(counter == 1):
            newGoal.pose.position.x = point1.pose.position.x
            newGoal.pose.position.y = point1.pose.position.y
            newGoal.pose.position.z = point1.pose.position.z
            newGoal.pose.orientation.w = point1.pose.orientation.w
            rospy.loginfo('go to point 1---------------------------------------------------------------------------------------------')
            rospy.loginfo(point1.pose.position.x)
            rospy.loginfo(point1.pose.position.y)
            rospy.loginfo(goalstatus)
            if((goalstatus == 3 and timesec > 10) or timesec > 30):
                flag = False
                counter = counter + 1
                rospy.loginfo('Add counter---------------------------------------------------------------------------------------------')
        if(counter == 2):
            newGoal.pose.position.x = point2.pose.position.x
            newGoal.pose.position.y = point2.pose.position.y
            newGoal.pose.position.z = point2.pose.position.z
            newGoal.pose.orientation.w = point2.pose.orientation.w
            rospy.loginfo('go to point 2---------------------------------------------------------------------------------------------')
            rospy.loginfo(point2.pose.position.x)
            rospy.loginfo(point2.pose.position.y)
            rospy.loginfo(goalstatus)
            if((goalstatus == 3 and timesec > 40) or timesec > 60):
                flag = False
                counter = counter + 1
                rospy.loginfo('Add counter 2---------------------------------------------------------------------------------------------')

        if(counter == 3):
            newGoal.pose.position.x = point3.pose.position.x
            newGoal.pose.position.y = point3.pose.position.y
            newGoal.pose.position.z = point3.pose.position.z
            newGoal.pose.orientation.w = point3.pose.orientation.w
            rospy.loginfo('go to point 3---------------------------------------------------------------------------------------------')
            rospy.loginfo(point3.pose.position.x)
            rospy.loginfo(point3.pose.position.y)
            rospy.loginfo(goalstatus)
            if((goalstatus == 3 and timesec > 70) or timesec > 90):
                flag = False
                counter = counter + 1
                rospy.loginfo('Add counter 3---------------------------------------------------------------------------------------------')


        if(counter == 4):
            newGoal.pose.position.x = point4.pose.position.x
            newGoal.pose.position.y = point4.pose.position.y
            newGoal.pose.position.z = point4.pose.position.z
            newGoal.pose.orientation.w = point4.pose.orientation.w
            rospy.loginfo('go to point 4---------------------------------------------------------------------------------------------')
            rospy.loginfo(point4.pose.position.x)
            rospy.loginfo(point4.pose.position.y)
            rospy.loginfo(goalstatus)
            if((goalstatus == 3 and timesec > 100) or timesec > 120):
                flag = False
                counter = counter + 1
                rospy.loginfo('Add counter 4---------------------------------------------------------------------------------------------')


        if(counter == 5):
            newGoal.pose.position.x = point5.pose.position.x
            newGoal.pose.position.y = point5.pose.position.y
            newGoal.pose.position.z = point5.pose.position.z
            newGoal.pose.orientation.w = point5.pose.orientation.w
            rospy.loginfo('go to point 5---------------------------------------------------------------------------------------------')
            rospy.loginfo(point5.pose.position.x)
            rospy.loginfo(point5.pose.position.y)
            rospy.loginfo(goalstatus)
            if((goalstatus == 3 and timesec > 130) or timesec > 150):
                flag = False
                counter = counter + 1
                rospy.loginfo('Add counter 5---------------------------------------------------------------------------------------------')

        if (flag == False):

            newGoal.header.stamp = rospy.get_rostime()
            newGoal.header.frame_id = 'odom'

            temp = newGoal

            #Publish to move_base
            publisher.publish(temp)
            rospy.loginfo("Going to: ")
            rospy.loginfo(temp)
            #newtime = rospy.get_time()
            timesec = rospy.get_time() - oldtimer
            rospy.loginfo("timer: ")
            rospy.loginfo(timesec)
            

            #flag = True

        rate.sleep()

if __name__ == '__main__':
    try:
        calc_go_to_path_points()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass