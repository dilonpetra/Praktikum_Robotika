#! /usr/bin/env python3

import rospy #import rospy
from trajectory_by_name_srv.srv import TrajByName, TrajByNameRequest #import service message yang digunakan oleh service /trajectory_by_name
import sys #import sys

rospy.init_node('service_client') #inisialisasi node dengan nama service_client
rospy.wait_for_service('/trajectory_by_name') #menunggu service /trajectory_by_name dirun
traj_by_name_service = rospy.ServiceProxy('/trajectory_by_name', TrajByName) #membuat koneksi dengan service
traj_by_name_object = TrajByNameRequest() # membuat objek dari TrajByNameRequest
traj_by_name_object.traj_name = "release_food" # mengisi nilai objek dengan nilai tertentu
result = traj_by_name_service(traj_by_name_object) # mengirim nama dari trajectory untuk dieksekusi oleh robot
print(result) #mencetak hasil dari pemanggilan service

