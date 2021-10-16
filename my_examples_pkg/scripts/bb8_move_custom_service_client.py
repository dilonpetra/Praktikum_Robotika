#! /usr/bin/env python3

import rospy #import rospy 
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest #import service message 

rospy.init_node('service_move_bb8_in_circle_custom_client') #buat node dengan nama service_move_bb8_in_circle_custom_client
rospy.wait_for_service('/move_bb8_in_circle_custom') #menunggu service /move_bb8_in_circle_custom 

move_bb8_in_circle_service_client = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage) #membuat koneksi dengan service 
move_bb8_in_circle_request_object = MyCustomServiceMessageRequest() # membuat objek request


move_bb8_in_circle_request_object.duration = 10 #set duration request dengan nilai 10
rospy.loginfo("Doing Service Call...") 
result = move_bb8_in_circle_service_client(move_bb8_in_circle_request_object) # mengirim request objek untuk dieksekusi oleh robot
rospy.loginfo(str(result)) # mencetak hasil 
rospy.loginfo("END of Service call...")

