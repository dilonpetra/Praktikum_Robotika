#! /usr/bin/env python3

import rospy #import rospy
from std_srvs.srv import Empty, EmptyResponse
from bb_8_move_circle_class import MoveBB8

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    movebb8_object = MoveBB8()
    movebb8_object.move_bb8()
    rospy.loginfo("Finished service move_bb8_in_circle")
    return EmptyResponse()

rospy.init_node('service_move_bb8_in_circle_server')
my_service = rospy.Service('move_bb8_in_circle', Empty, my_callback)
rospy.loginfo("Service /move_bb8_in_circle ready")
rospy.spin()
