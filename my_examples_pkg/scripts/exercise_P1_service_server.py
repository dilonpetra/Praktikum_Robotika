#! /usr/bin/env python3

import rospy #import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from exercise_P1_class import MoveBB8

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_specific_time has been called")
    movebb8_object = MoveBB8()
    movebb8_object.move_bb8()
  
    
    movebb8_object.move_bb8(linear_speed=0.0, angular_speed=0.0)
    rospy.loginfo("Finished service move_bb8_in_specific_time")
    response= MyCustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('exercise_p1')
my_service = rospy.Service('/move_bb8_in_specific_time', MyCustomServiceMessage, my_callback)
rospy.loginfo("Service move_bb8_in_specific_time ready")
rospy.spin()

