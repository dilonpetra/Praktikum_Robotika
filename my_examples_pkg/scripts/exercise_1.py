#! /usr/bin/env python3

import rospy #import library python untuk ros
from geometry_msgs.msg import Twist #import Twist dari package geometri_msg

rospy.init_node('exercise_1') #inisialiasi node dengan nama 'exercise_1'
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) #membuat publisher objek yang akan mempublish pada topic /cmd_vel dan dengan tipe message Twist

rate = rospy.Rate(2) #set rate publish dengan nilai 2 Hz
var = Twist() #membuat variabel dengan tipe Twist

while not rospy.is_shutdown(): #loop while
    var.linear.x = 1 #set linier x =1
    var.angular.z = 1 #set angular z =1

    pub.publish(var) #publish variabel var
    rate.sleep() #maintance publish rate 2 Hz

