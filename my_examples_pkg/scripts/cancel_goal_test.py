#! /usr/bin/env python3

from typing import Counter
import actionlib
import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback

PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4
nImage = 1

def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

rospy.init_node('example_no_waitforresult_action_client_node') # initializes the action client node
action_server_name = '/ardrone_action_server'
client = actionlib.SimpleActionClient(action_server_name, ArdroneAction) # create the connection to the action server


rospy.loginfo('Waiting for action Server '+action_server_name) 
client.wait_for_server() # waits until the action server is up and running
rospy.loginfo('Action server found.....'+action_server_name)

goal = ArdroneGoal() # creates a goal to send to the action server
goal.nseconds = 10 # indicates, take pictures along 10 seconds

client.send_goal(goal, feedback_cb=feedback_callback)
state_result = client.get_state()

rate = rospy.Rate(1)

rospy.loginfo("state_result: "+str(state_result))
counter = 0

#takeoff

while state_result < DONE:
    rospy.loginfo("Doing Stuff while waiting for the Server to give a result....")
    counter += 1
    rate.sleep()
    state_result = client.get_state()
    rospy.loginfo("state_result: "+str(state_result)+", counter ="+str(counter))
    if counter ==2:
        rospy.logwarn("canceling goal....")
        client.cancel_goal()
        rospy.logwarn("goal canceled")
        state_result = client.get_state()
        rospy.loginfo("Update state_result after Cancel : "+str(state_result)+", counter ="+str(counter))


