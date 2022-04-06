#!/usr/bin/env python
from ast import Global
import rospy
from geometry_msgs.msg import PoseStamped
from list_of_points.msg import PointArray
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry


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

# #create the class point with x and y arguments
# class points:
#     def __init__(self, x =0, y = 0):
#         self.x = x
#         self.y = y




# points = PointArray()
# points.points.append(Point(1,2,0))
# points.points.append(Point(1,3,0))
# points.points.append(Point(1,1,0))
# points.points.append(Point(2,1,0))






def tb3_max_point():
    # initialize the node
    rospy.init_node('tb3_max_point', anonymous=True)

    # subscribe to the /tb3_max
    rospy.Subscriber('tb3_max', PoseStamped, sub_callback_max)

    # subscribe to the /tb3_min
    rospy.Subscriber('tb3_min', PoseStamped, sub_callback_min)



    # create the publisher object to publish the initial pose information to path_points topic
    publisher = rospy.Publisher('path_points_topic', PointArray, queue_size=50)

    rate = rospy.Rate(10)   # 10 Hz refresh rate

    while not rospy.is_shutdown():
        global max, max_x, max_y, step_size_x

        # populate with time stamp information of max
        max.header.stamp = rospy.get_rostime()
        max.header.frame_id = 'tb3_max'


        # populate with time stamp information of min
        min.header.stamp = rospy.get_rostime()
        min.header.frame_id = 'tb3_min'


        #create an instance of point class called p1
        points = PointArray()
        points.points.append(Point(max_x,max_y,0))
        points.points.append(Point(min_x,(max_y-step_size_x),0))
        points.points.append(Point(max_x,(max_y-(step_size_x * 2)),0))
        points.points.append(Point(min_x,min_y,0))
        
        # publish the PoseStamped object
        publisher.publish(points)



        




        
        rospy.loginfo(max_x)

        rate.sleep()

if __name__ == '__main__':
    try:
        tb3_max_point()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
