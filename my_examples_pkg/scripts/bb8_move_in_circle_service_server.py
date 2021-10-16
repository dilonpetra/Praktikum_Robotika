#! /usr/bin/env python3

import rospy #import rospy
from std_srvs.srv import Empty, EmptyResponse #import service message
from geometry_msgs.msg import Twist #import twist

def my_callback(request): #definisikan fungsi my_callback
    rospy.loginfo("service bb8_move_in_circle telah dipanggil") # menset loginfo "service bb8_move_in_circle telah dipanggil"
    move_circle.linear.x = 0.2 # set nilai linear x = 2
    move_circle.angular.z = 0.2 # set nilaiangular z = 2
    my_pub.publish(move_circle) # publish move_circle
    rospy.loginfo("finished service move bb8 in circle") # menset loginfo "finished service move bb8 in circle"
    return EmptyResponse() # mengembalikan respons kosong


rospy.init_node('service_move_bb8_in_circle_server') #buat node dengan nama service_move_bb8_in_circle_server
my_service = rospy.Service('/move_bb8_circle', Empty, my_callback) #membuat service move_bb8_circle dengan callback
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) #membuat publisher objek yang akan mempublish pada topic /cmd_vel dan dengan tipe message Twist
move_circle =Twist() # membuat variable dengan tipe twist
rospy.loginfo("service /move_bb8_circle ready") # menset loginfo "service /move_bb8_circle ready"
rospy.spin() #maintain service


