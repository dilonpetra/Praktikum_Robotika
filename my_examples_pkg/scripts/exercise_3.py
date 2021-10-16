#! /usr/bin/env python3

import rospy #import library python untuk ros
from my_examples_pkg.msg import Age #import message Age dari package my_examples_pkg

rospy.init_node('exercise_3') #inisialiasi node dengan nama 'exercise_3'
pub = rospy.Publisher('/age_of_robot', Age, queue_size=1) #membuat publisher objek yang akan mempublish pada topic /age_of_robot dan dengan tipe message Age

rate = rospy.Rate(2) #set rate publish dengan nilai 2 Hz
var = Age() #membuat variabel dengan tipe Age

while not rospy.is_shutdown(): #loop while
    var.years = 2001 #set years = 2001
    var.months = 1 #set months = 1
    var.days = 29 # set days = 29
    pub.publish(var) #publish variabel var
    rate.sleep() #maintance publish rate 2 Hz

