#!/usr/bin/env python

import rospy
import tf
from visualization_msgs.msg import Marker
cntr = 0
intermed_marker = Marker()
flag = True

# function to create a Marker object from the trans and rot array populated by the tf listener
def create_marker(trans, rot):

    # create the Marker object to be returned

    marker = Marker()

    # populate with marker parameters
    #################################
    marker.header.frame_id = "map"
    marker.type = marker.SPHERE
    marker.action = marker.ADD
    marker.header.stamp = rospy.Time.now()

    # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
    marker.type = 2
    marker.id = 0

    # Set the scale of the marker
    marker.scale.x = 0.2
    marker.scale.y = 0.2
    marker.scale.z = 0.2

    # Set the color
    marker.color.r = 0.0
    marker.color.g = 1.0
    marker.color.b = 0.0
    marker.color.a = 1.0

    # Set the pose of the marker
    marker.pose.position.x = trans[0]
    marker.pose.position.y = trans[2]
    marker.pose.position.z = trans[1]
    marker.pose.orientation.x = rot[0]
    marker.pose.orientation.y = rot[1]
    marker.pose.orientation.z = rot[2]
    marker.pose.orientation.w = 1.0
    
    # return the Marker object
    return marker 

def locate_marker():
    # initialize the node
    rospy.init_node('locate_marker_0', anonymous=True)

    # create the TransformListener object
    listener = tf.TransformListener()


    rate = rospy.Rate(10)       # 10 Hz refresh rate

    while not rospy.is_shutdown():
        try:
            # lookup transform between map and fiducial_0 
            (trans,rot) = listener.lookupTransform('/map', '/fiducial_0', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
        # create the publisher object to publish the Marker object to rviz
        publisher = rospy.Publisher('visulization_marker/ArUco_Location_0', Marker, queue_size=50)

        # create the Marker object
        marker = create_marker(trans, rot)

        # publish the Marker object
        publisher.publish(marker)


        rate.sleep()

if __name__ == '__main__':
    try:
        locate_marker()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass