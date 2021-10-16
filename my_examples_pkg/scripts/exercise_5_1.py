#! /usr/bin/env python3

import rospy #import rospy
import rospkg
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest #import service message xecTraj, ExecTrajRequest 

rospy.init_node('service_execute_trajectory_client') #inisialisasi node dengan nama service_execute_trajectory_client
rospy.wait_for_service('/execute_trajectory') #menunggu service /execute_trajectory dirun
execute_trajectory_service_client = rospy.ServiceProxy('/execute_trajectory', ExecTraj) #membuat koneksi dengan service
execute_trajectory_request_object = ExecTrajRequest() # membuat objek dari ExecTrajRequest

rospack = rospkg.RosPack()
trajecetory_file_path = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt" #menentukan directory dari get_food.txt

execute_trajectory_request_object.file = trajecetory_file_path
result=execute_trajectory_service_client(execute_trajectory_request_object)
print(result)

