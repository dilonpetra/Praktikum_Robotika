#! /usr/bin/env python3

import rospy #import rospy
from std_srvs.srv import Empty, EmptyResponse #import service message

def my_callback(request): #definisikan fungsi my_callback
    print("My_callback has been called") #cetak My_callback has been called
    return EmptyResponse() #kembalikan EmptyResponse()
    #return MyServiceResponse(len(request.words.split()))

rospy.init_node('service_server') #buat node dengan nama service_server
my_service = rospy.Service('/my_service', Empty, my_callback) #membuat service /my_service dengan callback
rospy.spin() #maintain service


