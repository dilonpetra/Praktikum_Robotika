#! /usr/bin/env python3

import rospy #import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse #import service message
from geometry_msgs.msg import Twist #import twist


def my_callback(request): #definisikan fungsi my_callback
    rospy.loginfo("service /move_bb8_in_circle_custom telah dipanggil") # menset loginfo "service /move_bb8_in_circle_custom telah dipanggil"
    move_circle.linear.x = 0.2 # set nilai linear x = 2
    move_circle.angular.z = 0.2 # set nilaiangular z = 2
    i = 0
    while i <= request.duration:
        my_pub.publish(move_circle) # publish move_circle
        rate.sleep()
        i=i+1

    move_circle.linear.x = 0 # set nilai linear x = 0
    move_circle.angular.z = 0 # set nilaiangular z = 0
    my_pub.publish(move_circle) # publish move_circle
    rospy.loginfo("finished service /move_bb8_in_circle_custom") # menset loginfo "finished service /move_bb8_in_circle_custom"
    response= MyCustomServiceMessageResponse() # menyimpan fMyCustomServiceMessageResponse() pada variable response
    response.success = True # respon.succees = true
    return response # mengembalikan respons 


rospy.init_node('service_move_bb8_in_circle_custom_server') #buat node dengan nama service_move_bb8_in_circle_custom_server
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage, my_callback) #membuat service m/move_bb8_in_circle_custom dengan callback
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) #membuat publisher objek yang akan mempublish pada topic /cmd_vel dan dengan tipe message Twist
move_circle =Twist() # membuat variable dengan tipe twist
rate = rospy.Rate(1) # set rate publish dengan nilai 1 hz
rospy.loginfo("service /move_bb8_in_circle_custom ready") # menset loginfo "service /move_bb8_in_circle_custom ready"
rospy.spin() #maintain service


