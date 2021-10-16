#! /usr/bin/env python3

import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback

nImage = 1

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received

def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

rospy.init_node('example_with_waitforresult_action_client_node') # initializes the action client node
action_server_name = '/ardrone_action_server'
client = actionlib.SimpleActionClient(action_server_name , ArdroneAction)
rospy.loginfo('Waiting for action Server '+action_server_name)
client.wait_for_server() # waits until the action server is up and running
rospy.loginfo('Action server found.....'+action_server_name)


goal = ArdroneGoal() # creates a goal to send to the action server
goal.nseconds = 10
client.send_goal(goal, feedback_cb=feedback_callback)
rate = rospy.Rate(1)

rospy.loginfo("Lets Start The Wait for the Action To finish Loop...")
while not client.wait_for_result():
    rospy.loginfo("Doing Stuff while waiting for the Server to give a result....")
    rate.sleep()
rospy.loginfo("Example with WaitForResult Finished.")

