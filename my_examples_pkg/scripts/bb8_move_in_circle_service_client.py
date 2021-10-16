#! /usr/bin/env python3


import rospy #import rospy
from std_srvs.srv import Empty, EmptyRequest #import service message dengan empty request dari std_srv


rospy.init_node('service_move_bb8_in_circle_client') #inisialisasi node dengan nama service_move_bb8_in_circle_client
rospy.wait_for_service('/move_bb8_circle') #menunggu service /move_bb8_circle dirun
move_bb8_in_circle_service_client = rospy.ServiceProxy('/move_bb8_circle', Empty) #membuat koneksi dengan service
move_bb8_in_circle_request_object = EmptyRequest() # membuat objek dari empty request
result = move_bb8_in_circle_service_client(move_bb8_in_circle_request_object) # mengirim request objek untuk dieksekusi oleh robot
print(result) #mencetak hasil dari pemanggilan service

