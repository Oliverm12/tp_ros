#! /usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

rospy.init_node('rviz_marker')

marker_pub = rospy.Publisher("/marker_1", Marker, queue_size = 2)

marker = Marker()


marker.header.frame_id = "map"
marker.header.stamp = rospy.Time.now()

# set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
marker.type = 2
marker.id = 0

# Set the scale of the marker
marker.scale.x = 0.5
marker.scale.y = 0.5
marker.scale.z = 0.5


# Set the color - Blue
marker.color.r = 0.1
marker.color.g = 0.1
marker.color.b = 0.8
marker.color.a = 1.0

# Set the pose of the marker
marker.pose.position.x = 5
marker.pose.position.y = 2
marker.pose.position.z = 0

marker.pose.orientation.x = 0.0
marker.pose.orientation.y = 0.0
marker.pose.orientation.z = 0.0
marker.pose.orientation.w = 1.0




 # Sphere Marker #2 (A single sphere)
 # A Sphere List with one sphere, this renders a
 # higher-quality sphere than the method above

sphere_marker2 = Marker()
sphere_marker2.header.frame_id = "map"
marker.header.stamp = rospy.Time.now()

sphere_marker2.type = 2
sphere_marker2.id = 1


# Set the scale of the marker
sphere_marker2.scale.x = 2
sphere_marker2.scale.y = 2
sphere_marker2.scale.z = 2

sphere_marker2.pose.position.x = 6
sphere_marker2.pose.position.y = 3
sphere_marker2.pose.position.z = 0


sphere_marker2.pose.orientation.x = 0.0
sphere_marker2.pose.orientation.y = 0.0
sphere_marker2.pose.orientation.z = 0.0
sphere_marker2.pose.orientation.w = 1.0



# Set the color - Blue
marker.color.r = 0.1
marker.color.g = 0.1
marker.color.b = 0.8
marker.color.a = 1.0










while not rospy.is_shutdown():
  marker_pub.publish(marker)

  
  rospy.rostime.wallsleep(1.0)
