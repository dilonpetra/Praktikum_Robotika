#! /usr/bin/env python3

import rospy #import library python untuk ros
from std_msgs.msg import Int32 #import message Int32 dari package std_msgs

rospy.init_node('topic_publisher') #inisialiasi node dengan nama 'topic_publisher'
pub = rospy.Publisher('/counter', Int32, queue_size=1) #membuat publisher objek yang akan mempublish pada topic /counter dan dengan tipe message Int32

rate = rospy.Rate(2) #set rate publish dengan nilai 2 Hz
count = Int32() #membuat variabel dengan tipe Int32
count.data +=0 #inisialisasi variiable 'count;

while not rospy.is_shutdown(): #loop while
    pub.publish(count) #publish message dengan variable count
    count.data +=1 # increment variable count
    rate.sleep() #maintance publish rate 2 Hz

